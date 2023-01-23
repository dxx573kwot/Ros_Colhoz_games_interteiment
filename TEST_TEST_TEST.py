import threading


def ddd():
    a = 0
    while a < 10000000:
        a += 1


if __name__ == '__main__':
    p = threading.Thread(target=ddd)
    p.start()
    while p.is_alive():
        print(0)
    print(1)
