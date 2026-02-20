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
        Simulates downloading field boundaries.
        In a real scenario, this would hit the USDA API.
        Here we generate realistic mock data for the workshop.
        """
        print(f"📡 Requesting {limit} fields (Random: {random})...")
        
        # Mock Data Generation (Iowa/Corn Belt area)
        # Creating a grid of fields
        start_lat, start_lon = 42.0, -93.0
        fields = []
        
        for i in range(limit):
            # Create ~40 acre fields (approx 0.004 degrees square)
            lat_offset = (i // 5) * 0.005
            lon_offset = (i % 5) * 0.005
            
            minx = start_lon + lon_offset
            miny = start_lat + lat_offset
            maxx = minx + 0.004
            maxy = miny + 0.004
            
            geom = box(minx, miny, maxx, maxy)
            
            fields.append({
                "field_id": f"FLD_{i:03d}",
                "geometry": geom,
                "crop_2023": np.random.choice(["Corn", "Soybeans", "Wheat"]),
                "acres": 40.0 + np.random.uniform(-2, 2),
                "yield_2023": np.random.choice([180, 200, 220, 50, 60]), # Bushels
                "owner": f"Farmer_{i}"
            })
            
        gdf = gpd.GeoDataFrame(fields, crs="EPSG:4326")
        
        # Save to file
        output_file = self.data_dir / "fields.geojson"
        gdf.to_file(output_file, driver="GeoJSON")
        
        return gdf, output_file
