#! /bin/python3
import ctypes

path = "/home/bandi/ctopy/libfun.so"
c_functions = ctypes.CDLL(path)

c_functions.printer("almafa")

output = c_functions.square(16)

print(output)

output = c_functions.square("al")
c_functions.square.argtypes = [ctypes.c_int]
output = c_functions.square("al")

print(output)
