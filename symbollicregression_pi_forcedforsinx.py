import numpy as np
import sympy as sp
from gplearn.genetic import SymbolicRegressor
from sklearn.metrics import mean_squared_error

# Define dataset
def generate_data(n_samples=100):
    X = np.linspace(0, 10, n_samples).reshape(-1, 1)
    y = np.sin(np.pi * X).flatten()  # Ensure pi is a key part of the equation
    return X, y

X, y = generate_data()

# Define custom function set
function_set = ['add', 'sub', 'mul', 'div', 'sin', 'cos', 'tan', 'log']
constants = [np.pi]  # Explicitly adding pi as a constant

# Define and train Symbolic Regressor
est = SymbolicRegressor(
    function_set=function_set,
    const_range=(np.pi, np.pi),  # Force usage of pi
    generations=50,
    population_size=1000,
    parsimony_coefficient=0.01,
    metric='mean absolute error',
    random_state=42,
    verbose=1
)

est.fit(X, y)

def discovered_equation():
    expr = est._program
    return expr

# Print discovered equation
print("Discovered Equation with π:", discovered_equation())

# Evaluate the model
predictions = est.predict(X)
mse = mean_squared_error(y, predictions)
print("Mean Squared Error:", mse)

# Plot results
import matplotlib.pyplot as plt
plt.scatter(X, y, label='Actual Data', color='blue')
plt.plot(X, predictions, label='Model Prediction', color='red')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Symbolic Regression Model Fit')
plt.show()
