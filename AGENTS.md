# AGENTS.md: The Instruction Manual

> **Mission**: Build a professional agricultural data factory.

## Key Directive 1: Context Budget (Reading Order)
1. **Analyze Instructions**: Read the prompt carefully.
2. **Check Context**: Look at `AGENTS.md` and related KIs before requesting new files.
3. **Minimize Noise**: Do not read large data files (CSVs, GeoJSONs) directly unless asked. Use `head` or `describe()`.

## Key Directive 2: Code Standards
- **Typing**: Strict type hints are required for all function signatures.
  - `def calculate_yield(acres: float, bushels: int) -> float:`
- **Naming**:
  - Variables/Functions: `snake_case` (e.g., `field_boundary`)
  - Classes: `PascalCase` (e.g., `SatelliteGrid`)
  - Constants: `UPPER_CASE` (e.g., `MAX_RETRIES`)
- **Documentation**: Google-style docstrings for all complex functions.

## Key Directive 3: Autonomy Boundaries
- **CAN**: Write code, run tests, fix lint errors, create files.
- **CANNOT**: Push to production (main branch) directly. Must go through CI/CD.
- **CANNOT**: Commit API keys. Keys must be loaded from `os.environ`.

## Data Dictionary (The Language of the Farm)
- **Field Name** -> `str`
- **Field Count** -> `int`
- **Yield / Area** -> `float`
- **Irrigated?** -> `bool`
- **Crop Rotation** -> `list[str]`
- **Field Metadata** -> `dict`
