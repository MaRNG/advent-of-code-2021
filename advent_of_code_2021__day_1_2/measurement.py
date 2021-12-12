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

    measurements_to_sum = []

    for depth_measurement in depth_measurements:
        depth_measurements_number = int(depth_measurement)

        if measurements_to_sum.__len__() < 3:
            measurements_to_sum.append(depth_measurements_number)
        elif measurements_to_sum.__len__() == 3:
            measurements_to_sum.pop(0)
            measurements_to_sum.append(depth_measurements_number)

        if measurements_to_sum.__len__() == 3:
            current_sum = 0

            for number in measurements_to_sum:
                current_sum += number

            if last_measurement != -1 and current_sum > last_measurement:
                depth_increased_count += 1

            last_measurement = current_sum

    return depth_increased_count


run()
