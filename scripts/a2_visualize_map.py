import geopandas as gpd
import pandas as pd
import folium

def main():
    print("🌐 Building interactive map...")
    
    # 1. Load data
    file_path = 'data/assignment-02/fields_with_crops.geojson'
    gdf = gpd.read_file(file_path)
    
    # Clean NaNs to prevent JS errors in Folium
    for col in gdf.columns:
        if col != 'geometry':
            gdf[col] = gdf[col].fillna('Unknown').astype(str)
            
    import os
    # Load and merge soil
    soil_file = 'data/assignment-02/soil_EPSG4326.csv'
    if os.path.exists(soil_file) and os.path.getsize(soil_file) > 10:
        try:
            soil_df = pd.read_csv(soil_file)
            gdf = gdf.merge(soil_df, on='field_id', how='left')
        except Exception as e:
            print(f"⚠️ Error reading soil data: {e}")
    
    # 2. Setup map
    center_lat = gdf.geometry.centroid.y.mean()
    center_lon = gdf.geometry.centroid.x.mean()
    m = folium.Map(location=[center_lat, center_lon], zoom_start=12, tiles="CartoDB positron")
    
    # 3. Create Feature Group and Colored Polygons
    fg = folium.FeatureGroup(name="Fields")
    
    def get_color(feature):
        crop = feature['properties'].get('crop_2023', 'Unknown').lower()
        if 'corn' in crop: return '#ffd700'
        if 'soybean' in crop: return '#4caf50'
        if 'wheat' in crop: return '#ff9800'
        return '#9e9e9e'

    folium.GeoJson(
        gdf,
        style_function=lambda feature: {
            'fillColor': get_color(feature),
            'color': '#333333',
            'weight': 1,
            'fillOpacity': 0.7
        },
        tooltip=folium.GeoJsonTooltip(
            fields=[c for c in gdf.columns if c != 'geometry'],
            aliases=[c.replace('_', ' ').title() + ":" for c in gdf.columns if c != 'geometry'],
            localize=True
        )
    ).add_to(fg)
    
    # 4. Add to map and save
    fg.add_to(m)
    folium.LayerControl().add_to(m)
    
    output_path = 'data/assignment-02/my_fields_map.html'
    m.save(output_path)
    print(f"✅ Map created successfully at {output_path}!")

if __name__ == "__main__":
    main()
