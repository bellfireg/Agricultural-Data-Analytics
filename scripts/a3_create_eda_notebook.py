import os
import nbformat as nbf
import pandas as pd
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt

def create_notebook():
    os.makedirs('notebooks', exist_ok=True)
    nb = nbf.v4.new_notebook()
    
    cells = []
    
    # Title
    cells.append(nbf.v4.new_markdown_cell("# Assignment 3: Exploratory Data Analysis of Row Crop Fields\n\n## 1. Data Ingestion & Inspection"))
    
    # Imports & Load Data
    code = """import pandas as pd
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Seaborn style
sns.set_theme(style="whitegrid", palette="YlGn")

# Load data merged from Assignment 2
df = gpd.read_file('../data/assignment-02/fields_with_crops.geojson')

# Load and merge soil data
import os
soil_file = '../data/assignment-02/soil_EPSG4326.csv'
if os.path.exists(soil_file):
    soil_df = pd.read_csv(soil_file)
    df = df.merge(soil_df, on='field_id', how='left')

# Basic info
df.info()"""
    cells.append(nbf.v4.new_code_cell(code))
    
    # Describe
    cells.append(nbf.v4.new_markdown_cell("## Basic Statistics\nChecking the summary statistics of the numeric fields."))
    cells.append(nbf.v4.new_code_cell("df.describe()"))
    
    # EDA Visuals
    cells.append(nbf.v4.new_markdown_cell("## 2. Visual Exploration (The \"3 Visuals\" Task)"))
    
    # Visual 1
    code_v1 = """# Visual 1 (Distribution): Soil Organic Matter
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='om_pct', bins=15, kde=True, color='forestgreen')
plt.title('Distribution of Soil Organic Matter (%) across Fields', fontsize=14, pad=15)
plt.xlabel('Organic Matter (%)', fontsize=12)
plt.ylabel('Count of Fields', fontsize=12)
plt.tight_layout()
plt.show()"""
    cells.append(nbf.v4.new_code_cell(code_v1))
    
    # Visual 2
    code_v2 = """# Visual 2 (Relationship): Soil Type vs Acreage
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='dominant_soil', y='acres', palette='YlOrBr')
plt.title('Relationship Between Soil Type and Field Acreage', fontsize=14, pad=15)
plt.xlabel('Dominant Soil Type', fontsize=12)
plt.ylabel('Field Area (Acres)', fontsize=12)
plt.tight_layout()
plt.show()"""
    cells.append(nbf.v4.new_code_cell(code_v2))
    
    # Visual 3
    code_v3 = """# Visual 3 (Correlation): Numerical features Heatmap
plt.figure(figsize=(8, 6))
# Select only numeric columns for correlation (in actual scenario, we convert strings or handle na)
numeric_cols = ['acres', 'om_pct', 'ph_water']
corr = df[numeric_cols].astype(float).corr()

sns.heatmap(corr, annot=True, cmap='Greens', vmin=-1, vmax=1, center=0)
plt.title('Correlation Heatmap of Numeric Field Variables', fontsize=14, pad=15)
plt.tight_layout()
plt.show()"""
    cells.append(nbf.v4.new_code_cell(code_v3))

    # Dashboard Assets
    cells.append(nbf.v4.new_markdown_cell("## 3. High-Res Map Export for Dashboard"))
    code_dash = """import os
os.makedirs('../output/dashboard_assets', exist_ok=True)

# 1. Export High-Res Organic Matter Plot
plt.figure(figsize=(10, 6), dpi=300)
sns.histplot(data=df, x='om_pct', bins=15, kde=True, color='#2ca02c') # agricultural green
plt.title('Soil Organic Matter Distribution', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Organic Matter (%)', fontsize=12, fontweight='bold')
plt.ylabel('Number of Fields', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('../output/dashboard_assets/01_om_distribution.png')
plt.close()

# 2. Export High-Res Soil vs Acreage Boxplot
plt.figure(figsize=(12, 6), dpi=300)
sns.boxplot(data=df, x='dominant_soil', y='acres', palette='YlOrBr') # soil brown palette
plt.title('Field Acreage by Dominant Soil Type', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Soil Classification', fontsize=12, fontweight='bold')
plt.ylabel('Total Area (Acres)', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('../output/dashboard_assets/02_soil_acreage_boxplot.png')
plt.close()

print('✅ High-res dashboard assets saved to output/dashboard_assets/')"""
    cells.append(nbf.v4.new_code_cell(code_dash))

    nb['cells'] = cells
    with open('notebooks/03_field_eda.ipynb', 'w') as f:
        nbf.write(nb, f)
    
    print("✅ Created notebooks/03_field_eda.ipynb")

if __name__ == '__main__':
    create_notebook()
