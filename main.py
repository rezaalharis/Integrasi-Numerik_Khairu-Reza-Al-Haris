Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import time
import matplotlib.pyplot as plt

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Fungsi integrasi trapezoid
def trapezoid_integration(f, a, b, N):
    x = np.linspace(a, b, N+1)
    y = f(x)
    h = (b - a) / N
    integral = (h/2) * np.sum(y[:-1] + y[1:])
    return integral

# Fungsi untuk menghitung galat RMS
def rms_error(estimation, reference):
    return np.sqrt((estimation - reference)**2)

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Menyimpan hasil untuk analisis
errors = []
times = []

# Menghitung integral, galat, dan waktu eksekusi untuk setiap N
for N in N_values:
    start_time = time.time()
    pi_estimation = trapezoid_integration(f, 0, 1, N)
...     end_time = time.time()
...     execution_time = end_time - start_time
...     error = rms_error(pi_estimation, pi_ref)
...     
...     # Menyimpan hasil
...     errors.append(error)
...     times.append(execution_time)
...     
...     # Output hasil
...     print(f'N = {N}')
...     print(f'Estimated π: {pi_estimation}')
...     print(f'RMS Error: {error}')
...     print(f'Execution Time: {execution_time} seconds\n')
... 
... # Plot hasil galat dan waktu eksekusi
... plt.figure(figsize=(12, 6))
... 
... plt.subplot(1, 2, 1)
... plt.plot(N_values, errors, 'o-', label='RMS Error')
... plt.xlabel('N')
... plt.ylabel('RMS Error')
... plt.xscale('log')
... plt.yscale('log')
... plt.title('RMS Error vs N')
... plt.grid(True)
... plt.legend()
... 
... plt.subplot(1, 2, 2)
... plt.plot(N_values, times, 'o-', label='Execution Time')
... plt.xlabel('N')
... plt.ylabel('Time (seconds)')
... plt.xscale('log')
... plt.yscale('log')
... plt.title('Execution Time vs N')
... plt.grid(True)
... plt.legend()
... 
... plt.tight_layout()
... plt.show()
