---
license: mit
task_categories:
- time-series-forecasting
tags:
- nigeria
- agriculture
- food-systems
- synthetic
- crop-production-and-yields
size_categories:
- 100K<n<1M
---

# Nigeria Agriculture – Seasonal Crop Yields

## Dataset Description

State/LGA-level yields by crop, season, area, production, and quality grade.

**Category**: Crop Production & Yields  
**Rows**: 140,000  
**Format**: CSV, Parquet  
**License**: MIT  
**Synthetic**: Yes (generated using reference data from FAO, NBS, NiMet, FMARD)

## Dataset Structure

### Schema

- **state**: string
- **lga**: string
- **crop**: string
- **season**: string
- **area_ha**: float
- **yield_t_ha**: float
- **production_t**: float
- **quality_grade**: string

### Sample Data

```
| state   | lga            | crop    | season   |   area_ha |   yield_t_ha |   production_t | quality_grade   |
|:--------|:---------------|:--------|:---------|----------:|-------------:|---------------:|:----------------|
| Rivers  | Rivers-LGA-13  | yam     | 2025_wet |     306.5 |        12.41 |         3802.8 | Grade A         |
| Kwara   | Kwara-LGA-10   | cassava | 2022_dry |     100.1 |        10.93 |         1093.3 | Grade A         |
| Taraba  | Taraba-LGA-13  | sorghum | 2023_wet |     624.2 |         0.97 |          608   | Grade A         |
| Katsina | Katsina-LGA-02 | yam     | 2023_wet |     545   |         6.43 |         3503.9 | Grade A         |
| Enugu   | Enugu-LGA-07   | rice    | 2024_wet |    2591.8 |         3.03 |         7855.6 | Grade A         |
```

## Data Generation Methodology

This dataset was synthetically generated using:

1. **Reference Sources**:
   - FAO (Food and Agriculture Organization) - crop yields, production data
   - NBS (National Bureau of Statistics, Nigeria) - farm characteristics, surveys
   - NiMet (Nigerian Meteorological Agency) - weather patterns
   - FMARD (Federal Ministry of Agriculture and Rural Development) - extension guides
   - IITA (International Institute of Tropical Agriculture) - agronomic research

2. **Domain Constraints**:
   - Crop calendars and phenology (planting/harvest windows)
   - Agro-ecological zone characteristics (Sahel, Sudan Savanna, Guinea Savanna, Rainforest)
   - Nigeria-specific realities (smallholder dominance, market dynamics, conflict zones)
   - Statistical distributions matching national agricultural patterns

3. **Quality Assurance**:
   - Distribution testing (KS test, chi-square)
   - Correlation validation (rainfall-yield, fertilizer-yield, yield-price)
   - Causal consistency (DAG-based generation)
   - Multi-scale coherence (farm → state aggregations)
   - Ethical considerations (representative, unbiased)

See `QUALITY_ASSURANCE.md` in the repository for full methodology.

## Use Cases

- **Machine Learning**: Yield prediction, price forecasting, pest detection, supply chain optimization
- **Policy Analysis**: Agricultural program evaluation, subsidy impact assessment, food security planning
- **Research**: Climate-agriculture interactions, market dynamics, technology adoption patterns
- **Education**: Teaching agricultural economics, data science applications in agriculture

## Limitations

- **Synthetic data**: While grounded in real distributions, individual records are not real observations
- **Simplified dynamics**: Some complex interactions (e.g., multi-generational pest populations) are simplified
- **Temporal scope**: Covers 2022-2025; may not reflect longer-term trends or future climate scenarios
- **Spatial resolution**: State/LGA level; does not capture micro-level heterogeneity within localities

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{nigeria_agriculture_2025,
  title = {Nigeria Agriculture – Seasonal Crop Yields},
  author = {Electric Sheep Africa},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/datasets/electricsheepafrica/nigerian_agriculture_seasonal_crop_yields}
}
```

## Related Datasets

This dataset is part of the **Nigeria Agriculture & Food Systems** collection:
- https://huggingface.co/collections/electricsheepafrica/nigeria-agriculture-and-food-systems

## Contact

For questions, feedback, or collaboration:
- **Organization**: Electric Sheep Africa
- **Collection**: Nigeria Agriculture & Food Systems
- **Repository**: https://github.com/electricsheepafrica/nigerian-datasets

## Changelog

### Version 1.0.0 (October 2025)
- Initial release
- 140,000 synthetic records
- Quality-assured using FAO/NBS/NiMet reference data
