ARG BUILD_ARCH=amd64
ARG BUILD_FROM=ghcr.io/hassio-addons/debian-base/${BUILD_ARCH}:5.3.0

FROM $BUILD_FROM

# Install dependecies
RUN apt-get update && apt-get install -y \
    aircrack-ng \
    iproute2 \
    kmod \
    procps \
    python3 \
    pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    scapy \
    cryptography \
    matplotlib \
    requests

COPY rootfs /