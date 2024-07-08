import serial
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque

# 设置串行端口
ser = serial.Serial('/dev/ttyUSB0', 9600)  # 根据实际情况调整端口

# 定义激光传感器的数量
NUM_SENSORS = 24
# 设置图表的队列长度
QUEUE_LENGTH = 20
# 手势检测的阈值
SWEEP_THRESHOLD = 5
DISTANCE_THRESHOLD = 20

# 初始化队列
laser_queue = deque(maxlen=QUEUE_LENGTH)
distances_queue = deque(maxlen=QUEUE_LENGTH)
# 初始化坏掉的激光传感器列表
broken_sensors = []


def read_arduino_data():
    data = ser.readline().decode('utf-8').strip()
    if data:
        try:
            laser_data, distance_data = data.split(';')
            laser_states = list(map(int, filter(None, laser_data.split(','))))
            distances = list(map(int, filter(None, distance_data.split(','))))
            return laser_states, distances
        except ValueError as e:
            print(f"Error parsing data: {data}")
            print(e)
    return None, None


def detect_broken_sensors():
    global broken_sensors
    # 读取多次数据来确定哪些传感器是坏的
    for _ in range(10):
        laser_states, _ = read_arduino_data()
        if laser_states is not None:
            for i in range(NUM_SENSORS):
                if laser_states[i] == 0:
                    broken_sensors.append(i)
    broken_sensors = list(set(broken_sensors))


def update_queues(laser_states, distances):
    laser_queue.append(laser_states)
    distances_queue.append(distances)


def plot_laser_harp(ax):
    ax.clear()
    ax.set_xlim(0, NUM_SENSORS)
    ax.set_ylim(0, 30)
    ax.set_xticks(range(NUM_SENSORS))
    ax.set_yticks(range(0, 31, 5))
    ax.set_title('Laser Harp Sensor States')

    # 绘制激光竖琴的状态
    if laser_queue:
        latest_states = laser_queue[-1]
        for i in range(NUM_SENSORS):
            if i in broken_sensors:
                ax.plot([i, i], [0, 30], color='gray', linestyle='--')
            else:
                color = 'red' if latest_states[i] == 0 else 'green'
                ax.plot([i, i], [0, 30], color=color)

                if latest_states[i] == 0:
                    height = calculate_height(distances_queue[-1])
                    ax.plot(i, height, 'o', color='blue')


def calculate_height(distances):
    if not distances:
        return 0
    avg_distance = sum(distances) / len(distances)
    # 将距离转换为图中的高度
    return (avg_distance - 7) * (30 / 20)


def update(frame):
    laser_states, distances = read_arduino_data()
    if laser_states is not None and distances is not None:
        update_queues(laser_states, distances)

    plot_laser_harp(ax1)


# 初始化绘图
fig, ax1 = plt.subplots(figsize=(12, 8))

# 检测坏掉的激光传感器
detect_broken_sensors()

ani = FuncAnimation(fig, update, interval=50)

plt.tight_layout()
plt.show()
