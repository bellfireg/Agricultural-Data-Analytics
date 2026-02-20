import geopandas as gpd
from shapely.geometry import box
import pandas as pd
import numpy as np
from pathlib import Path

class BoundaryClient:
    """
    Client for fetching Agricultural Field Boundaries.
    Simulates fetching from USDA CLU (Common Land Unit) or similar sources.
    """
    
    def __init__(self, data_dir: str = "./data/boundaries"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def fetch_boundaries(self, limit: int = 10, random: bool = False) -> gpd.GeoDataFrame:
        """
        Simulates downloading field boundaries (Mock Data).
        Now standardized with strict schema.
        """
        print(f"📡 Requesting {limit} fields (Standardized Mock)...")
        
        # Mock Data Generation (Iowa/Corn Belt area)
        start_lat, start_lon = 42.0, -93.0
        fields = []
        
        crops = ["Corn", "Soybeans", "Wheat", "Alfalfa", "Oats"]
        
        for i in range(limit):
            # Create ~40 acre fields (grid pattern with slight jitter)
            # Grid calculation
            row = i // 20 
            col = i % 20
            
            lat_offset = row * 0.005 + np.random.uniform(-0.0005, 0.0005)
            lon_offset = col * 0.005 + np.random.uniform(-0.0005, 0.0005)
            
            minx = start_lon + lon_offset
            miny = start_lat + lat_offset
            maxx = minx + 0.004
            maxy = miny + 0.004
            
            geom = box(minx, miny, maxx, maxy)
            
            fields.append({
                "field_id": f"FLD_{i:04d}",
                "geometry": geom,
                "crop_2023": np.random.choice(crops, p=[0.4, 0.4, 0.1, 0.05, 0.05]),
                "acres": round(40.0 + np.random.uniform(-2, 2), 2),
                "yield_2023": int(np.random.normal(180, 20) if "Corn" in crops else 50), 
                "owner": f"Farmer_{i%50:03d}",
                "planting_date": f"2023-05-{np.random.randint(1, 30):02d}",
                "soil_type": np.random.choice(["Loam", "Sandy Loam", "Silt Clay"])
            })
            
        gdf = gpd.GeoDataFrame(fields, crs="EPSG:4326")
        
        # STANDARDIZATION STEP
        gdf = self.standardize_schema(gdf)
        
        # Save to file
        output_file = self.data_dir / "fields.geojson"
        gdf.to_file(output_file, driver="GeoJSON")
        
        return gdf, output_file

    def standardize_schema(self, gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """Enforce types and column order."""
        required_columns = {
            "field_id": "object",
            "crop_2023": "object",
            "acres": "float64",
            "yield_2023": "int64",
            "owner": "object", 
            "planting_date": "object",
            "soil_type": "object",
            "geometry": "geometry"
        }
        
        # Ensure all columns exist
        for col, dtype in required_columns.items():
            if col not in gdf.columns:
                gdf[col] = None # Or default value
                
        # Enforce Column Order
        gdf = gdf[list(required_columns.keys())]
        
        # Validate Geometry CRS
        if gdf.crs != "EPSG:4326":
            gdf = gdf.to_crs("EPSG:4326")
            
        return gdf
