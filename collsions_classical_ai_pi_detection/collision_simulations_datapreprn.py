import csv

# Function to apply momentum transfer in an elastic collision
def mulA(vec, m1, m2):
    msum = (m1 + m2)
    a11 = (m1 - m2) / float(msum)
    a12 = 2 * m2 / float(msum)
    a21 = 2 * m1 / float(msum)
    a22 = (m2 - m1) / float(msum)

    v1 = a11 * vec[0] + a12 * vec[1]
    v2 = a21 * vec[0] + a22 * vec[1]

    return [v1, v2]

# Function for wall collision (inverts velocity)
def mulW(vec):
    return [-vec[0], vec[1]]

# Function to check if collisions should continue
def checkspeeds(speed1, speed2):
    return not (speed1 <= 0 and speed2 <= 0 and abs(speed2) >= abs(speed1))

# Define mass ratios to test
mass_ratios = [10**i for i in range(0, 10)]  # Testing from 1 to 1,000,000 any higher and its comparable to c

# Open CSV file to store results
with open("collisions_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Mass Ratio", "Collision Count"])  # Column headers

    # Iterate over different mass ratios
    for ratio in mass_ratios:
        m1 = 1
        m2 = ratio

        initvector = [0, 1]  # Initial velocities
        currentvector = initvector[:]
        collisioncount = 0
        mtype = 'A'

        # Run the simulation
        while checkspeeds(currentvector[0], currentvector[1]):
            if mtype == 'A':
                currentvector = mulA(currentvector, m1, m2)
                mtype = 'W'
            else:
                currentvector = mulW(currentvector)
                mtype = 'A'
            collisioncount += 1

        # Store results
        writer.writerow([m2, collisioncount])
        print(f"Mass ratio {m2}: {collisioncount} collisions")

print("Collision data saved in collisions_data.csv")
