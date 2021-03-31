import threading
import time
from random import randint

semaphore = threading.BoundedSemaphore(1)
counter = 0


def child_team():
    global counter
    i = randint(1, 100)
    while i > 0:
        try:
            number_of_fighters = i
            i = i - randint(1, 10)
            i = i + randint(1, 10)
            semaphore.acquire()
            # time.sleep(1)
            counter += 1
            print(f'Number of fighters (child) - {number_of_fighters}, counter - {counter}')
            semaphore.release()
        except Exception:
            raise Exception('Counter is blocked')


def parent_team():
    global counter
    i = randint(1, 100)
    threading.Thread(target=child_team).start()
    while i >0:
        try:
            number_of_fighters = i
            i = i - randint(1, 10)
            i = i + randint(1, 10)
            semaphore.acquire()
            # time.sleep(1)
            counter += 1
            print(f'Number of fighters (parent) - {number_of_fighters}, counter - {counter}')
            semaphore.release()
        except Exception:
            raise Exception('Counter is blocked')


if __name__ == '__main__':
    parent = threading.Thread(target=parent_team)
    parent.start()
