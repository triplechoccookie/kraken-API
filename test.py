__author__ = 'Karsten'

import analysis
import threading
import concurrent.futures


# lock to serialize console output
lock = threading.Lock()


def worker(a, b):
    with lock:
        print(str(a) + '/' + str(b))
    result = analysis.simulate_trade_on_ma_crossover_with_fees(a, b, 0.002, 100)
    if result['money'] > 100:
        with lock:
            print(str(a) + '/' + str(b) + ': ' + str(result))

if __name__ == '__main__':
    pool = concurrent.futures.ProcessPoolExecutor(1)

    for i in range(8, 100):
        for j in range(1, 100):
            if i > j:
                pool.submit(worker, i, j)

    pool.shutdown()