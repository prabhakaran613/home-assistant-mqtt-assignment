# home-assistant-mqtt-assignment

This repository contains a simple example of using MQTT with Home Assistant.  
It includes a Python script to publish MQTT messages and a Home Assistant configuration file.

## Files

- `mqtt_publish.py` – Python script that connects to the MQTT broker and publishes a message.
- `configuration.yaml` – Home Assistant configuration that subscribes to the MQTT topic and exposes the data as an entity.

## Requirements

- Python 3
- MQTT broker (for example: Mosquitto)
- Home Assistant

## Setup

1. Install the `paho-mqtt` Python package:


2. Update `mqtt_publish.py` with your MQTT broker host, port, topic, and payload.

3. Update the MQTT section in `configuration.yaml` with the same topic and any entity name required by the assignment.

4. Restart Home Assistant to load the updated configuration.

## Usage

1. Run the Python script to publish a test message:


2. Open Home Assistant and verify that the MQTT entity shows the received value.

3. Use this setup to demonstrate end‑to‑end communication between the Python publisher and Home Assistant via MQTT.

