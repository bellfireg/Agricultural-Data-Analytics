import geopandas as gpd

input_file = "data/boundaries/fields.geojson"
output_file = "data/boundaries/fields_subset.geojson"

print("🗺️ Loading original fields...")
gdf = gpd.read_file(input_file)
subset = gdf.head(20) # Take just 20 fields to speed up API calls
subset.to_file(output_file, driver="GeoJSON")
print(f"✅ Created subset with 20 fields at {output_file}")
