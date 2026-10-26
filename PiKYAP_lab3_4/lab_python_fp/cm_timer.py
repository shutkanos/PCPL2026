import contextlib, time

class cm_timer_1:
    def __enter__(self):
        self.timer = time.time()
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"time: {time.time() - self.timer}")

@contextlib.contextmanager
def cm_timer_2():
    timer = time.time()
    yield
    print(f"time: {time.time() - timer}")

if __name__ == "__main__":
    with cm_timer_1():
        time.sleep(0.9)
    with cm_timer_2():
        time.sleep(0.8)