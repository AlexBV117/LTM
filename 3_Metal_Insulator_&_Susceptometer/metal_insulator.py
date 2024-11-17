import numpy as np
import matplotlib.pyplot as plt
import re
from pandas import read_csv
from scipy.optimize import curve_fit
from math import log10, floor

def round_sig(x, sig=1):
    return round(x, sig-int(floor(log10(abs(x))))-1)

def get_data(file):
    file_data = read_csv(file)
    # Extract the raw data lists from the data dictionary, and take a slice of the area of iterest
    volt_data = file_data.get("Amplitude (V)").to_numpy()
    temp_data = file_data.get("Temperature (K)").to_numpy()
    # Generate points for the fitted curve
    label = re.findall(r'(\d{1,2}K_to_\d{1,2}K)', file)[0]
    return (temp_data, volt_data, f"Data: {label}")

data_371 = get_data("3.7.1_R&S_Metal_Insulator_5K_to_11K.csv")
data_372 = get_data("3.7.2_R&S_Metal_Insulator_11K_to_30K.csv")
data_375 = get_data("3.7.5_R&S_Metal_Insulator_30K_to_60K.csv")
data_LH = (data_371, data_372, data_375)
data_373 = get_data("3.7.3_R&S_Metal_Insulator_15K_to_5K.csv")
data_374 = get_data("3.7.4_R&S_Metal_Insulator_30K_to_15K.csv")
data_376 = get_data("3.7.6_R&S_Metal_Insulator_60K_to_30K.csv")
data_HL = (data_373, data_374, data_376)

markers = ["o", "x", "D"]
linestyles = ["dashed", "dashdot", "dotted"]
colours = [(0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75)]

fig, ax = plt.subplots()
for i, data in enumerate(data_LH):
    ax.plot(data[0], data[1], color=colours[i], linestyle=linestyles[0], label=data[2])
for i, data in enumerate(data_HL):
    ax.plot(data[0], data[1], color=colours[i], linestyle=linestyles[2], label=data[2])
ax.set_title("Voltage vs Temperature for a Metal to Insulator Transition")
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Voltage (V)")
ax.legend(loc="lower left")
fig.savefig("metal_insulator.png", dpi=300)

plt.show()
