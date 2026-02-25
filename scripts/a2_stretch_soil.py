from skills import SSURGOSoilSkill

def main():
    print("🌍 Downloading Soil Data (Stretch Goal)...")
    skill = SSURGOSoilSkill()
    
    field_file = 'data/assignment-02/fields_EPSG4326.geojson'
    
    soil = skill.download_for_fields(
        field_file,
        output_path='data/assignment-02/soil_EPSG4326.csv'
    )
    
    print("✅ Soil data downloaded successfully!")
    print(soil.head())

if __name__ == "__main__":
    main()
