import time


def fibo(a):
    for _ in range(a):
        a += 1
    return a


def main():
    """Печать 1000 элемента последовательности Фибоначчи"""
    tic = time.perf_counter()
    result = fibo(1000)
    toc = time.perf_counter()
    print(f"Вычисление заняло {toc - tic:0.16f} секунд")
    print(result)


if __name__ == "__main__":
    main()