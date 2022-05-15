import time
class MeasureTime():
    def __init__(self, measurements, key, cpu_run=False):
        self.measurements = measurements
        self.key = key

    def __enter__(self):
        self.t0 = time.perf_counter() # 记录开始时间

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.measurements[self.key] = time.perf_counter() - self.t0 # 计算执行时间

if __name__ == "__main__":
  measurements = {}

  with MeasureTime(measurements, "pre_processing"):
    for i in range(10000):
       i*i

  print(measurements)
