import math
from datetime import datetime


def analyze_swing_data(data: list) -> dict:
    sorted_data = sorted(data, key=lambda x: datetime.strptime(x['Timestamp'], '%Y-%m-%dT%H:%M:%S.%f%z'))

    x_velocity = y_velocity = z_velocity = 0
    previous_message = sorted_data.pop(0)

    for current_message in sorted_data:
        x_velocity, y_velocity, z_velocity = calculate_velocity(x_velocity, y_velocity, z_velocity, previous_message,
                                                                current_message)
        previous_message = current_message

    return calculate_trajectory_data(x_velocity, y_velocity, z_velocity)


def calculate_velocity(previous_x_velocity, previous_y_velocity, previous_z_velocity, previous_message, current_message):
    time_diff = datetime.strptime(current_message['Timestamp'], '%Y-%m-%dT%H:%M:%S.%f%z') - datetime.strptime(
        previous_message['Timestamp'], '%Y-%m-%dT%H:%M:%S.%f%z')
    time_diff_in_seconds = time_diff.total_seconds()

    x_velocity = previous_message['Acceleration']['LinearX']*time_diff_in_seconds + previous_x_velocity
    y_velocity = previous_message['Acceleration']['LinearY'] * time_diff_in_seconds + previous_y_velocity
    z_velocity = previous_message['Acceleration']['LinearZ'] * time_diff_in_seconds + previous_z_velocity

    return x_velocity, y_velocity, z_velocity


def calculate_trajectory_data(x_velocity, y_velocity, z_velocity):
    if y_velocity < 0:
        print("\nhorizontal velocity is negative!")
        return {'distance': -1, 'swing_speed': -1}

    gravity = 9.8

    horizontal_velocity = math.sqrt(x_velocity**2 + z_velocity**2)
    flight_time = (y_velocity/gravity)*2
    distance = horizontal_velocity*flight_time
    swing_speed = math.sqrt(horizontal_velocity**2 + y_velocity**2)

    return {'distance': distance, 'swing_speed': swing_speed}

