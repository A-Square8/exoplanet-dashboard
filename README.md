# Astronomy Observation Insights Dashboard

A modular, interactive data analytics dashboard that explores exoplanet discoveries from the NASA Exoplanet Archive. This project showcases a complete data science pipeline—ingestion, cleaning, feature engineering, analysis, and visualization—built with Python and deployed as a web app using Streamlit.

## Overview

This dashboard analyzes real-time exoplanet data to uncover trends, statistical insights, and habitable zone classifications. It features:
- **Modular Structure**: Separates the data science process into distinct modules for clarity and scalability.
- **Complex Analytics**: Includes correlation heatmaps, ANOVA statistical tests, and custom habitable zone calculations based on stellar parameters.
- **Interactive Visualizations**: Offers line charts, bar charts, scatter plots with trendlines, 3D star maps, and box plots using Plotly.
- **Deployment**: Hosted on Streamlit Community Cloud for public access.

## Features

- **Data Ingestion**: Fetches live data from the NASA Exoplanet Archive.
- **Data Cleaning**: Handles missing values and outliers (e.g., extreme orbital periods).
- **Feature Engineering**: Classifies planets (Rocky, Super-Earth, etc.) and computes habitable zone boundaries using stellar luminosity and temperature.
- **Analysis**: Provides discovery rates, method counts, correlation matrices, ANOVA tests for planet radii, and average star brightness.
- **Visualization**: Interactive plots to explore trends, distributions, and spatial data.
- **User Interaction**: Filters by year, discovery method, planet type, and habitable zone class; includes data export as CSV.

## Tech Stack

- **Languages/Frameworks**: Python, Streamlit
- **Libraries**: Pandas, Plotly, pandasql, SciPy, statsmodels
- **Deployment**: Streamlit Community Cloud
- **Version Control**: Git, GitHub
