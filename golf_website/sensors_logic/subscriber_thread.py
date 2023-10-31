from paho.mqtt import client
import json
import threading
from golf_website.sensors_logic.data_anlyzer import analyze_swing_data


MQTT_BROKER = 'broker.hivemq.com'


class MQTTSubscriberThread(threading.Thread):

    def __init__(self, mqtt_broker, client_name, topic, qos):
        super().__init__()
        self.mqtt_broker = mqtt_broker
        self.client_name = client_name
        self.topic = topic
        self.qos = qos
        self.swing_results = None
        self.last_message_time = None
        self.messages = list()
        self.event = threading.Event()

    def run(self):

        subscriber = client.Client(self.client_name)
        subscriber.on_message = self.on_message
        subscriber.connect(self.mqtt_broker)
        subscriber.subscribe(self.topic, self.qos)
        print(f"Started listening to: {self.topic}")
        subscriber.loop_start()
        self.event.wait()  # waiting for all the data to be processed before ending the thread
        subscriber.loop_stop()
        subscriber.disconnect()

    def on_message(self, receiver, userdata, message):
        decoded_message = json.loads(message.payload)
        self.messages.append(decoded_message)
        if decoded_message['NOTE'] == 'HIT':
            self.swing_results = analyze_swing_data(self.messages)
            self.event.set()
