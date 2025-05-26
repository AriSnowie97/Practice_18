import threading
import random

def sum_part(data_part, results, index):
    results[index] = sum(data_part)

if __name__ == "__main__":
    data = [random.randint(1, 100) for _ in range(1000)]
    n_threads = 4
    chunk_size = len(data) // n_threads
    remainder = len(data) % n_threads
    threads = []
    results = [0] * n_threads
    start_index = 0

    for i in range(n_threads):
        end_index = start_index + chunk_size + (1 if i < remainder else 0)
        data_part = data[start_index:end_index]
        thread = threading.Thread(target=sum_part, args=(data_part, results, i))
        threads.append(thread)
        thread.start()
        start_index = end_index

    for thread in threads:
        thread.join()

    total_sum = sum(results)
    print(f"Загальна сума: {total_sum}")