import matplotlib.pyplot as plt

# Define sample yield curve data
maturities = [1, 2, 5, 10, 30]       # in years
yields = [3.2, 3.5, 3.8, 4.0, 4.2]   # in percent

# Plot
plt.figure(figsize=(8, 5))
plt.plot(maturities, yields, marker='o', linestyle='-', color='steelblue')
plt.title('Example Yield Curve')
plt.xlabel('Maturity (Years)')
plt.ylabel('Yield (%)')
plt.grid(True)

# Save image to correct path
plt.savefig('../assets/yield_curve.png', dpi=300)
