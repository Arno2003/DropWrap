import folium
import pandas as pd

# Sample data (replace with your dataset)
data = pd.DataFrame({
    'Student_ID': [1, 2, 3, 4, 5],
    'Dropout_Reason': ['Financial', 'Academic', 'Personal', 'Financial', 'Academic'],
    # Replace with actual latitudes
    'Latitude': [40.7128, 34.0522, 41.8781, 38.8951, 37.7749],
    # Replace with actual longitudes
    'Longitude': [-74.0060, -118.2437, -87.6298, -77.0364, -122.4194],
    # Cluster labels from hierarchical clustering
    'Cluster_Label': [1, 2, 1, 3, 2]
})

# Create a base map
m = folium.Map(location=[data['Latitude'].mean(),
               data['Longitude'].mean()], zoom_start=5)

# Create markers for each student
for _, row in data.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"Student ID: {row['Student_ID']}, Dropout Reason: {row['Dropout_Reason']}, Cluster: {row['Cluster_Label']}",
        icon=folium.Icon(color='blue' if row['Cluster_Label'] ==
                         1 else 'green' if row['Cluster_Label'] == 2 else 'red')
    ).add_to(m)

# Display the map
m.save('student_dropout_map.html')
