import time


def measure_time(method):
    def timed(*args, **kwargs):
        start = time.time()
        result = method(*args, **kwargs)
        stop = time.time()
        print(f"'{method.__name__}' time[s]: {stop - start}")
        return result

    return timed
