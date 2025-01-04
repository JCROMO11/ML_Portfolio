# Scopus Affiliations Analysis

## Overview

This project processes a dataset of Scopus papers to analyze the affiliations of authors and plot the frequency of countries based on these affiliations. The workflow involves:

1. **Loading Data**: The data is loaded from an online CSV file containing paper affiliations.
2. **Cleaning Data**: Rows with missing affiliation data are removed.
3. **Country Extraction**: Extracts country names from the affiliation data.
4. **Country Frequency**: Counts the frequency of each country mentioned.
5. **Visualization**: Plots a world map showing the frequency of countries using the `folium` library.

The project provides insights into the distribution of authors' affiliations by country and visualizes the results on an interactive map.

## Features

- **Data Loading**: Automatically loads the `scopus-papers.csv` file.
- **Data Cleaning**: Removes rows with missing affiliation data and standardizes country names.
- **Country Extraction**: Extracts and normalizes country names from affiliation data.
- **Country Frequency Analysis**: Counts the frequency of each country across all authors' affiliations.
- **World Map Visualization**: Uses `folium` to create a choropleth map based on the frequency of countries.

## Workflow

1. **Loading Data**: The `load_affiliations()` function loads the dataset from a CSV file and extracts the 'Affiliations' column.
2. **Cleaning Data**: The `remove_na_rows()` function removes rows with missing affiliation data.
3. **Extracting Countries**: The `add_countries_column()` function transforms the 'Affiliations' column into a list of countries.
4. **Country Normalization**: The `clean_countries()` function replaces specific country names to ensure consistency (e.g., "United States" becomes "United States of America").
5. **Counting Frequency**: The `count_country_frequency()` function counts the occurrences of each country.
6. **Map Visualization**: The `plot_world_map()` function creates a world map that visualizes the frequency of each country using `folium`.
