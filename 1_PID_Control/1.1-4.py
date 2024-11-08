import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv

raw_data_10_P = read_csv("1.1_Good_Control_1.0_P.csv")
time_data_10_P = raw_data_10_P.get("Time (s)").to_numpy()
temp_data_10_P = raw_data_10_P.get("Temperature (K)").to_numpy()
temp_data_10_P_trunc = temp_data_10_P[149:]

raw_data_05_P = read_csv("1.2_Good_Control_0.5_P.csv")
time_data_05_P = raw_data_05_P.get("Time (s)").to_numpy()
temp_data_05_P = raw_data_05_P.get("Temperature (K)").to_numpy()
temp_data_05_P_trunc = temp_data_05_P[216:]


raw_data_20_P = read_csv("1.3_Good_Control_2.0_P.csv")
time_data_20_P = raw_data_20_P.get("Time (s)").to_numpy()
temp_data_20_P = raw_data_20_P.get("Temperature (K)").to_numpy()
temp_data_20_P_trunc = temp_data_20_P[60:]

raw_data_15_P = read_csv("1.4_Good_Control_1.5_P.csv")
time_data_15_P = raw_data_15_P.get("Time (s)").to_numpy()
temp_data_15_P = raw_data_15_P.get("Temperature (K)").to_numpy()
temp_data_15_P_trunc = temp_data_15_P[75:] 

def sigma(data):
    n = len(data)
    mean_T = sum(data)/n
    summation = sum((data - mean_T) ** 2)
    return np.sqrt((1 / (n - 1)) * summation)

fig, ax = plt.subplots()
ax.hlines(10, xmin=0, xmax=110, linestyle="dashed", color='k')
ax.hlines((9.95, 10.05), xmin=0, xmax=110, linestyle="dotted", color='k')
ax.vlines(0, ymin=7.7, ymax=10.7, linestyle="dashed", color='k')
ax.plot(time_data_05_P-5.258, temp_data_05_P, color="lime", label=f"0.5P - σ: {sigma(temp_data_05_P_trunc):0.2f} - stabilisation time: 48s")
ax.plot(time_data_10_P-5.519, temp_data_10_P, color='green', label=f"1.0P - σ: {sigma(temp_data_10_P_trunc):0.2f} - stabilisation time: 35s")
ax.plot(time_data_15_P-2.759, temp_data_15_P, color='blue', label=f"1.5P - σ: {sigma(temp_data_15_P_trunc):0.2f} - stabilisation time: 30s")
ax.plot(time_data_20_P-2.759, temp_data_20_P, color='cyan', label=f"2.0P - σ: {sigma(temp_data_20_P_trunc):0.2f} - stabilisation time: 27s")
ax.set_title("Tempterature Oscillations { P=1.2, I=3.42 }")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Temperature (K)")
ax.legend(loc="lower right")

fig.savefig("Good_Control_Graph_P.png", dpi=300)

plt.show()

