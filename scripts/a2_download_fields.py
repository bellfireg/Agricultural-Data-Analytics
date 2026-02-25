from skills import FieldBoundariesSkill


def main():
    print("🚜 Downloading Field Boundaries...")
    skill = FieldBoundariesSkill(config="data")
    fields = skill.download(
        count=30,  # 20-30 fields requested
        regions=['corn_belt'],
        output_path='data/assignment-02/fields_EPSG4326.geojson'
    )
    
    print("✅ Field boundaries downloaded successfully!")
    print(f"Total fields: {len(fields)}")
    print(fields.head())

if __name__ == "__main__":
    main()
