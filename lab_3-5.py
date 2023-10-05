import time
import math

# math.pow
start_time = time.perf_counter()
result_pow = math.pow(4.7, 2)
end_time = time.perf_counter()
elapsed_time_pow = end_time - start_time
print(f"Using math.pow: 2^2 = {result_pow}, Elapsed Time: {elapsed_time_pow} seconds")

# **
start_time = time.perf_counter()
result_operator = 4.7 ** 2
end_time = time.perf_counter()
elapsed_time_operator = end_time - start_time
print(f"Using ** Operator: 2^2 = {result_operator}, Elapsed Time: {elapsed_time_operator} seconds")

# both methods get to the same answer "22.090000000000003"