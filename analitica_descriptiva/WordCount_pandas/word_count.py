import glob

import pandas as pd


def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    filenames = glob.glob(f"{input_directory}/*.txt")

    dataframes = [
        pd.read_csv(filename, sep="\t", header=None, names=["text"])
        for filename in filenames
    ]

    concatenated_df = pd.concat(dataframes, ignore_index=True)

    return concatenated_df


def clean_text(dataframe):
    """Text cleaning"""
    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].str.lower()
    dataframe["text"] = dataframe["text"].str.replace(".", "")
    dataframe["text"] = dataframe["text"].str.replace(",", "")
    return dataframe


def count_words(dataframe):
    """Word count"""
    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].str.split()
    dataframe = dataframe.explode("text")
    dataframe["count"] = 1
    dataframe = dataframe.groupby("text", as_index=False).agg({"count": "sum"})
    return dataframe


def count_words2(dataframe):
    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].str.split()
    dataframe = dataframe.explode("text")
    dataframe = dataframe["text"].value_counts()
    return dataframe


def save_output(dataframe, output_filename):
    """Save output to a file."""
    dataframe.to_csv(output_filename, sep="\t", index=True, header=False)


def run(input_directory, output_filename):
    """Call all functions."""
    df = load_input(input_directory)
    df = clean_text(df)
    df = count_words2(df)
    save_output(df, output_filename)


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
