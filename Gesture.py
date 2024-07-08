import serial

# Set the serial port
ser = serial.Serial('/dev/ttyACM0', 9600)




# Read Arduino data
def read_arduino_data():
    data = ser.readline().decode('utf-8').strip()
    if data:
        laser_data, distance_data = data.split(';')
        laser_states = list(map(int, laser_data.split(',')))
        distances = list(map(int, distance_data.split(',')))
        return laser_states, distances
    return None, None

# Detect broken lasers
