import time, datetime, json
from paho.mqtt import client


def simulate(sensor_id: str, mqtt_broker: str, publisher_name: str, topic: str):

    publisher = client.Client(publisher_name)
    publisher.connect(mqtt_broker)
    swing_id = f"{sensor_id}-{datetime.datetime.now()}"

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 0, 'LinearY': 0, 'LinearZ': 0}, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:56.4440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:56.5440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:56.6440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:56.7440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:56.8440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:56.9440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:57.0440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:57.1440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:57.2440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:57.3440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:57.4440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:57.5440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:57.6440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:57.7440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:57.8440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:57.9440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:58.0440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:58.1440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:58.2440+0300', 'NOTE': ''}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)

    sensor_data = {'sensor_id': sensor_id, 'Acceleration': {'LinearX': 1, 'LinearY': 2, 'LinearZ': 0}, 'Timestamp': '2023-10-26T18:07:58.3440+0300', 'NOTE': 'HIT'}
    json_data = json.dumps(sensor_data, indent=4)
    publisher.publish(topic, json_data, qos=0)
    publisher.loop()  # ensure the message will be delivered
    print('message sent')
    time.sleep(0.1)


simulate(sensor_id='08174AE2-EF6A-407D-80B7-2D6AACD2836E', mqtt_broker='broker.hivemq.com',
         publisher_name='golf_sensor', topic='Golf-Analytics/7')

