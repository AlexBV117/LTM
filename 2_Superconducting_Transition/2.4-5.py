import numpy as np
import matplotlib.pyplot as plt
import re
from pandas import read_csv
from scipy.optimize import curve_fit
from math import log10, floor

def round_sig(x, sig=1):
    return round(x, sig-int(floor(log10(abs(x))))-1)

def sigmoid(x, a, b, c):
    return (a / (1 + np.exp(-b * (x + c))))

def inv_sigmoid(y, a, b, c):
    return ((-1/b) * np.log((a/y) - 1)) - c

def print_fit_perams(label, ps, pcov):
    print(f"{label}:")
    pname = ["a", "b", "c"]
    perr = np.sqrt(np.diag(pcov)) # one standard deviation errors
    for p, err, name in zip(ps, perr, pname):
        err = round_sig(err)
        dec = len(str(err))-2
        print(f"\t{name}: {p:1.{dec}f} ± {err}")

def get_data(file, section, current, init_vals, fit_func):
    file_data = read_csv(file)
    # Extract the raw data lists from the data dictionary, and take a slice of the area of iterest
    volt_data = file_data.get("Amplitude (V)").to_numpy()[section[0]:section[1]]
    temp_data = file_data.get("Temperature (K)").to_numpy()[section[0]:section[1]]
    # Convert the volateg value to a resistance
    resi_data = volt_data/current
    # Generate points for the fitted curve
    temp_fit, resi_fit, fit, fit_cov = get_fit(fit_func, temp_data, resi_data, init_vals) 
    # Pull out the temperature range from the file name
    label = re.findall(r'(\d.\dK_to_\d.\dK)', file)[0]
    print_fit_perams(label, fit, fit_cov)
    return ((temp_data, resi_data, f"Data: {label}"), (temp_fit, resi_fit, f"Fit: {label}"), fit)

def get_fit(func, x, y, perams):
    # Fit a sigmoid function to the raw data
    fit, fit_cov = curve_fit(func, x, y, p0=perams)
    # One data run if from low -> high temp and another is high -> low temp.
    # therefore the range will be inverted for one of the runs
    x1, x2 = x[0], x[-1]
    larger  = lambda x1, x2: x1 if x1 > x2 else (x2 if x2 > x1 else 0)
    smaller = lambda x1, x2: x1 if x1 < x2 else (x2 if x2 < x1 else 0)
    x_fit = np.arange(smaller(x1, x2), larger(x1,x2), 0.01)
    # generate the fitted curve data points
    y_fit = sigmoid(x_fit, *fit)
    return (x_fit, y_fit, fit, fit_cov)

def get_t_annotations(func, offset, a, b, c):
    result = []
    a_vals = [x * a for x in [0.1, 0.5, 0.9]]
    t_vals = func(a_vals, a, b, c).tolist()
    t_off, a_off, i = offset
    # just in case its not for some reason
    if len(a_vals) != len(t_vals):
        raise Exception(f"Length Issue:\na_vals = {a_vals}\nt_vals = {t_vals}")
    for t, a in zip(t_vals, a_vals):
        # Alternate between shifting the annotations left or right of the point
        r_l = (-1) ** i
        # Account for the length of the annotation
        # the left shited labels need moved over more.
        adjust = lambda r_l: 0.125 if r_l == 1 else 0
        xy_text = [t - (adjust(r_l) + (t_off * r_l)), a - (adjust(r_l) + (a_off * r_l))]
        label = f"({t:1.2f},{a:1.2f})"
        result.append(((t, a), label, xy_text))
    return result

data_20 = get_data("2.4_Ramp_8.4K_to_8.9K_5V.csv", (0, 244), 4.8e-3, [3.762, 36, -8.7], sigmoid)
data_21 = get_data("2.5_Ramp_8.9K_to_8.4K_5V.csv", (0, 244), 4.8e-3, [3.76, 36, -8.65], sigmoid)
data_runs = (data_20, data_21)

markers = ["o", "x", "D"]
linestyles = ["dashed", "dashdot", "dotted"]

fig, ax = plt.subplots()
for i, run in enumerate(data_runs):
    ax.plot(run[1][0], run[1][1], color=(0.5, 0.5, 0.5), linestyle=linestyles[i], label=run[1][2])
    ax.scatter(run[0][0], run[0][1], color=(0, 0, 0), marker=markers[i], label=run[0][2])
    t = get_t_annotations(inv_sigmoid, (0.05, 0, i), *run[2]) # Get the annotations for the graph
    for point in t:
        ax.scatter(*point[0], color=(0.75, 0.75, 0.75), marker="D")
        ax.annotate(point[1], xy=point[0], xycoords='data', xytext=point[2], arrowprops=dict(arrowstyle="->"))
ax.set_title("Resistance vs Temperature { P=0.8, I=5.46, D=0 }")
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Resistance (Ω)")
ax.legend(loc="lower right")
fig.savefig("2.4-5.png", dpi=300)

plt.show()
