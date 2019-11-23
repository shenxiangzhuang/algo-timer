from algotimer import Timer, TimerPloter


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fibMemo(n):
    cache = {1: 1, 2: 1}

    def rec(n):
        if n not in cache:
            cache[n] = rec(n - 1) + rec(n - 2)
        return cache[n]
    return rec(n)


if __name__ == '__main__':
    with Timer('fib, 30') as t:
        print('fib(30) = ', fib(30))

    with Timer('fib, 35') as t:
        print('fib(35) = ', fib(35))

    with Timer('fibMemo, 30') as t:
        print('fibMemo(30) = ', fibMemo(30))

    with Timer('fibMemo, 35') as t:
        print('fibMemo(35) = ', fibMemo(35))

    ploter = TimerPloter()
    ploter.plot()
