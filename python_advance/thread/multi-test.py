import threading
import time


class Fun:

    @staticmethod
    def fun(fun_obj, fun_name: str, i):
        return getattr(fun_obj, fun_name)(0, i)


lock = threading.Lock()


class Test:

    @staticmethod
    def add(a, b):
        time.sleep(3)
        with lock:
            print(a + b)
        return


def multi():
    threads = []
    for i in range(100):
        threads.append(threading.Thread(target=Fun.fun, kwargs={
            'fun_obj': Test, 'fun_name': 'add', 'i': i}))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    multi()
