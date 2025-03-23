import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("collisions_data.csv")

# Log scale for better visualization
df["log_mass_ratio"] = np.log10(df["Mass Ratio"])

# Plot the results
plt.figure(figsize=(8, 5))
plt.scatter(df["log_mass_ratio"], df["Collision Count"], color='blue', label="Collisions")
plt.xlabel("Log(Mass Ratio)")
plt.ylabel("Collision Count")
plt.title("Collision Count vs Mass Ratio")
plt.legend()
plt.grid(True)
plt.show()
