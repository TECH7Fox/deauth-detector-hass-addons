#!/usr/bin/with-contenv bashio
# ==============================================================================
# Creating sensor.deauth-detector
# ==============================================================================

# shellcheck shell=bash

bashio::log.info "Creating sensor.deauth-detector..."
curl -X POST -H "Authorization: Bearer ${SUPERVISOR_TOKEN}" \
    -H "Content-Type: application/json" \
    -d '{
        "state": "",
        "attributes": {
            "icon": "mdi:wifi-alert",
            "friendly_name": "Last Deauth Detected",
            "device_class": "timestamp",
            "address 1": "",
            "address 2": "",
            "address 3": "",
        }
    }' \
    http://supervisor/core/api/states/sensor.deauth_detector
bashio::log.info "sensor.deauth-detector created"