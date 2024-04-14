import stingray.spectroscopy as spec
import matplotlib.pyplot as plt
import numpy as np
from astropy.modeling import models
from stingray import Lightcurve, Crossspectrum

dt = 0.01
time = np.arange(0, 100, dt)

qpo_freq = 0.1
harmonic_freq = 2 * qpo_freq

counts_qpo = 100 * np.sin(2 * np.pi * qpo_freq * time - np.pi / 4)
counts_qpo_test = 100 * np.sin(2 * np.pi * qpo_freq * time ) # remove this shit blah blah blah
counts_harmonic = 50 * np.sin(2 * np.pi * harmonic_freq * time - np.pi / 4)
counts = counts_qpo + counts_harmonic

lc = Lightcurve(time, counts, dt=dt)
cs = Crossspectrum(lc, lc)

model = models.Lorentz1D(x_0=qpo_freq, amplitude=100) + models.Lorentz1D(
    x_0=harmonic_freq, amplitude=50
)

# model_new = models.Lorentz1D(x_0=counts_qpo_test, amplitude=100)
# ev = model_new.evaluate(time, x_0=counts_qpo_test, amplitude=100, fwhm=2.0)

model_new = models.Lorentz1D(x_0=3*np.pi/4)
ev = model_new.evaluate(time,x_0=3*np.pi/4,amplitude=100,fwhm=2.0)

plt.grid(True)
plt.plot(time,ev,color='blue')
# plt.plot(time,counts_qpo,color='red')
plt.plot(time,counts_qpo_test,color='black')
plt.show()

# avg_psi, stddev = spec.get_mean_phase_difference(cs, model)