import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from scipy.optimize import curve_fit

start = 80
stop = 161

raw_data = read_csv("1.0_P_Oscillations_Data.csv")
time_data = raw_data.get("Time (s)").to_numpy()[start:stop]
temp_data = raw_data.get("Temperature (K)").to_numpy()[start:stop]

def sin(time, wavelength, phase, amplitude, offset):
    return offset + amplitude * np.sin((time / wavelength) + phase)

[fit, fit_cov] = curve_fit(sin, time_data, temp_data)

print(*fit)

fit_time = np.arange(time_data[0], time_data[-1], 0.01)
fit_amp = sin(fit_time, *fit)

fig, ax = plt.subplots()
ax.plot(time_data, temp_data)
ax.plot(fit_time, fit_amp)
plt.show()
