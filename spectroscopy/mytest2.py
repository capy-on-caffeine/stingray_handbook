import numpy as np
from astropy.modeling import models
from stingray import Lightcurve, Crossspectrum
import stingray.spectroscopy as spec  # Import your spectroscopy modu
import matplotlib.pyplot as plt

dt = 0.01
time = np.arange(0, 100, dt)
qpo_freq = 0.1  # QPO frequency
harmonic_freq = 2 * qpo_freq  # Frequency of the harmonic
counts_qpo = 100 * np.sin(2 * np.pi * qpo_freq * time)
# counts_qpo_shifted = 100 * np.sin(2 * np.pi * qpo_freq * time - np.pi / 2)
counts_harmonic = 50 * np.sin(2 * np.pi * harmonic_freq * time)
counts = counts_qpo + counts_harmonic

# plt.plot(time, counts, color='blue')
# plt.plot(time, counts_qpo, color='red')
# plt.plot(time, counts_qpo_shifted, color='black')
# plt.plot(time, counts_harmonic, color='green')
# plt.grid(True)
# plt.show()

lc = Lightcurve(time, counts, dt=dt)

# plt.plot(lc.time, lc.counts, color='red')
# plt.grid(True)
# plt.show()

cs = Crossspectrum(lc, lc)

plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(cs.freq, np.abs(cs.power), color='blue')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('Cross Spectrum Magnitude')

# Plot the phase of the cross spectrum
plt.subplot(2, 1, 2)
plt.plot(cs.freq, np.angle(cs.power), color='red')
plt.xlabel('Frequency')
plt.ylabel('Phase (radians)')
plt.title('Cross Spectrum Phase')

plt.tight_layout()
plt.show()

qpo_phase = np.pi / 4  # Known phase of the QPO
harmonic_phase = np.pi / 6  # Known phase of the harmonic
model = models.Lorentz1D(x_0=qpo_freq) + models.Lorentz1D(x_0=harmonic_freq)

# Calculate the mean phase difference
avg_psi, stddev = spec.get_mean_phase_difference(cs, model)

# Test against known phases
print(np.isclose(avg_psi, qpo_phase - harmonic_phase, atol=1e-5))  # Tolerance might need adjustment
print(np.isclose(stddev, 0.0, atol=1e-5))