import numpy as np
import matplotlib.pyplot as plt
import re
from pandas import read_csv
from scipy.optimize import curve_fit


def sigmoid(x, a, b, c):
    return (a / (1 + np.exp(-b * (x + c))))

def get_data(file, start, stop, current, init_vals):
    file_data = read_csv(file)
    volt_data = file_data.get("Amplitude (V)").to_numpy()[start:stop]
    temp_data = file_data.get("Temperature (K)").to_numpy()[start:stop]
    resi_data = volt_data/current
    fit, _ = curve_fit(sigmoid, temp_data, resi_data, p0=init_vals)
    temp_start, temp_stop = temp_data[0], temp_data[-1]
    if temp_start < temp_stop:
        temp_fit = np.arange(temp_start, temp_stop, 0.01)
    else:
        temp_fit = np.arange(temp_stop, temp_start, 0.01)
    volt_fit = sigmoid(temp_fit, *fit)
    label = re.findall(r'(\d\.\dK_to_\d\.\dK)', file)
    return ((temp_data, resi_data, f"Data: {label[0]}"), (temp_fit, volt_fit, f"Fit: {label[0]}"), fit)


data_22 = get_data("2.2_Ramp_8.9K_to_8.4K.csv", 0, 238, 9.5e-4, [3.762, 36, -8.7])
data_23 = get_data("2.3_Ramp_8.4K_to_8.9K.csv", 0, 238, 9.5e-4, [3.76, 36, -8.65])

data_runs = (data_22, data_23)

markers = ["o", "x", "D"]
linestyles = ["dashed", "dashdot", "dotted"]
fig, ax = plt.subplots()
for i, data in enumerate(data_runs):
    ax.scatter(data[0][0], data[0][1], color=(0, 0, 0), marker=markers[i], label=data[0][2])
    ax.plot(data[1][0], data[1][1], color=(0.5, 0.5, 0.5), linestyle=linestyles[i], label=data[1][2])
#ax.hlines((3.762, 0), xmin=8.3, xmax=8.9, color='k', linestyle="dotted")
ax.set_title("Resistance vs Temperature { P=0.8, I=5.46, D=0 }")
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Resistance (Ω)")
ax.legend(loc="lower right")
fig.savefig("2.2-3.png", dpi=300)

plt.show()
