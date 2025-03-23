import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from gplearn.genetic import SymbolicRegressor
from sklearn.preprocessing import StandardScaler

# Load dataset
file_path = "collisions_data.csv"
df = pd.read_csv(file_path)

# Extract values
mass_ratios = df["Mass Ratio"].values.reshape(-1, 1)
collision_counts = df["Collision Count"].values

# Convert mass ratios to log scale for better pattern detection
log_mass_ratios = np.log10(mass_ratios)

# Visualize the dataset
plt.figure(figsize=(8, 5))
plt.scatter(log_mass_ratios, collision_counts, color='blue', label="Data Points")
plt.xlabel("Log(Mass Ratio)")
plt.ylabel("Collision Count")
plt.title("Collision Count vs Log(Mass Ratio)")
plt.legend()
plt.grid(True)
plt.show()

# Scale log mass ratios
scaler = StandardScaler()
log_mass_ratios_scaled = scaler.fit_transform(log_mass_ratios.reshape(-1, 1))

# Symbolic Regression Model with refined constraints
sr = SymbolicRegressor(
    function_set=['add', 'sub', 'mul', 'div', 'sin', 'cos'],
    generations=100,  # More iterations for better convergence
    population_size=3000,  # Larger population for more diverse solutions
    stopping_criteria=0.001,  # Lower stopping criteria for more accuracy
    const_range=(3.1, 3.2),  # Biasing towards detecting π
    p_crossover=0.7,
    p_subtree_mutation=0.1,
    p_hoist_mutation=0.05,
    p_point_mutation=0.1,
    parsimony_coefficient=0.01,  # Penalizing overly complex equations
    verbose=1,
    random_state=42
)

# Fit model to data
sr.fit(log_mass_ratios_scaled, collision_counts)

# Get discovered equation
discovered_equation = sr._program
discovered_equation
