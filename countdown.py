import threading
import time

def countdown():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    print("Зворотний відлік завершено!")

if __name__ == "__main__":
    thread1 = threading.Thread(target=countdown)
    thread1.start()
    print("Основний потік продовжує виконання...")