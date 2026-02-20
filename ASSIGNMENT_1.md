# Assignment #1: Field Data Acquisition and Documentation

## 1. Dataset Overview
- **File Name**: `fields.geojson`
- **Source**: Simulated Field Data (USDA CLU Proxy)
- **Total Fields**: 200
- **Total Area**: 8,029.63 Acres

## 2. Spatial Characteristics
- **Coordinate Reference System (CRS)**: EPSG:4326 (WGS 84)
- **Geometry Type**: Polygon
- **Spatial Extent**:
  - **West**: -93.0000
  - **South**: 42.0000
  - **East**: -92.9760
  - **North**: 42.1990

## 3. Attribute Table Observations
The dataset contains the following attributes:
- `field_id`: Unique identifier for each field.
- `crop_2023`: Crop type grown in the 2023 season.
- `acres`: Calculated area of the field.
- `yield_2023`: Recorded yield (Bushels/Acre).
- `owner`: Anonymized owner ID.

### Crop Distribution (2023)
| crop_2023   |   count |
|:------------|--------:|
| Soybeans    |      70 |
| Wheat       |      65 |
| Corn        |      65 |
