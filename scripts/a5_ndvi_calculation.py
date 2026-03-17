import os
import numpy as np
import geopandas as gpd
import rasterio
from rasterio.transform import from_bounds
import matplotlib.pyplot as plt

import sys

# To fix import of the skill since the folder structure has dashes
try:
    import sys
    sys.path.append(os.path.abspath('.'))
    # We need to import the class from the module
    import importlib.util
    spec = importlib.util.spec_from_file_location("sentinel2_imagery", "skills/sentinel2-imagery/scripts/sentinel2_imagery.py")
    sentinel2_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sentinel2_module)
    Sentinel2ImagerySkill = sentinel2_module.Sentinel2ImagerySkill
except Exception as e:
    print(f"Error importing skill: {e}")

def create_mock_band(field_geom, filename, is_nir=False):
    """Creates a mock GeoTIFF band for a given field geometry."""
    bounds = field_geom.bounds
    width, height = 100, 100
    transform = from_bounds(bounds[0], bounds[1], bounds[2], bounds[3], width, height)
    
    # Create synthetic data: higher values if NIR, lower if RED to simulate healthy vegetation
    if is_nir:
        data = np.random.uniform(2000, 5000, (height, width)).astype(np.float32)
    else:
        data = np.random.uniform(500, 1500, (height, width)).astype(np.float32)
        
    profile = {
        'driver': 'GTiff',
        'dtype': 'float32',
        'nodata': None,
        'width': width,
        'height': height,
        'count': 1,
        'crs': 'EPSG:4326',
        'transform': transform,
        'compress': 'lzw'
    }
    
    with rasterio.open(filename, 'w', **profile) as dst:
        dst.write(data, 1)

def main():
    os.makedirs('data/assignment-05', exist_ok=True)
    os.makedirs('reports', exist_ok=True)

    print("Loading field boundary...")
    fields = gpd.read_file('data/assignment-02/fields_EPSG4326.geojson')
    field = fields.iloc[0] # Pick the first field
    
    red_path = 'data/assignment-05/sentinel2_field_0_20240715_B4_EPSG4326.tif'
    nir_path = 'data/assignment-05/sentinel2_field_0_20240715_B8_EPSG4326.tif'
    ndvi_path = 'data/assignment-05/sentinel2_field_0_20240715_NDVI_EPSG4326.tif'
    
    print("Generating mock Red and NIR bands (Simulation of Data Read Step)...")
    create_mock_band(field.geometry, red_path, is_nir=False)
    create_mock_band(field.geometry, nir_path, is_nir=True)
    
    print("Calculating NDVI leveraging the Sentinel-2 Imagery Skill...")
    skill = Sentinel2ImagerySkill()
    try:
        skill.calculate_ndvi(red_path, nir_path, ndvi_path)
    except Exception as e:
        print(f"Error calculating NDVI: {e}")
        return

    print("Generating single-band (Red) and NDVI visualizations...")
    
    # Plot Red Band
    fig, ax = plt.subplots(figsize=(8, 6))
    with rasterio.open(red_path) as src:
        im = ax.imshow(src.read(1), cmap='Reds', extent=[src.bounds.left, src.bounds.right, src.bounds.bottom, src.bounds.top])
        plt.colorbar(im, ax=ax, label='Reflectance')
    ax.set_title('Sentinel-2 Single Band (B4 - Red)')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    plt.savefig('data/assignment-05/single_band_red.png', dpi=150, bbox_inches='tight')
    plt.close()

    # Plot NDVI
    fig, ax = plt.subplots(figsize=(8, 6))
    with rasterio.open(ndvi_path) as src:
        im = ax.imshow(src.read(1), cmap='RdYlGn', vmin=-1, vmax=1, extent=[src.bounds.left, src.bounds.right, src.bounds.bottom, src.bounds.top])
        plt.colorbar(im, ax=ax, label='NDVI Value')
    ax.set_title('Crop Health Analysis: NDVI')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    plt.savefig('data/assignment-05/ndvi_output.png', dpi=150, bbox_inches='tight')
    plt.close()

    print("✅ Assets generated successfully in data/assignment-05!")

if __name__ == "__main__":
    main()
