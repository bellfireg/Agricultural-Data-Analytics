
import geopandas as gpd
import pandas as pd
from pathlib import Path

# Load Data
data_path = Path("data/boundaries/fields.geojson")
if not data_path.exists():
    print("Error: Data not found!")
    exit(1)

gdf = gpd.read_file(data_path)

# Calculate Stats
total_fields = len(gdf)
total_acres = gdf['acres'].sum()
crs = gdf.crs
bounds = gdf.total_bounds # minx, miny, maxx, maxy
crop_counts = gdf['crop_2023'].value_counts().to_markdown()

# Generate Report Content
report = f"""# Assignment #1: Field Data Acquisition and Documentation

## 1. Dataset Overview
- **File Name**: `fields.geojson`
- **Source**: Simulated Field Data (USDA CLU Proxy)
- **Total Fields**: {total_fields}
- **Total Area**: {total_acres:,.2f} Acres

## 2. Spatial Characteristics (Curriculum Alignment)
- **Data Type**: Vector (Polygons) - *As defined in Class 03 Key Takeaways*
- **Coordinate Reference System (CRS)**: {crs} (WGS 84)
- **Geometry Type**: Polygon
- **Spatial Extent**:
  - **West**: {bounds[0]:.4f}
  - **South**: {bounds[1]:.4f}
  - **East**: {bounds[2]:.4f}
  - **North**: {bounds[3]:.4f}

## 3. Attribute Table Observations
The dataset connects everything through **Field Boundaries** (Key Takeaway).
Attributes include:
- `field_id`: Unique identifier (Primary Key for future joins).
- `crop_2023`: Crop type (Corn, Soybeans, Wheat, Alfalfa, Oats).
- `acres`: Calculated area of the field.
- `yield_2023`: Recorded yield (Bushels/Acre).
- `owner`: Anonymized owner ID.

### Crop Distribution (2023)
{crop_counts}
"""

with open("ASSIGNMENT_1.md", "w") as f:
    f.write(report)

print("✅ Report generated: ASSIGNMENT_1.md")
