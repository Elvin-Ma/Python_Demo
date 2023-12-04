import numpy as np
import sys
import os
import struct
import time

# for nan
import math

def get_bf16_data(f):
    file = open(f, "rb")
    l = os.path.getsize(f)
    array = []
    for i in range(int(l/2)):
        data = file.read(2)
        a = struct.unpack("H", data)[0]
        b = struct.pack("I", a << 16)
        fl = struct.unpack("f", b)
        if math.isnan(fl[0]):
          print(f"[WARNING] FAILED to get bf16 data, encounting nan. ")
        array.append(fl[0])
    return np.array(array, dtype=np.float32)

def get_float32_data(path):
  data = np.fromfile(path, dtype=np.float32)
  return data

def get_uint8_data(path):
  data = np.fromfile(path, dtype=np.uint8)
  return data

def get_int8_data(path):
  data = np.fromfile(path, dtype=np.int8)
  return data

def get_norm_diff(pred, gt, batch_size=1):
  return np.linalg.norm(pred - gt) / batch_size

def data_compare(lhs, rhs):
  if lhs.size != rhs.size:
    print(f"[ERROR] FAILED to match input size: {lhs.size} and {rhs.size}")
    return False

  threshold1 = 0.04
  threshold2 = 0.04
  if lhs.dtype == np.uint8:
    threshold1 = 1.04

  cnt = 0
  length = len(lhs)

  for i in range(length):
    gap = abs(lhs[i] - rhs[i])

    if gap > threshold1 and gap > abs(rhs[i] * threshold2):
      print(f"{i}: abs( {lhs[i]:8.8f} - {rhs[i]:8.8f} ) = {gap:8.8f}")
      cnt += 1

  print(f"[INFO] L2 Norm. Difference: {np.linalg.norm(lhs - rhs)}")
  print(f"[INFO] Mismatch data counter: {cnt}")
  print(f'test data: max {lhs.max():8.8f}, min {lhs.min():8.8f}, mean {lhs.mean():8.8f}')
  print(f'golden data: max {rhs.max():8.8f}, min {rhs.min():8.8f}, mean {rhs.mean():8.8f}')
  
  return (cnt == 0)

if __name__ == "__main__":
  lhs, rhs = 0, 0
  if len(sys.argv) == 3:
      lhs, rhs = get_bf16_data(sys.argv[1]), get_bf16_data(sys.argv[2])
  elif len(sys.argv) == 4:
    if sys.argv[3] == "bf16":
      lhs, rhs = get_bf16_data(sys.argv[1]),  get_bf16_data(sys.argv[2])
    elif sys.argv[3] == "fp32":
      lhs, rhs = get_float32_data(sys.argv[1]), get_float32_data(sys.argv[2])
    elif sys.argv[3] == "int8":
      lhs, rhs = get_int8_data(sys.argv[1]), get_int8_data(sys.argv[2])
    elif sys.argv[3] == "uint8":
      lhs, rhs = get_uint8_data(sys.argv[1]), get_uint8_data(sys.argv[2])
    else:
      print("[ERROR] FAILED to support data type {}".format(sys.argv[3]))
  else:
      print("[ERROR] FAILED to compare since args are invalid")

  if data_compare(lhs, rhs):
    print("SUCCESSED to compare data")
  else:
    print("FAILED to compare data")
