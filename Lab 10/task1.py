

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Mall_Customers.csv")
print(df.head())

# Drop 'CustomerID'
X = df.drop(columns=['CustomerID'])

# K-Means clustering on raw data
kmeans_raw = KMeans(n_clusters=5, init='k-means++', random_state=42)
labels_raw = kmeans_raw.fit_predict(X)

# Visualize two selected features
plt.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'], c=labels_raw, cmap='rainbow')
plt.title('Clusters (Without Scaling)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()

# Copy features to scale
X_scaled = X.copy()

# Scale only 'Annual Income' and 'Spending Score'
scaler = StandardScaler()
X_scaled[['Annual Income (k$)', 'Spending Score (1-100)']] = scaler.fit_transform(
    X_scaled[['Annual Income (k$)', 'Spending Score (1-100)']]
)


# K-Means clustering on scaled features
kmeans_scaled = KMeans(n_clusters=5, init='k-means++', random_state=42)
labels_scaled = kmeans_scaled.fit_predict(X_scaled)

# Visualize again
plt.scatter(X_scaled['Annual Income (k$)'], X_scaled['Spending Score (1-100)'], c=labels_scaled, cmap='rainbow')
plt.title('Clusters (With Scaling)')
plt.xlabel('Scaled Income')
plt.ylabel('Scaled Spending Score')
plt.show()

