
import geopandas as gpd
import folium
from pathlib import Path
import json

# Configuration
input_file = Path("data/boundaries/fields.geojson")
output_file = Path("docs/index.html")

def create_map():
    print(f"🗺️  Loading data from {input_file}...")
    
    if not input_file.exists():
        print("❌ Error: Data file not found.")
        return

    # Load Data
    gdf = gpd.read_file(input_file)
    
    # fix: Convert Timestamps to strings for JSON serialization
    for col in gdf.columns:
        if gdf[col].dtype == 'object' or 'datetime' in str(gdf[col].dtype):
            try:
                 gdf[col] = gdf[col].astype(str)
            except:
                pass
    
    # Calculate Center
    center_lat = gdf.geometry.centroid.y.mean()
    center_lon = gdf.geometry.centroid.x.mean()
    
    # Create Map
    m = folium.Map(location=[center_lat, center_lon], zoom_start=13, tiles="OpenStreetMap")
    
    # Add Fields
    print(f"🎨 Drawing {len(gdf)} fields...")
    
    # Style Function based on Crop Type
    def style_function(feature):
        crop = feature['properties']['crop_2023']
        colors = {
            "Corn": "#ffd700",      # Gold
            "Soybeans": "#228b22",  # Forest Green
            "Wheat": "#f4a460",     # Sandy Brown
            "Alfalfa": "#90ee90",   # Light Green
            "Oats": "#deb887"       # Burlywood
        }
        return {
            'fillColor': colors.get(crop, '#808080'),
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.6
        }

    # Add GeoJSON layer
    folium.GeoJson(
        gdf,
        name="Agricultural Fields",
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(
            fields=['field_id', 'crop_2023', 'acres', 'yield_2023', 'owner'],
            aliases=['Field ID:', 'Crop:', 'Acres:', 'Yield (bu/ac):', 'Owner:']
        )
    ).add_to(m)
    
    # Add Layer Control
    folium.LayerControl().add_to(m)
    
    # Save Map
    m.save(output_file)
    print(f"✅ Map saved to: {output_file}")
    
if __name__ == "__main__":
    create_map()
