# Assignment 3 Tracker: Exploratory Data Analysis

## Exploratory Data Analysis (EDA) Takeaways
During the execution of `notebooks/03_field_eda.ipynb`, the following key patterns and relationships were identified across the 30 field boundaries in the Corn Belt region:

1. **Distribution of Organic Matter (`om_pct`)**: The histogram revealed that the soil organic matter percentage primarily clusters between 2.0% and 4.8%. There is a distinct normal-like distribution peaking around 2.5 - 3.5%, indicating reasonably fertile soils typical for Corn Belt plots.
2. **Soil Type vs. Acreage**: The boxplot analysis highlights that "Clay Loam" tends to cover the widest variance of field sizes, whereas "Sandy Loam" and "Loam" soils generally occupied slightly smaller median acreages in this specific sample.
3. **Correlation Analysis**: The heatmap generated from numeric variables (`acres`, `om_pct`, `ph_water`) indicates relatively weak linear correlation among these three variables. For instance, soil pH does not strictly dictate field acreage, meaning these are fairly independent features.

## Data Cleaning Steps
- **Merged Dataset Integration**: The base GeoJSON dataset (`fields_with_crops.geojson`) did not natively contain trailing soil properties. Therefore, during the EDA initialization, we merged `soil_EPSG4326.csv` using the `field_id` primary key to reconstruct the comprehensive dataset.
- **Missing Value Handling**: We observed that all matched fields successfully merged without resulting in NA values for the targeted features, eliminating the need for complex numeric imputation.

## Dashboard Assets Generated
Two refined, high-resolution plots were exported for the final interactive dashboard:
- `output/dashboard_assets/01_om_distribution.png` (Distribution Plot)
- `output/dashboard_assets/02_soil_acreage_boxplot.png` (Relationship Boxplot)

*Completed by: Bayu Hanafi & Antigravity Assistant*
