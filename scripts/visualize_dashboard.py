import geopandas as gpd
import pandas as pd
import folium
from pathlib import Path

# Data paths
FIELD_FILE = "data/boundaries/fields_subset.geojson"
SOIL_FILE = "data/my_soil.csv"
WEATHER_FILE = "data/my_weather.csv"
CROP_FILE = "data/my_crops.csv"
OUTPUT_FILE = "data/agricultural_dashboard.html"

def create_dashboard():
    print("🗺️ Loading datasets...")
    
    # 1. Load Geometries
    gdf = gpd.read_file(FIELD_FILE)
    
    # 2. Load and merge attributes
    if Path(SOIL_FILE).exists() and Path(SOIL_FILE).stat().st_size > 10:
        try:
            soil_df = pd.read_csv(SOIL_FILE)
        # Assuming soil_df has 'field_id' and 'soil_name' or similar
        # Let's take the dominant soil per field or just first row per field
            soil_summary = soil_df.groupby('field_id').first().reset_index()
            # Rename for clarity
            soil_cols = {c: f"Soil_{c}" for c in soil_summary.columns if c != 'field_id'}
            soil_summary.rename(columns=soil_cols, inplace=True)
            gdf = gdf.merge(soil_summary, on="field_id", how="left")
        except pd.errors.EmptyDataError:
            print("⚠️ Soil data file is empty. Skipping soil layer.")
        
    if Path(WEATHER_FILE).exists() and Path(WEATHER_FILE).stat().st_size > 10:
        try:
            weather_df = pd.read_csv(WEATHER_FILE)
            weather_summary = weather_df.groupby('field_id').agg({
                'T2M': 'mean',
                'PRECTOTCORR': 'sum'
            }).reset_index()
            weather_summary.rename(columns={'T2M': 'Avg_Temp_C', 'PRECTOTCORR': 'Total_Precip_mm'}, inplace=True)
            gdf = gdf.merge(weather_summary, on="field_id", how="left")
        except Exception as e:
            print(f"⚠️ Weather data error: {e}")
            
    if Path(CROP_FILE).exists() and Path(CROP_FILE).stat().st_size > 10:
        try:
            crop_df = pd.read_csv(CROP_FILE)
            crop_summary = crop_df.groupby('field_id').first().reset_index()
            crop_cols = {c: f"Crop_{c}" for c in crop_summary.columns if c != 'field_id'}
            crop_summary.rename(columns=crop_cols, inplace=True)
            gdf = gdf.merge(crop_summary, on="field_id", how="left")
        except Exception as e:
            print(f"⚠️ Crop data error: {e}")

    # Ensure JSON serializability for Folium tooltips
    for col in gdf.columns:
        if col != 'geometry':
            # fill NA values so they don't say 'nan'
            gdf[col] = gdf[col].fillna('N/A').astype(str)

    print("🌐 Building interactive map...")
    
    # Find center
    center_lat = gdf.geometry.centroid.y.mean()
    center_lon = gdf.geometry.centroid.x.mean()
    
    m = folium.Map(location=[center_lat, center_lon], zoom_start=11, tiles="CartoDB positron")
    
    # Create feature group for fields
    fg = folium.FeatureGroup(name="Fields")
    
    # Define color scheme based on Crop_2023 or random
    def get_color(feature):
        props = feature['properties']
        crop = props.get('Crop_crop_name', props.get('crop_2023', 'Unknown'))
        if 'corn' in str(crop).lower(): return '#ffd700'
        if 'soybean' in str(crop).lower(): return '#4caf50'
        if 'wheat' in str(crop).lower(): return '#ff9800'
        return '#9e9e9e'

    # Add GeoJson to map
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
    
    fg.add_to(m)
    
    # Add layer control
    folium.LayerControl().add_to(m)
    
    # Save
    m.save(OUTPUT_FILE)
    print(f"✅ Dashboard generated at: {OUTPUT_FILE}")

if __name__ == "__main__":
    create_dashboard()
