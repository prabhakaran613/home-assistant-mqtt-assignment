import paho.mqtt.client as mqtt
import time
import json

student_name = "S Prabhakaran"
unique_id = "42130632"
topic = "home/prabhakaran-2025/sensor"

broker = "192.168.1.10"
port = 1883

username = "mqtt"
password = "Prabha@10139"

def on_connect(client, userdata, flags, rc):
    print("Connect result code:", rc)

client = mqtt.Client(client_id="prabhakaran_ha_sensor")
client.username_pw_set(username, password)
client.on_connect = on_connect

client.connect(broker, port, keepalive=60)
client.loop_start()

print(f"Connecting to broker: {broker} port: {port}\n")

print(f"Publishing sensor data to topic: {topic}")
print(f"Student: {student_name} | Register: {unique_id}\n")

while True:
    data = {
        "temperature": 25,
        "humidity": 60,
        "gas_level": 80
    }
    client.publish(topic, json.dumps(data))
    print(f"[{time.strftime('%H:%M:%S')}] Sent:", data)
    time.sleep(3)
