import threading
import time
from random import randint

semaphore = threading.BoundedSemaphore(1)
counter = 0


def shrinking_team():
    global counter
    i = randint(1, 100)
    while i > 0:
        number_of_fighters = i
        i = i - randint(1, 10)
        semaphore.acquire()
        # time.sleep(1)
        counter += 1
        print(f'Number of fighters (shrinking) - {number_of_fighters}, Counter - {counter}')
        semaphore.release()
        if i < 0:
            print("All first team fighters were killed")


def growing_team():
    global counter
    i = randint(1, 100)
    while i < 150:
        number_of_fighters = i
        i = i + randint(1, 10)
        semaphore.acquire()
        # time.sleep(1)
        counter += 1
        print(f'Number of fighters (growing) - {number_of_fighters}, Counter - {counter}')
        semaphore.release()
        if i > 150:
            print("The number of fighters has reached the maximum")


if __name__ == '__main__':
    firstProcess = threading.Thread(target=shrinking_team)
    secondProcess = threading.Thread(target=growing_team)

    firstProcess.start()
    secondProcess.start()

    firstProcess.join()
    secondProcess.join()
