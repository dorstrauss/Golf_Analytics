import json
from paho.mqtt import client


def on_message(receiver, userdata, message):
    decoded_message = json.loads(message.payload)
    print("Received message: ", str(message.payload.decode("utf-8")))

def start_listening():
    mqtt_broker = "broker.emqx.io"  # the address of our broker
    receiver = client.Client("Swing_receiver")  # creating the subscriber client
    receiver.connect(mqtt_broker)

    print("Started listening")
    receiver.subscribe("POSITION", qos=0)
    receiver.on_message = on_message
    receiver.loop_forever()
