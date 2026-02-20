# Agricultural Data Factory 🚜
**Assignment #1: Field Data Acquisition & Documentation**

## 📊 Live Viewer
**[👉 Click Here to View the Interactive Field Map](https://bellfireg.github.io/Agricultural-Data-Analytics/)**
*(Note: Requires GitHub Pages to be enabled in Settings > Pages > Source: `docs/`)*

## 📂 Project Structure
- **`docs/index.html`**: The interactive map (Corn/Soybeans/Wheat/Alfalfa/Oats).
- **`ASSIGNMENT_1.md`**: Detailed report on spatial characteristics and dataset stats.
- **`data/boundaries`**: The raw GeoJSON data (500 standardized fields).
- **`packages/agri-data-toolkit`**: Python package for data fetching.

## 🚀 How to Run Locally
1.  **Install**:
    ```bash
    pip install -e packages/agri-data-toolkit
    pip install -r requirements.txt
    ```
2.  **Generate Data**:
    ```bash
    agri-toolkit download --limit 500
    ```
3.  **Visualise**:
    ```bash
    python scripts/visualize_fields.py
    ```

## 🛠️ Technologies
- **Python**: Core logic.
- **GeoPandas**: Vector data manipulation.
- **Folium**: Interactive mapping.
- **USDA NASS**: Data standards.
