import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Sample student data
df = pd.DataFrame({
    'student_id': range(1, 11),
    'GPA': [3.5, 2.8, 3.9, 2.4, 3.2, 2.9, 3.6, 3.0, 2.7, 3.7],
    'study_hours': [10, 5, 15, 3, 8, 6, 12, 7, 4, 14],
    'attendance_rate': [90, 70, 95, 60, 85, 75, 92, 80, 65, 93]
})

print(df)

# Selecting features for clustering
X = df[['GPA', 'study_hours', 'attendance_rate']]

# Apply Standard Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


wcss = []
for i in range(2, 7):  # Trying K from 2 to 6
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plotting the elbow curve
plt.plot(range(2, 7), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()


# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Visualizing clusters
plt.figure(figsize=(8, 5))
for label in df['cluster'].unique():
    cluster_data = df[df['cluster'] == label]
    plt.scatter(cluster_data['study_hours'], cluster_data['GPA'], label=f'Cluster {label}', s=100)

plt.title("Student Clusters Based on Academic Performance")
plt.xlabel("Weekly Study Hours")
plt.ylabel("GPA")
plt.legend()
plt.grid(True)
plt.show()


# Final student table with cluster labels
print(df[['student_id', 'GPA', 'study_hours', 'attendance_rate', 'cluster']])
