import numpy as np
import matplotlib.pyplot as plt
import re
from pandas import read_csv
from scipy.optimize import curve_fit
from math import log10, floor

def round_sig(x, sig=1):
    return round(x, sig-int(floor(log10(abs(x))))-1)

def linear(x, m, c):
    return ((m * x) + c)

def get_data(file, fit_func):
    file_data = read_csv(file)
    # Extract the raw data lists from the data dictionary, and take a slice of the area of iterest
    keithley_volt_data = file_data.get("Keithley Voltage (V)").to_numpy()
    multimet_volt_data = file_data.get("Multimeter Voltage (mV)").to_numpy() * 1e-3
    curr_data = np.log(file_data.get("Multimeter Current (μA)").to_numpy() * 1e-6)
    volt_data = keithley_volt_data - multimet_volt_data
    # Generate points for the fitted curve
    volt_fit, curr_fit, fit, fit_cov = get_fit(fit_func, volt_data, curr_data)
    label = re.findall(r'(\d{2,3}K)', file)[0]
    print_fit_perams(label, fit, fit_cov)
    return ((volt_data, curr_data, f"Data: {label}"), (volt_fit, curr_fit, f"Fit: {label}"), (fit, fit_cov))

def get_fit(func, x, y):
    # Fit a sigmoid function to the raw data
    fit, fit_cov = curve_fit(func, x[:-1], y[:-1])
    x_fit = np.linspace(x[0], x[-1], 100)
    # generate the fitted curve data points
    y_fit = func(x_fit, *fit)
    return (x_fit, y_fit, fit, fit_cov)


def print_fit_perams(label, ps, pcov):
    print(f"{label}:")
    pname = ["m", "c"]
    perr = np.sqrt(np.diag(pcov)) # one standard deviation errors
    for p, err, name in zip(ps, perr, pname):
        err = round_sig(err)
        dec = len(str(err))-2
        print(f"\t{name}: {p:1.{dec}f} ± {err}")

def get_voltage_temp(data_runs, label,current):
    volts = []
    temps = (50, 100, 150, 200, 250, 295)
    for data in data_runs:
        volts.append(data[0][0][current])
    x_fit, y_fit, fit, fit_cov = get_fit(linear, temps, volts)
    print_fit_perams(label, fit, fit_cov)
    return ((temps, volts, f"Data: {label}"), (x_fit, y_fit, f"Fit: {label}"), (fit, fit_cov))


data_40 = get_data("4.0_295K.csv", linear)
data_41 = get_data("4.1_50K.csv" , linear)
data_42 = get_data("4.2_100K.csv", linear)
data_43 = get_data("4.3_150K.csv", linear)
data_44 = get_data("4.4_200K.csv", linear)
data_45 = get_data("4.5_250K.csv", linear)

data_runs = (data_41, data_42, data_43, data_44, data_45, data_40)

markers = ["o", "x", "D", "^", "<", ">"]
colours = [(0.25, 0.25, 0.25), (0.35, 0.35, 0.35), (0.45, 0.45, 0.45), (0.55, 0.55, 0.55), (0.65, 0.65, 0.65), (0.75, 0.75, 0.75)]

fig, ax = plt.subplots()
for i, run in enumerate(data_runs):
    ax.plot(run[1][0], run[1][1], color=colours[i], label=run[1][2])
    ax.scatter(run[0][0], run[0][1], color=(0, 0, 0), marker=markers[i], label=run[0][2])
ax.set_title("Current vs Voltage Over a Temperature Range 50K -> 295K")
ax.set_xlabel("Voltage (V)")
ax.set_ylabel("Natural log of Current (ln(A))")
ax.legend(loc="upper left")
fig.savefig("I-V.png", dpi=300)

data_1 = get_voltage_temp(data_runs, "5μA",0)
data_2 = get_voltage_temp(data_runs, "10μA",1)

data_runs = (data_1, data_2)

fig2, ax2 = plt.subplots()
for i, run in enumerate(data_runs):
    ax2.plot(run[1][0], run[1][1], color=colours[i], label=run[1][2])
    ax2.scatter(run[0][0], run[0][1], color=(0, 0, 0), marker=markers[i], label=run[0][2])
ax2.set_title("Current vs Voltage Over a Temperature Range 50K -> 295K")
ax2.set_xlabel("Voltage (V)")
ax2.set_ylabel("Natural log of Current (ln(A))")
ax2.legend(loc="upper right")
fig2.savefig("V-T.png", dpi=300)

plt.show()

