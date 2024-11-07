import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv

raw_data_05_I = read_csv("1.5_Good_Control_0.5_I.csv")
raw_data_10_I = read_csv("1.2_Good_Control_0.5_P.csv")
raw_data_20_I = read_csv("1.6_Good_Control_2.0_I.csv")

time_data_05_I = raw_data_05_I.get("Time (s)").to_numpy()
temp_data_05_I = raw_data_05_I.get("Temperature (K)").to_numpy()
temp_data_05_I_trunc = temp_data_05_I[170:]

time_data_10_I = raw_data_10_I.get("Time (s)").to_numpy()
temp_data_10_I = raw_data_10_I.get("Temperature (K)").to_numpy()
temp_data_10_I_trunc = temp_data_10_I[175:]

time_data_20_I = raw_data_20_I.get("Time (s)").to_numpy()
temp_data_20_I = raw_data_20_I.get("Temperature (K)").to_numpy()
temp_data_20_I_trunc = temp_data_20_I[142:]

def sigma(data):
    n = len(data)
    mean_T = sum(data)/n
    summation = sum((data - mean_T) ** 2)
    return np.sqrt((1 / (n - 1)) * summation)

fig, ax = plt.subplots()
ax.hlines(10, xmin=0, xmax=110, linestyle="dashed", color='k')
ax.hlines((9.95, 10.05), xmin=0, xmax=110, linestyle="dotted", color='k')
ax.vlines(0, ymin=7.7, ymax=10.7, linestyle="dashed", color='k')
ax.plot(time_data_05_I-2.261, temp_data_05_I, color="lime", label=f"0.5I - σ: {sigma(temp_data_05_I_trunc):0.2f} - stabilisation time: 47s")
ax.plot(time_data_10_I-5.262, temp_data_10_I, color="green", label=f"1.0I - σ: {sigma(temp_data_10_I_trunc):0.2f} - stabilisation time: 48s")
ax.plot(time_data_20_I-2.506, temp_data_20_I, color="cyan", label=f"2.0I - σ: {sigma(temp_data_20_I_trunc):0.2f} - stabilisation time: NAs")
ax.set_title("Tempterature Oscillations { P=0.6, I=3.42 }")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Temperature (K)")
ax.legend(loc="lower right")
fig.savefig("Good_Control_Graph_I.png")
plt.show()

