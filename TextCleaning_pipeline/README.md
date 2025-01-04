# Text Cleaning Pipeline

This project provides a pipeline to clean and preprocess text data. The goal is to read a CSV file with a column of text, apply various cleaning techniques (such as removing punctuation, stemming, and deduplication), and output a cleaned version of the text in a new CSV file.

## Requirements

- Python 3.x
- NLTK (can be installed with `pip install nltk`)
- Pandas (can be installed with `pip install pandas`)

## Description of Functions

1. **`load_data(input_file)`**:
   - Reads the input CSV file using Pandas and returns a DataFrame.

2. **`create_fingerprint(df)`**:
   - Creates a new column called 'fingerprint' by applying several text preprocessing steps:
     - Strips leading/trailing spaces.
     - Converts the text to lowercase.
     - Removes hyphens and punctuation.
     - Splits the text into words.
     - Applies stemming to each word using the Porter Stemmer.
     - Removes duplicates and sorts the list of tokens.
     - Joins the tokens into a string.

3. **`generate_cleaned_column(df)`**:
   - Sorts the DataFrame by the 'fingerprint' and 'text' columns.
   - For each unique fingerprint, the first corresponding 'text' value is retained.
   - Creates a new column called 'cleaned', mapping fingerprints to their respective text values.

4. **`save_data(df, output_file)`**:
   - Saves the cleaned text data in the output file, with a column named 'text'.

5. **`main(input_file, output_file)`**:
   - Orchestrates the entire data cleaning process by calling the previous functions.
