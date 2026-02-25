from pathlib import Path
from skills import SSURGOSoilSkill, NASAPowerWeatherSkill, CDLCroplandSkill

def main():
    field_file = "data/boundaries/fields_subset.geojson"
    
    print("🚜 Fetching Soil data...")
    soil_skill = SSURGOSoilSkill()
    soil_skill.download_for_fields(field_file, output_path="data/my_soil.csv")
    
    print("⛅ Fetching Weather data (2023)...")
    weather_skill = NASAPowerWeatherSkill()
    weather_skill.download_for_fields(
        field_file, 
        start_date="2023-01-01", 
        end_date="2023-12-31", 
        output_path="data/my_weather.csv"
    )
    
    print("🌾 Fetching Crop data (2020-2023)...")
    crop_skill = CDLCroplandSkill()
    crop_skill.download_for_fields(
        field_file, 
        years=[2020, 2021, 2022, 2023], 
        output_path="data/my_crops.csv"
    )

if __name__ == "__main__":
    main()
