import numpy as np
from astropy.modeling import models
from stingray import Lightcurve, Crossspectrum
import stingray.spectroscopy as spec
import matplotlib.pyplot as plt

from stingray.utils import find_nearest

# dt = 0.01
# time = np.arange(0, 100, dt)
# qpo_freq = 0.1
# harmonic_freq = 2 * qpo_freq
# counts_qpo = 100 * np.sin(2 * np.pi * qpo_freq * time)
# counts_harmonic = 50 * np.sin(2 * np.pi * harmonic_freq * time)
# counts = counts_qpo + counts_harmonic
# lc = Lightcurve(time, counts, dt=dt)
# cs = Crossspectrum(lc, lc)

# qpo_phase = np.pi / 4
# harmonic_phase = np.pi / 4
# model = models.Lorentz1D(x_0=qpo_freq) + models.Lorentz1D(
#     x_0=harmonic_freq
# )

# cap_phi_1, cap_phi_2, small_psi = spec.get_phase_lag(cs, model)
# print(cap_phi_1)
# print(cap_phi_2)
# print(small_psi)

dt = 0.01
time = np.arange(0, 100, dt)
qpo_freq = 0.1
harmonic_freq = 2 * qpo_freq
counts_qpo = 100 * np.sin(2 * np.pi * qpo_freq * time)
counts_harmonic = 50 * np.sin(2 * np.pi * harmonic_freq * time)
counts = counts_qpo + counts_harmonic
lc = Lightcurve(time, counts, dt=dt)
cs = Crossspectrum(lc, lc)

qpo_phase = np.pi / 4
harmonic_phase = np.pi / 4
model = models.Lorentz1D(x_0=qpo_freq) + models.Lorentz1D(
    x_0=harmonic_freq
)

x_0_0 = qpo_freq
x_0_1 = harmonic_freq

_, idx_0 = find_nearest(cs.freq, x_0_0)
_, idx_1 = find_nearest(cs.freq, x_0_1)


print(x_0_0)
print(x_0_1)

C_E_1 = cs.power[idx_0]  # 1st harmonic
C_E_2 = cs.power[idx_1]  # 2nd harmonic

print(C_E_1)
print(C_E_2)

delta_E_1 = np.angle(C_E_1)
delta_E_2 = np.angle(C_E_2)

print(delta_E_1)
print(delta_E_2)

# cap_phi_1, cap_phi_2, small_psi = spec.get_phase_lag(cs, model)
# print(cap_phi_1)
# print(cap_phi_2)
# print(small_psi)