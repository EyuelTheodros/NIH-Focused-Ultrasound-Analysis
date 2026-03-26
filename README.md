# NIH-Focused-Ultrasound-Analysis
Analysis of NIH-funded focused ultrasound research grants (2022-2026)
An independent data analysis project examining how the NIH funds focused ultrasound research across institutions, therapeutic areas, and fiscal years (2022–2026).

## What This Project Does

Focused ultrasound is a non-invasive technology that uses sound waves to treat conditions inside the body without surgery. This project analyzes 309 NIH-funded grants to answer:

- Which research areas get the most funding?
- Which institutions lead the field?
- Is funding growing or shrinking over time?
- What emerging areas are worth watching?

## Key Findings

- **Oncology** leads in both grant count and total funding
- **Stanford University** is the top-funded institution at $9M+
- Funding showed a **major surge in 2025**
- **Drug delivery** and **neuromodulation** are emerging growth areas

## Tools Used

- **Python** (pandas, matplotlib) — automated categorization and data visualization
- **Excel** — data cleaning, pivot tables, analysis
- **NIH RePORTER** — grant data source

## Files

- `DatanCleaning.xlsx` — Cleaned dataset with 309 grants across 12 key fields
- `categorize.py` — Python script that auto-categorizes grants into 9 research areas
- `analysis.py` — Python script that analyzes top-funded institutions and generates charts
- `top_institutions.png` — Bar chart of top 10 institutions by funding
- `FUS_Funding_Analysis_v2.pdf` — Full summary report with findings

## Data Source

All grant data was exported from [NIH RePORTER](https://reporter.nih.gov/) using the search term "focused ultrasound."
