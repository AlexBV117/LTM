import matplotlib.pyplot as plt
from pandas import read_csv

def get_data(file):
    file_data = read_csv(file)
    ampl_data = file_data.get("Amplitude (V)").to_numpy()
    temp_data = file_data.get("Temperature (K)").to_numpy()
    return (temp_data, ampl_data)

data_20 = get_data("2.0_Ramp_7k_to_12K.csv")
data_21 = get_data("2.1_Ramp_12k_to_7K.csv")
data_22 = get_data("2.2_Ramp_8.9K_to_8.4K.csv")
data_23 = get_data("2.3_Ramp_8.4K_to_8.9K.csv")
data_24 = get_data("2.4_Ramp_8.4K_to_8.9K_5V.csv")
data_25 = get_data("2.5_Ramp_8.9K_to_8.4K_5V.csv")
data_26 = get_data("2.6_Last_Chance.csv")

data_1 = (
    (data_20, "2.0_Ramp_7k_to_12K.csv", "Fast Ramp: 7k → 12K @1V"),
    (data_21, "2.1_Ramp_12k_to_7K.csv", "Fast Ramp: 12k → 7K @1V")
)
fig1, axes1 = plt.subplots(2)
fig1.suptitle("Voltage vs Temperature { P=0.8, I=5.46, D=0 }")
for i, axes in enumerate(axes1):
    axes.plot(*data_1[i][0], color='k', label=f"{data_1[i][2]}")
    axes.set_title(data_1[i][1])
    axes.set_xlabel("Temperature (K)")
    axes.set_ylabel("Amplitude (V)")
    axes.legend(loc="lower right")
plt.tight_layout()
fig1.savefig("Raw1.png", dpi=300)

data_2 = (
    (data_22, "2.2_Ramp_8.9k_to_8.4K.csv", "Slow Ramp: 8.9k → 8.4K @1V"),
    (data_23, "2.3_Ramp_8.4k_to_8.9K.csv", "Slow Ramp: 8.4k → 8.9K @1V")
)
fig2, axes2 = plt.subplots(2)
fig2.suptitle("Voltage vs Temperature { P=0.8, I=5.46, D=0 }")
for i, axes in enumerate(axes2):
    axes.plot(*data_2[i][0], color='k', label=f"{data_2[i][2]}")
    axes.set_title(data_2[i][1])
    axes.set_xlabel("Temperature (K)")
    axes.set_ylabel("Amplitude (V)")
    axes.legend(loc="lower right")
plt.tight_layout()
fig2.savefig("Raw2.png", dpi=300)

data_3 = (
    (data_24, "2.4_Ramp_8.4k_to_8.9K_5V.csv", "Slow Ramp: 8.4k → 8.9K @5V"),
    (data_25, "2.5_Ramp_8.9k_to_8.4K_5V.csv", "Slow Ramp: 8.9k → 8.4K @5V")
)
fig3, axes3 = plt.subplots(2)
fig3.suptitle("Voltage vs Temperature { P=0.8, I=5.46, D=0 }")
for i, axes in enumerate(axes3):
    axes.plot(*data_3[i][0], color='k', label=f"{data_3[i][2]}")
    axes.set_title(data_3[i][1])
    axes.set_xlabel("Temperature (K)")
    axes.set_ylabel("Amplitude (V)")
    axes.legend(loc="lower right")
plt.tight_layout()
fig3.savefig("Raw3.png", dpi=300)

fig4, axes4 = plt.subplots()
fig4.suptitle("Voltage vs Temperature { P=0.8, I=5.46, D=0 }")
axes4.plot(*data_26, color='k', label="Slow Ramp: 8.4K → 11.2K @5V")
axes4.set_title("2.6_Last_Chance.csv")
axes4.set_xlabel("Temperature (K)")
axes4.set_ylabel("Amplitude (V)")
axes4.legend(loc="lower right")
plt.tight_layout()
fig4.savefig("Raw5.png", dpi=300)

plt.show()
