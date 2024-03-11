from itertools import combinations


def calculate_max_concurrent_time(processes):
    max_concurrent_time = 0

    for combo in combinations(processes.keys(), 4):
        current_time = 0
        dependencies = set()

        for process_id in combo:
            current_time += processes[process_id][0]
            dependencies.update(processes[process_id][1])

        # Check if all dependencies are satisfied
        if all(dep not in combo for dep in dependencies):
            max_concurrent_time = max(max_concurrent_time, current_time)

    return max_concurrent_time


if __name__ == "__main__":
    with open('7.csv') as f:
        di = {}
        for i in f.readlines():
            da = i.replace('"', '').split(';')
            z = [int(j) for j in da[2:]]
            di[int(da[0])] = [int(da[1]), z]
    print(di)
    max_concurrent_time = calculate_max_concurrent_time(di)
    print("Максимальная продолжительность отрезка времени:", max_concurrent_time, "мс")
