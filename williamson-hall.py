import math
import pandas as pd
import matplotlib.pyplot as plt

def williamson_hall(FWHM, theta_degrees):
    theta_rad = [math.radians(deg / 2) for deg in theta_degrees]  # Convert theta/2 to radians
    fwhm_rad = [math.radians(fwhm) for fwhm in FWHM]  # Convert FWHM to radians
    
    bcos_theta = [fwhm * math.cos(theta) for fwhm, theta in zip(fwhm_rad, theta_rad)]
    foursin_theta = [4 * math.sin(theta) for theta in theta_rad]
    
    data = {
        "FWHM": FWHM,
        "Theta (degrees)": theta_degrees,
        "Bcos(Theta)": bcos_theta,
        "4sin(Theta)": foursin_theta
    }
    df = pd.DataFrame(data)
    
    # Plotting Williamson-Hall plot
    plt.figure(figsize=(8, 6))
    plt.scatter(foursin_theta, bcos_theta, color='blue', label='Data points')
    plt.xlabel("4sin(Theta)")
    plt.ylabel("Bcos(Theta)")
    plt.title("Williamson-Hall Plot")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()
    
    return df

#Example usage
FWHM = [0.153455,
0.152002,
0.162407,
0.202929,
0.185814,
0.202766,
0.274127,
0.369451,
0.18587,
0.254347,
0.3351]
theta_degrees =[24.3727,
28.1258,
31.5754,
33.1965,
42.728,
44.0103,
47.6106,
54.1837,
55.0752,
56.1,
58.1961]
wavelength = 1.541  # nanometers

# Calculate microstrain and crystallite size
williamson_hall(FWHM, theta_degrees)