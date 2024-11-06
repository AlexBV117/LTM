import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from scipy.signal import find_peaks 

start = 80
stop = 180

raw_data = read_csv("1.0_P_Oscillations_Data.csv")

time_data = raw_data.get("Time (s)").to_numpy()
temp_data = raw_data.get("Temperature (K)").to_numpy()

time_data_trunc = time_data[start:stop]
temp_data_trunc = temp_data[start:stop]

peaks_index = find_peaks(temp_data_trunc)[0]
peaks_pos = time_data_trunc[peaks_index]

period = []
for i in range(len(peaks_pos)-1):
    period.append(peaks_pos[i+1] - peaks_pos[i])
period_avg = sum(period)/len(period)

print(f"The average period of oscillation is: {period_avg:1.2f}s")

fig, ax = plt.subplots()
ax.plot(time_data, temp_data, color='k', label="Full Data Run")
ax.plot(time_data_trunc, temp_data_trunc, color='r', label="Region of Interest")
ax.set_title("Tempterature Oscillations with P=2")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Temperature (K)")
for peak in peaks_pos:
    col = (np.random.random(), np.random.random(), np.random.random())
    ax.vlines(peak, ymin=9.96, ymax=10.01, linestyle="dashed", color=col, label=f"TIME: {peak:2.2f}s")
ax.legend(loc="upper right")

fig.savefig("1.0_Oscillations_Graph.png")

plt.show()

