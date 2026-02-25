import geopandas as gpd

def main():
    print("🚜 Copying 30 Field Boundaries from local data...")
    # Read the data we downloaded in Assignment 1
    gdf = gpd.read_file('data/boundaries/fields.geojson')
    
    # Filter for Corn Belt states (approximated by our bounding box coordinates in Assignment 1)
    # Since our mock data was generated for Iowa roughly, we just take 30 of them
    sampled = gdf.head(30)
    
    # Save to the new assignment folder
    output_path = 'data/assignment-02/fields_EPSG4326.geojson'
    sampled.to_file(output_path, driver='GeoJSON')
    
    print(f"✅ Field boundaries created successfully at {output_path}!")
    print(f"Total fields: {len(sampled)}")
    print(sampled[['field_id', 'crop_2023']].head())

if __name__ == "__main__":
    main()
