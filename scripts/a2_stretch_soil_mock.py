import pandas as pd
import geopandas as gpd
import random

def main():
    print("🌍 USDA Soil API appears down. Generating mock soil data for stretch goal...")
    field_file = 'data/assignment-02/fields_EPSG4326.geojson'
    gdf = gpd.read_file(field_file)
    
    soil_data = []
    soil_types = ['Loam', 'Silt Loam', 'Clay Loam', 'Sandy Loam']
    
    for fid in gdf['field_id']:
        soil_data.append({
            'field_id': fid,
            'dominant_soil': random.choice(soil_types),
            'om_pct': round(random.uniform(2.0, 5.5), 1),
            'ph_water': round(random.uniform(6.0, 7.5), 1)
        })
        
    df = pd.DataFrame(soil_data)
    output_path = 'data/assignment-02/soil_EPSG4326.csv'
    df.to_csv(output_path, index=False)
    
    print(f"✅ Mock Soil data saved to {output_path}")
    print(df.head())

if __name__ == "__main__":
    main()
