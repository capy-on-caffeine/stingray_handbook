import numpy as np
from astropy.modeling import models
from stingray import Lightcurve, Crossspectrum
import stingray.spectroscopy as spec
import matplotlib.pyplot as plt

dt = 0.01
time = np.arange(0, 100, dt)
qpo_freq = 0.1
harmonic_freq = 2 * qpo_freq
counts_qpo = 100 * np.sin(2 * np.pi * qpo_freq * time - np.pi / 4)
counts_harmonic = 50 * np.sin(2 * np.pi * harmonic_freq * time - np.pi / 4)
counts = counts_qpo + counts_harmonic

# plt.grid(True)
# plt.plot(time, counts, color='black')
# plt.plot(time, counts_qpo, color='red')
# plt.plot(time, counts_harmonic, color='green')

lc = Lightcurve(time, counts, dt=dt)
cs = Crossspectrum(lc, lc)

model = models.Lorentz1D(x_0=qpo_freq, amplitude=100) + models.Lorentz1D(x_0=harmonic_freq, amplitude=50)
avg_psi, stddev = spec.get_mean_phase_difference(cs, model)

# Plotting the QPO component
# mqpo = models.Lorentz1D(x_0=qpo_freq, amplitude=100)
# qpo_eval = mqpo.evaluate(time, x_0=qpo_freq, amplitude=100, fwhm=2.0)
# mh = models.Lorentz1D(x_0=harmonic_freq, amplitude=50)
# h_eval = mh.evaluate(time, x_0=harmonic_freq, amplitude=50, fwhm=2.0)
# avg_psi, stddev = spec.get_mean_phase_difference(cs, mqpo)
# plt.plot(time, qpo_eval + h_eval, color='blue')

# plt.show()

print(avg_psi)
print(stddev)
