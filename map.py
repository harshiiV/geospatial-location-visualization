import pandas as pd
import folium

# Load the CSV file
data = pd.read_csv("students.csv")

# Create a base map (WGS84 coordinates)
map_center = [28.6, 77.2]
m = folium.Map(location=map_center, zoom_start=11)

# Add markers to the map
for _, row in data.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=row["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# Save the map as HTML
m.save("student_location_map.html")

print("Map created successfully!")
