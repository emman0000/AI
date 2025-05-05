import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample vehicle data
data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

# Create DataFrame
df = pd.DataFrame(data)
print(df)

# One-hot encode vehicle_type, drop_first avoids dummy variable trap
df_encoded = pd.get_dummies(df, columns=['vehicle_type'], drop_first=True)

# Drop identifier
X_unscaled = df_encoded.drop(columns=['vehicle_serial_no'])

# Apply KMeans
kmeans_unscaled = KMeans(n_clusters=3, random_state=42)
df['cluster_unscaled'] = kmeans_unscaled.fit_predict(X_unscaled)

# Show results
print("\nClusters without scaling:")
print(df[['vehicle_serial_no', 'mileage', 'fuel_efficiency', 'maintenance_cost', 'cluster_unscaled']])


# Scale numeric features only
features_to_scale = ['mileage', 'fuel_efficiency', 'maintenance_cost']
scaler = StandardScaler()

X_scaled = df_encoded.copy()
X_scaled[features_to_scale] = scaler.fit_transform(X_scaled[features_to_scale])

# Apply KMeans
X_scaled_input = X_scaled.drop(columns=['vehicle_serial_no'])
kmeans_scaled = KMeans(n_clusters=3, random_state=42)
df['cluster_scaled'] = kmeans_scaled.fit_predict(X_scaled_input)

# Show results
print("\nClusters with scaling:")
print(df[['vehicle_serial_no', 'mileage', 'fuel_efficiency', 'maintenance_cost', 'cluster_scaled']])

# Plot with scaling
plt.figure(figsize=(8,5))
colors = ['red', 'green', 'blue']
for label in df['cluster_scaled'].unique():
    temp = df[df['cluster_scaled'] == label]
    plt.scatter(temp['mileage'], temp['fuel_efficiency'], 
                c=colors[label], label=f'Cluster {label}', s=100)
    
plt.xlabel('Mileage')
plt.ylabel('Fuel Efficiency')
plt.title('Vehicle Clusters (Using Scaled Features)')
plt.legend()
plt.grid(True)
plt.show()


print("\nComparison Table:")
print(df[['vehicle_serial_no', 'cluster_unscaled', 'cluster_scaled']])
