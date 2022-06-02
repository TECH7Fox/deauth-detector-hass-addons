#!/usr/bin/with-contenv bashio
# ==============================================================================
# Starting airmon-ng
# ==============================================================================

# shellcheck shell=bash

bashio::log.info "Starting airmon-ng"
airmon-ng start wlan1
bashio::log.info "Started airmon-ng"