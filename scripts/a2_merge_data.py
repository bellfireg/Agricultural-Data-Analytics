import geopandas as gpd
import pandas as pd

def main():
    print("🔄 Merging Fields and Crops...")
    
    # 1. Load Geometries
    field_file = 'data/assignment-02/fields_EPSG4326.geojson'
    gdf = gpd.read_file(field_file)
    
    # 2. Load Crops
    crop_file = 'data/assignment-02/cdl_EPSG4326.csv'
    crop_df = pd.read_csv(crop_file)
    
    # For visualization, we generally want the latest crop, but we can pivot 
    # the years into separate columns to keep all history in the geojson.
    # Pivot crop data so each year is a column
    crop_pivot = crop_df.pivot(index='field_id', columns='year', values='crop_name')
    # Rename columns to clear names
    crop_cols = {col: f"crop_{col}" for col in crop_pivot.columns}
    crop_pivot.rename(columns=crop_cols, inplace=True)
    crop_pivot.reset_index(inplace=True)
    
    # 3. Merge data via Primary Key (field_id)
    merged_gdf = gdf.merge(crop_pivot, on='field_id', how='left')
    
    # 4. Save
    output_path = 'data/assignment-02/fields_with_crops.geojson'
    merged_gdf.to_file(output_path, driver='GeoJSON')
    
    print(f"✅ Merged dataset created at {output_path}!")
    print(f"Total merged records: {len(merged_gdf)}")
    print("Sample:\n", merged_gdf[['field_id']].head())

if __name__ == "__main__":
    main()
