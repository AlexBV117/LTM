import numpy as np
import matplotlib.pyplot as plt
import re
from pandas import read_csv
from scipy.optimize import curve_fit
from math import log10, floor

def round_sig(x, sig=1):
    return round(x, sig-int(floor(log10(abs(x))))-1)

markers = ["o", "x", "D"]
linestyles = ["dashed", "dashdot", "dotted"]

def get_data(file, has_volt=False):
    file_data = read_csv(file)
    # Extract the raw data lists from the data dictionary, and take a slice of the area of iterest
    time_data = file_data.get("Time (s)").to_numpy()
    temp_data = file_data.get("Temperature (K)").to_numpy()
    if has_volt:
        volt_data = file_data.get("Amplitude (V)").to_numpy()
        return ((time_data, temp_data), (time_data, volt_data))
    else:
        return (time_data, temp_data)

data_30 = get_data("3.0_Good_Control_50K.csv")

fig1, ax1 = plt.subplots()
fig1.suptitle("3.0_Good_Control_50K.csv")
ax1.plot(*data_30, color='k')
ax1.set_title("Temperature vs Time { P=55, I=0, D=0 }")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Temperature (K)")
fig1.savefig("Raw1.png", dpi=300)

data_31 = get_data("3.1_Good_Control_50K_Final.csv")

fig2, ax2 = plt.subplots()
fig2.suptitle("3.1_Good_Control_50K_Final.csv")
ax2.plot(*data_31, color='k')
ax2.set_title("Temperature vs Time { P=22, I=8.464, D=0 }")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Temperature (K)")
fig2.savefig("Raw2.png", dpi=300)

data_32 = get_data("3.2_Metal_Insulator_40K_to_60K.csv", has_volt=True)

fig3, ax3 = plt.subplots(2)
fig3.suptitle("3.2_Metal_Insulator_40K_to_60K.csv")
ax3[0].plot(*data_32[0], color='k')
ax3[0].set_title("Temperature vs Time { P=22, I=8.464, D=0 }")
ax3[0].set_xlabel("Time (s)")
ax3[0].set_ylabel("Temperature (K)")
ax3[1].plot(*data_32[1], color='k')
ax3[1].set_title("Voltage vs Time { P=22, I=8.464, D=0 }")
ax3[1].set_xlabel("Time (s)")
ax3[1].set_ylabel("Amplitude (V)")
plt.tight_layout()
fig3.savefig("Raw3.png", dpi=300)

data_33 = get_data("3.3_Metal_Insulator_60K_to_40K.csv", has_volt=True)

fig4, ax4 = plt.subplots(2)
fig4.suptitle("3.3_Metal_Insulator_60K_to_40K.csv")
ax4[0].plot(*data_33[0], color='k')
ax4[0].set_title("Temperature vs Time { P=22, I=8.464, D=0 }")
ax4[0].set_xlabel("Time (s)")
ax4[0].set_ylabel("Temperature (K)")
ax4[1].plot(*data_33[1], color='k')
ax4[1].set_title("Voltage vs Time { P=22, I=8.464, D=0 }")
ax4[1].set_xlabel("Time (s)")
ax4[1].set_ylabel("Amplitude (V)")
plt.tight_layout()
fig4.savefig("Raw4.png", dpi=300)


data_34 = get_data("3.4_Susceptometer_Is_R.csv", has_volt=True)

fig5, ax5 = plt.subplots(2)
fig5.suptitle("3.4_Susceptometer_Is_R.csv")
ax5[0].plot(*data_34[0], color='k')
ax5[0].set_title("Temperature vs Time { P=0.52, I=5.4, D=0 }")
ax5[0].set_xlabel("Time (s)")
ax5[0].set_ylabel("Temperature (K)")
ax5[1].plot(*data_34[1], color='k')
ax5[1].set_title("Voltage vs Time { P=0.52, I=5.4, D=0 }")
ax5[1].set_xlabel("Time (s)")
ax5[1].set_ylabel("Amplitude (V)")
plt.tight_layout()
fig5.savefig("Raw5.png", dpi=300)

data_35 = get_data("3.5_Susceptometer_10k_to_7K.csv", has_volt=True)

fig6, ax6 = plt.subplots(2)
fig6.suptitle("3.5_Susceptometer_10k_to_7K.csv")
ax6[0].plot(*data_35[0], color='k')
ax6[0].set_title("Temperature vs Time { P=22, I=8.464, D=0 }")
ax6[0].set_xlabel("Time (s)")
ax6[0].set_ylabel("Temperature (K)")
ax6[1].plot(*data_35[1], color='k')
ax6[1].set_title("Voltage vs Time { P=22, I=8.464, D=0 }")
ax6[1].set_xlabel("Time (s)")
ax6[1].set_ylabel("Amplitude (V)")
plt.tight_layout()
fig6.savefig("Raw6.png", dpi=300)

data_36 = get_data("3.6_Susceptometer_7k_to_9K.csv", has_volt=True)

fig7, ax7 = plt.subplots(2)
fig7.suptitle("3.3_Metal_Insulator_60K_to_40K.csv")
ax7[0].plot(*data_36[0], color='k')
ax7[0].set_title("Temperature vs Time { P=22, I=8.464, D=0 }")
ax7[0].set_xlabel("Time (s)")
ax7[0].set_ylabel("Temperature (K)")
ax7[1].plot(*data_36[1], color='k')
ax7[1].set_title("Voltage vs Time { P=22, I=8.464, D=0 }")
ax7[1].set_xlabel("Time (s)")
ax7[1].set_ylabel("Amplitude (V)")
plt.tight_layout()
fig7.savefig("Raw7.png", dpi=300)

plt.show()
