#!/usr/bin/with-contenv bashio
# ==============================================================================
# Stop airmon-ng
# ==============================================================================

# shellcheck shell=bash

bashio::log.info "Stopping airmon-ng"
airmon-ng stop wlan1
bashio::log.info "Stopped airmon-ng"