import matplotlib.pyplot as plt
import re
from pandas import read_csv
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
    return ((temp_data, volt_data), f"Data: {label}")


def average(temp_data, volt_data, window_size=30):
    volt_result = []
    temp_result = []
    for i in range(len(volt_data)-window_size-1):
        volt_snippet = volt_data[i:i+window_size]
        temp_snippet = temp_data[i:i+window_size]
        volt_avg = sum(volt_snippet) / len(volt_snippet)
        temp_avg = sum(temp_snippet) / len(temp_snippet)
        volt_result.append(volt_avg)
        temp_result.append(temp_avg)
    return (temp_result, volt_result)

data_35 = get_data("3.5_Susceptometer_10K_to_7K.csv")
data_36 = get_data("3.6_Susceptometer_7K_to_9K.csv")
data_35 = (average(*data_35[0]), data_35[1])
data_runs = (data_35, data_36)

markers = ["o", "x", "D"]
linestyles = ["dashed", "dashdot", "dotted"]
colours = [(0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75)]

fig, ax = plt.subplots()
for i, data in enumerate(data_runs):
    ax.plot(*data[0], color=colours[i], label=data[1])
ax.set_title("Voltage vs Temperature { P=0.52, I=5.4, D=0 }")
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Amplitude (V)")
ax.legend(loc="lower right")
fig.savefig("metal_insulator.png", dpi=300)

plt.show()
