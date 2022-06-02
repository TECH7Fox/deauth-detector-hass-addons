import sys
import json
from requests import post
from scapy.all import Dot11Deauth, sniff
from datetime import datetime
from datetime import timedelta

monitor_device = sys.argv[1]
SUPERVISOR_TOKEN = sys.argv[2]

class DeauthenticationDetector:
    def __init__(self, *args, **kwargs):
        '''
        All Arguments And Keywords Will Directly Passed To
        Python Scapy Sniff Function.
        '''
        self.args = args
        self.kwargs = kwargs
        self.Sniffing_Start()
        self.latest = datetime.now()

    def extract_packets(self, pkt):
        '''
        Function For Extracting Packets.
          This Function Is Specially Created For Filtering 
          Deauthentication Packets.
        '''
        if pkt.haslayer(Dot11Deauth):
            if pkt.addr2 is not None and pkt.addr3 is not None:
                if self.latest >= datetime.now() - timedelta(seconds=10):
                    return
                
                now = datetime.now()
                self.latest = now
                time = now.strftime("%H:%M:%S")

                addr1 = pkt.addr1
                addr2 = pkt.addr2
                addr3 = pkt.addr3
                # flag = str(pkt.ChannelFlags)
                # signalStrength = str(pkt.dBm_AntSignal)
                # length = str(pkt.len)
                # reason = str(pkt.reason)
                print(f"[{time}] Detected deauth! Target: {addr1} <-> {addr2}")
                
                headers = {
                    'Authorization': 'Bearer ' + SUPERVISOR_TOKEN,
                    'Content-Type': 'application/json'
                }
                data = {
                    "state": f"{now}",
                    "attributes": {
                        "icon": "mdi:wifi-alert",
                        "friendly_name": "Last Deauth Detected",
                        "device_class": "timestamp",
                        "address 1": f"{addr1}",
                        "address 2": f"{addr2}",
                        "address 3": f"{addr3}",
                    }
                }
                post('http://supervisor/core/api/states/sensor.deauth_detector', headers=headers, data=json.dumps(data))
        return

    def Sniffing_Start(self):
        '''
        Function For Creating Python Scapy.sniff Function
        '''
        sniff(prn=self.extract_packets, store=0, *self.args, **self.kwargs)
        return

time = datetime.now().strftime("%H:%M:%S")
print(f"[{time}] Started monitoring on {monitor_device}")
DeauthenticationDetector(iface=monitor_device)