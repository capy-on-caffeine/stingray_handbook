import numpy as np
import matplotlib.pyplot as plt
# from stingray.modeling import Lorentz1D
from astropy.modeling import models

# Create Lorentz1D instance and set parameters
lorentz_profile = models.Lorentz1D()
lorentz_profile.amplitude = 1.0
lorentz_profile.x_0 = 10.0  # Peak position
lorentz_profile.fwhm = 2.0  # Full Width at Half Maximum

# Generate x values for plotting
x_values = np.linspace(5, 15, 1000)  # Adjust range and density as needed

# Evaluate Lorentzian profile at x_values
y_values = lorentz_profile.evaluate(x_values, 1.0, 10.0, 2.0)

# Plot the Lorentzian profile
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='Lorentzian Profile', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lorentzian Profile')
plt.grid(True)
plt.legend()
plt.show()