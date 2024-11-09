import matplotlib.pyplot as plt
from pandas import read_csv

def get_data(file, start, stop):
    file_data = read_csv(file)
    ampl_data = file_data.get("Amplitude (V)").to_numpy()[start:stop]
    temp_data = file_data.get("Temperature (K)").to_numpy()[start:stop]
    return (temp_data, (ampl_data/9.5e-4))

data_20 = get_data("2.0_Ramp_7k_to_12K.csv", 70, 83)
data_21 = get_data("2.1_Ramp_12k_to_7K.csv", 143, 158)

fig, ax = plt.subplots()
ax.plot(*data_20, color='r', label="07K to 12K")
ax.plot(*data_21, color='b', label="12K to 07K")
ax.set_title("Resistance vs Temperature { P=0.8, I=5.46, D=0 }")
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Resistance (Ω)")
ax.legend(loc="upper right")
fig.savefig("Run1.png", dpi=300)

plt.show()
