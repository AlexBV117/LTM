import matplotlib.pyplot as plt
from pandas import read_csv

def get_data(file):
    file_data = read_csv(file)
    ampl_data = file_data.get("Amplitude (V)").to_numpy()
    temp_data = file_data.get("Temperature (K)").to_numpy()
    time_data = file_data.get("Time (s)").to_numpy()
    return (time_data, temp_data), (time_data, ampl_data)

temp_20, volt_20 = get_data("2.0_Ramp_7K_to_12K.csv")
temp_21, volt_21 = get_data("2.1_Ramp_12K_to_7K.csv")
temp_22, volt_22 = get_data("2.2_Ramp_8.9K_to_8.4K.csv")
temp_23, volt_23 = get_data("2.3_Ramp_8.4K_to_8.9K.csv")
temp_24, volt_24 = get_data("2.4_Ramp_8.4K_to_8.9K_5V.csv")
temp_25, volt_25 = get_data("2.5_Ramp_8.9K_to_8.4K_5V.csv")
temp_26, volt_26 = get_data("2.6_Last_Chance.csv")


data_1 = (
    (temp_20, "Temperature vs Time { P=0.8, I=5.46, D=0 }", "Temperature (K)"),
    (volt_20, "Voltage vs Time { P=0.8, I=5.46, D=0 }", "Amplitude (V)")
)
fig1, axes1 = plt.subplots(2)
fig1.suptitle("2.0_Ramp_7k_to_12K.csv")
for i, axes in enumerate(axes1):
    axes.plot(*data_1[i][0], color='k')
    axes.set_title(data_1[i][1])
    axes.set_xlabel("Time (s)")
    axes.set_ylabel(data_1[i][2])
plt.tight_layout()
fig1.savefig("Raw1.png", dpi=300)

data_2 = (
    (temp_21, "Temperature vs Time { P=0.8, I=5.46, D=0 }", "Temperature (K)"),
    (volt_21, "Voltage vs Time { P=0.8, I=5.46, D=0 }", "Amplitude (V)")
)
fig2, axes2 = plt.subplots(2)
fig2.suptitle("2.1_Ramp_12k_to_7K.csv")
for i, axes in enumerate(axes2):
    axes.plot(*data_2[i][0], color='k')
    axes.set_title(data_2[i][1])
    axes.set_xlabel("Time (s)")
    axes.set_ylabel(data_2[i][2])
plt.tight_layout()
fig2.savefig("Raw2.png", dpi=300)

data_3 = (
    (temp_22, "Temperature vs Time { P=0.8, I=5.46, D=0 }", "Temperature (K)"),
    (volt_22, "Voltage vs Time { P=0.8, I=5.46, D=0 }", "Amplitude (V)")
)
fig3, axes3 = plt.subplots(2)
fig3.suptitle("2.2_Ramp_8.9K_to_8.4K.csv")
for i, axes in enumerate(axes3):
    axes.plot(*data_3[i][0], color='k')
    axes.set_title(data_3[i][1])
    axes.set_xlabel("Time (s)")
    axes.set_ylabel(data_3[i][2])
plt.tight_layout()
fig3.savefig("Raw3.png", dpi=300)

data_4 = (
    (temp_23, "Temperature vs Time { P=0.8, I=5.46, D=0 }", "Temperature (K)"),
    (volt_23, "Voltage vs Time { P=0.8, I=5.46, D=0 }", "Amplitude (V)")
)
fig4, axes4 = plt.subplots(2)
fig4.suptitle("2.3_Ramp_8.4K_to_8.9K.csv")
for i, axes in enumerate(axes4):
    axes.plot(*data_4[i][0], color='k')
    axes.set_title(data_4[i][1])
    axes.set_xlabel("Time (s)")
    axes.set_ylabel(data_4[i][2])
plt.tight_layout()
fig4.savefig("Raw4.png", dpi=300)

data_5 = (
    (temp_24, "Temperature vs Time { P=0.8, I=5.46, D=0 }", "Temperature (K)"),
    (volt_24, "Voltage vs Time { P=0.8, I=5.46, D=0 }", "Amplitude (V)")
)
fig5, axes5 = plt.subplots(2)
fig5.suptitle("2.4_Ramp_8.4K_to_8.9K_5V.csv")
for i, axes in enumerate(axes5):
    axes.plot(*data_5[i][0], color='k')
    axes.set_title(data_5[i][1])
    axes.set_xlabel("Time (s)")
    axes.set_ylabel(data_5[i][2])
plt.tight_layout()
fig5.savefig("Raw5.png", dpi=300)

data_6 = (
    (temp_25, "Temperature vs Time { P=0.8, I=5.46, D=0 }", "Temperature (K)"),
    (volt_25, "Voltage vs Time { P=0.8, I=5.46, D=0 }", "Amplitude (V)")
)
fig6, axes6 = plt.subplots(2)
fig6.suptitle("2.5_Ramp_8.9K_to_8.4K_5V.csv")
for i, axes in enumerate(axes6):
    axes.plot(*data_6[i][0], color='k')
    axes.set_title(data_6[i][1])
    axes.set_xlabel("Time (s)")
    axes.set_ylabel(data_6[i][2])
plt.tight_layout()
fig6.savefig("Raw6.png", dpi=300)

data_7 = (
    (temp_26, "Temperature vs Time { P=0.8, I=5.46, D=0 }", "Temperature (K)"),
    (volt_26, "Voltage vs Time { P=0.8, I=5.46, D=0 }", "Amplitude (V)")
)
fig7, axes7 = plt.subplots(2)
fig7.suptitle("2.6_Last_Chance.csv")
for i, axes in enumerate(axes7):
    axes.plot(*data_7[i][0], color='k')
    axes.set_title(data_7[i][1])
    axes.set_xlabel("Time (s)")
    axes.set_ylabel(data_7[i][2])
plt.tight_layout()
fig7.savefig("Raw7.png", dpi=300)

plt.show()
