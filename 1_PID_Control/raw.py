import matplotlib.pyplot as plt
from pandas import read_csv

def get_data(file: str):
    file_data = read_csv(file)
    time_data = file_data.get("Time (s)").to_numpy()
    temp_data = file_data.get("Temperature (K)").to_numpy()
    return (time_data, temp_data)

data_10 = get_data("1.0_P_Oscillations_Data.csv")
data_11 = get_data("1.1_Good_Control_1.0_P.csv")
data_12 = get_data("1.2_Good_Control_0.5_P.csv")
data_13 = get_data("1.3_Good_Control_2.0_P.csv")
data_14 = get_data("1.4_Good_Control_1.5_P.csv")
data_15 = get_data("1.5_Good_Control_0.5_I.csv")
data_16 = get_data("1.6_Good_Control_2.0_I.csv")

fig1, ax1 = plt.subplots()
ax1.plot(*data_10, color='k', label="Raw Data")
fig1.suptitle("Tempterature Oscillations { P=2, I=0, D=0 }")
ax1.set_title("1.0_P_Oscillations_Data.csv")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Temperature (K)")
ax1.legend(loc="upper right")
fig1.savefig("Raw_1.png", dpi=300)

data_P = (
    (data_11, "1.1_Good_Control_1.0_P.csv", "Raw Data: 1.0 * P"),
    (data_12, "1.2_Good_Control_0.5_P.csv", "Raw Data: 0.5 * P"),
    (data_13, "1.3_Good_Control_2.0_P.csv", "Raw Data: 2.0 * P"),
    (data_14, "1.4_Good_Control_1.5_P.csv", "Raw Data: 1.5 * P"),
)
fig2, axes2 = plt.subplots(2, 2, figsize=(10.53, 7.47))
axes2 = (*axes2[0], *axes2[1])
fig2.suptitle("Tempterature Oscillations { P=0.8, I=5.46, D=0 }")
for i, axes in enumerate(axes2):
    data, title, label = data_P[i]
    axes.plot(*data, color='k', label=label)
    axes.set_title(title)
    axes.set_xlabel("Time (s)")
    axes.set_ylabel("Temperature (K)")
    axes.legend(loc="lower right")
plt.tight_layout()
fig2.savefig("Raw_2.png", dpi=300)


data_I = (
    (data_15, "1.5_Good_Control_0.5_I.csv", "Raw Data: 0.5 * I"),
    (data_16, "1.6_Good_Control_2.0_I.csv", "Raw Data: 2.0 * I"),
)
fig3, axes3 = plt.subplots(2)
fig3.suptitle("Tempterature Oscillations { P=0.4, I=5.46, D=0 }")
for i, axes in enumerate(axes3):
    data, title, label = data_I[i]
    axes.plot(*data, color='k', label=label)
    axes.set_title(title)
    axes.set_xlabel("Time (s)")
    axes.set_ylabel("Temperature (K)")
    axes.legend(loc="lower right")
plt.tight_layout()
fig3.savefig("Raw_3.png", dpi=300)


plt.show()
