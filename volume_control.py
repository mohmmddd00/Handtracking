import math
import subprocess

def get_distance(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

def set_volume(dist, min_dist=0.02, max_dist=0.3):
    level = (dist - min_dist) / (max_dist - min_dist) * 100
    level = max(0, min(100, level))  # Clamp between 0 and 100

    script = f"set volume output volume {int(level)}"
    subprocess.run(["osascript", "-e", script], capture_output=True)

    return level

def handle_volume_control(hand_landmark):
    thumb = hand_landmark.landmark[4]
    index = hand_landmark.landmark[8]
    distance = get_distance(thumb, index)
    volume = set_volume(distance)

    return volume