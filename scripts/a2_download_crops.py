from skills import CDLCroplandSkill


def main():
    print("🌾 Downloading Crop Data...")
    class DummyConfig:
        def __init__(self):
            import logging
            from pathlib import Path
            self._data_root = Path("data")
            self.raw_data_path = self._data_root / "raw"
            self.processed_data_path = self._data_root / "processed"
            self.logger = logging.getLogger("dummy")
            
    config = DummyConfig()
    skill = CDLCroplandSkill(config=config)
    
    field_file = 'data/assignment-02/fields_EPSG4326.geojson'
    
    crops = skill.download_for_fields(
        field_file,
        years=[2020, 2021, 2022, 2023],
        output_path='data/assignment-02/cdl_EPSG4326.csv'
    )
    
    print("✅ Crop data downloaded successfully!")
    print(crops.head())

if __name__ == "__main__":
    main()
