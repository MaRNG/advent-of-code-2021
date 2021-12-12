import os


def run():
    print(measure_real_data())


def measure_real_data() -> int:
    with open(os.path.join(os.path.dirname(__file__), 'data/input.txt'), 'r') as f:
        lines = f.readlines()

        count: int = measure_depth_increasing(lines)

        return count


def measure_depth_increasing(depth_measurements: []) -> int:
    last_measurement: int = -1
    depth_increased_count: int = 0

    for depthMeasurement in depth_measurements:
        depth_measurement_number = int(depthMeasurement)

        if last_measurement != -1 and depth_measurement_number > last_measurement:
            depth_increased_count += 1

        last_measurement = depth_measurement_number

    return depth_increased_count


run()
