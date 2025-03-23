import csv
import math
import pandas as pd
import matplotlib.pyplot as plt

def relativistic_collision_count(m1, m2, u1, u2, c=1):
    def mulASR(vec, m1, m2, c):
        u1, u2 = vec
        Z = math.sqrt((1 - ((u1/c)**2)) * (1 - ((u2/c)**2)))

        a1N = (2*m1*m2*(c**2)*u2*Z) + (2*(m2**2)*(c**2)*u2) - (((m1**2) + (m2**2))*u1*(u2**2)) + (((m1**2) - (m2**2))*u1*(c**2)) 
        a2N = (2*m1*m2*(c**2)*u1*Z) + (2*(m1**2)*(c**2)*u1) - (((m1**2) + (m2**2))*u2*(u1**2)) + (((m2**2) - (m1**2))*u2*(c**2))
        a1D = (2*m1*m2*(c**2)*Z) - (2*(m2**2)*(u1)*u2) - (((m1**2) - (m2**2))*(u2**2)) + (((m1**2) + (m2**2))*(c**2)) 
        a2D = (2*m1*m2*(c**2)*Z) - (2*(m1**2)*(u1)*u2) - (((m2**2) - (m1**2))*(u1**2)) + (((m1**2) + (m2**2))*(c**2)) 

        v1 = a1N / float(a1D)
        v2 = a2N / float(a2D)
        return [v1, v2]

    def mulW(vec):
        return [-vec[0], vec[1]]

    def checkspeeds(speed1, speed2):
        return not (speed1 <= 0 and speed2 <= 0 and abs(speed2) >= abs(speed1))

    currentvector = [u1, u2]
    collisioncount = 0
    mtype = 'A'

    while checkspeeds(*currentvector):
        if mtype == 'A':
            currentvector = mulASR(currentvector, m1, m2, c)
            mtype = 'W'
        else:
            currentvector = mulW(currentvector)
            mtype = 'A'
        collisioncount += 1

    return collisioncount

def classical_collision_count(m1, m2, u1, u2):
    currentvector = [u1, u2]
    collisioncount = 0
    mtype = 'A'

    def classical_collision(vec, m1, m2):
        u1, u2 = vec
        v1 = ((m1 - m2) * u1 + 2 * m2 * u2) / (m1 + m2)
        v2 = ((m2 - m1) * u2 + 2 * m1 * u1) / (m1 + m2)
        return [v1, v2]

    def mulW(vec):
        return [-vec[0], vec[1]]

    while currentvector[0] > 0:
        if mtype == 'A':
            currentvector = classical_collision(currentvector, m1, m2)
            mtype = 'W'
        else:
            currentvector = mulW(currentvector)
            mtype = 'A'
        collisioncount += 1
    
    return collisioncount

# Generate data and save to CSV
mass_ratios = [10**i for i in range(10)]
base_mass = 1
init_velocity = [0, 0.1]

with open("relativistic_vs_classical_collision_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["log_mass_ratio", "relativistic_collisions", "classical_collisions"])
    
    for ratio in mass_ratios:
        m2 = base_mass * ratio
        rel_collisions = relativistic_collision_count(base_mass, m2, *init_velocity)
        clas_collisions = classical_collision_count(base_mass, m2, *init_velocity)
        writer.writerow([math.log10(ratio), rel_collisions, clas_collisions])
        print(f"Mass Ratio: {ratio}, Relativistic Collisions: {rel_collisions}, Classical Collisions: {clas_collisions}")

print("Data saved to relativistic_vs_classical_collision_data.csv")

# Load and visualize data
df = pd.read_csv("relativistic_vs_classical_collision_data.csv")

plt.figure(figsize=(8, 5))
plt.scatter(df["log_mass_ratio"], df["relativistic_collisions"], color='blue', label="Relativistic Collisions")
plt.scatter(df["log_mass_ratio"], df["classical_collisions"], color='red', label="Classical Collisions")
plt.plot(df["log_mass_ratio"], df["relativistic_collisions"], linestyle='dashed', color='blue', alpha=0.7)
plt.plot(df["log_mass_ratio"], df["classical_collisions"], linestyle='dotted', color='red', alpha=0.7)

plt.xlabel("Log(Mass Ratio)")
plt.ylabel("Collision Count")
plt.title("Comparison of Relativistic vs Classical Collisions")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()