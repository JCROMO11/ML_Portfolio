# Scopus Country Collaboration Network

## Overview

This project analyzes Scopus papers to visualize the collaboration network between the most frequent countries of authors' affiliations. The process involves:

1. **Loading Data**: The dataset containing paper affiliations is loaded from an online CSV file.
2. **Data Cleaning**: Rows with missing affiliation data are removed.
3. **Country Extraction**: Extracts countries from the affiliations.
4. **Country Frequency Calculation**: Counts the frequency of each country in the dataset.
5. **Co-occurrence Analysis**: Computes the co-occurrence of the most frequent countries.
6. **Network Visualization**: Uses `networkx` to create and visualize a network graph of countries that collaborate the most.

The project provides a visualization of country collaboration patterns using co-occurrence data.

## Features

- **Data Loading**: Automatically loads the `scopus-papers.csv` dataset.
- **Data Cleaning**: Removes rows with missing affiliation data.
- **Country Extraction**: Transforms affiliation information into a list of countries.
- **Country Frequency Calculation**: Counts the frequency of each country mentioned in the dataset.
- **Co-occurrence Network**: Computes the co-occurrence of the most frequent countries.
- **Network Visualization**: Visualizes the country collaboration network using `networkx` and `matplotlib`.

## Workflow

1. **Loading Data**: The `load_affiliations()` function loads the dataset from a CSV file.
2. **Data Cleaning**: The `remove_na_rows()` function removes rows with missing affiliation data.
3. **Country Extraction**: The `create_countries_column()` function transforms affiliations into country names.
4. **Counting Country Frequencies**: The `count_country_frequency()` function calculates how often each country appears.
5. **Selecting Frequent Countries**: The `select_most_frequente_countries()` function selects the top `n` most frequent countries.
6. **Co-occurrence Analysis**: The `compute_co_occurrences()` function analyzes co-occurrences of the most frequent countries.
7. **Network Visualization**: The `plot_country_collaboration()` function visualizes the collaboration network.