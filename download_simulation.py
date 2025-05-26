import threading
import time
import random

def simulate_download(file_name):
    duration = random.uniform(3, 5)
    print(f"Початок завантаження '{file_name}'...")
    time.sleep(duration)
    print(f"Завантаження '{file_name}' завершено за {duration:.2f} секунд.")

if __name__ == "__main__":
    threads = [
        threading.Thread(target=simulate_download, args=("file1.txt",)),
        threading.Thread(target=simulate_download, args=("image.png",)),
        threading.Thread(target=simulate_download, args=("document.pdf",)),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()  # Дочекатися завершення всіх потоків

    print("Всі завантаження завершено.")