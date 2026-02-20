# Assignment #1: Field Data Acquisition and Documentation

## 1. Dataset Overview
- **File Name**: `fields.geojson`
- **Source**: Simulated Field Data (USDA CLU Proxy)
- **Total Fields**: 500
- **Total Area**: 20,021.80 Acres

## 2. Spatial Characteristics (Curriculum Alignment)
- **Data Type**: Vector (Polygons) - *As defined in Class 03 Key Takeaways*
- **Coordinate Reference System (CRS)**: EPSG:4326 (WGS 84)
- **Geometry Type**: Polygon
- **Spatial Extent**:
  - **West**: -93.0005
  - **South**: 41.9995
  - **East**: -92.9005
  - **North**: 42.1245

## 3. Attribute Table Observations
The dataset connects everything through **Field Boundaries** (Key Takeaway).
Attributes include:
- `field_id`: Unique identifier (Primary Key for future joins).
- `crop_2023`: Crop type (Corn, Soybeans, Wheat, Alfalfa, Oats).
- `acres`: Calculated area of the field.
- `yield_2023`: Recorded yield (Bushels/Acre).
- `owner`: Anonymized owner ID.

### Crop Distribution (2023)
| crop_2023   |   count |
|:------------|--------:|
| Corn        |     213 |
| Soybeans    |     204 |
| Wheat       |      40 |
| Oats        |      23 |
| Alfalfa     |      20 |
