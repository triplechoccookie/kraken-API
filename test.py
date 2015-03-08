__author__ = 'Karsten'

import analysis
import threading
import concurrent.futures


# lock to serialize console output
lock = threading.Lock()


def worker(a, b):
    with lock:
        print(str(a) + '/' + str(b))
    result = analysis.simulateTradeOnMaCrossoverWithFees(a, b, 0.002, 100)
    if result['money'] > 100:
        with lock:
            print(str(a) + '/' + str(b) + ': ' + str(result))

if __name__ == '__main__':
    pool = concurrent.futures.ProcessPoolExecutor(4)

    for i in range(1, 100):
        for j in range(1, 100):
            if i > j:
                if ((i == 19) and (j >= 14)) or (i > 19):
                    pool.submit(worker, i, j)

    pool.shutdown()