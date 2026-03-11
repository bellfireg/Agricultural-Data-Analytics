# Assignment 4 Tracker: Geospatial Mapping and Field Variability Visualization

## Spatial Integration Summary
For this assignment, we successfully merged two distinct spatial datasets to analyze field variability:
1. **Field Boundaries (GeoJSON)**: Farm plot geometries obtained from the previously established APIs.
2. **SSURGO Soil Data (CSV)**: Environmental factors mapped securely by the `field_id` corresponding to the boundaries layer. 

By joining these tables within Python using the `merge` function, the environmental properties were seamlessly translated into spatial properties, forming a unified, multifaceted dataset (`field_soil_gdf`).

## CRS Alignment & Challenges
Before conducting the mapping overlay, we actively ensured data uniformity by calling the `.to_crs(epsg=4326)` function.
*   **Original Data Checks**: Both the field boundaries and the soil exports inherently matched the standard geographic coordinate reference system (EPSG:4326) during initial acquisition. 
*   **Challenge Mitigation**: Nevertheless, programmatically invoking `.to_crs()` serves to protect the codebase against potential upstream alterations or accidental CSV projection changes, ensuring the base layer and soil styling overlay align cleanly on the Matplotlib axis. 

## Dashboard Asset
The finalized, high-resolution geospatial map featuring the categorical soil type overlay has been generated.
*   **Output Path**: `output/dashboard_assets/field_spatial_map.png`

*Completed by: Bayu Hanafi & Antigravity Assistant*
