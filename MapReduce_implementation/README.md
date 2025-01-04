MapReduce Word Count in Python

Description

This project implements a simplified MapReduce pipeline in Python to perform a word count on text files. The program processes all .txt files in a specified input directory, tokenizes the text, counts word occurrences, and outputs the results to a specified output directory.

Features

Reads multiple .txt files from a directory.

Tokenizes text and normalizes words (removes punctuation and converts to lowercase).

Counts occurrences of each word.

Saves the results to an output file in a new directory.

Requirements

Python 3.6+

Standard Python libraries: os, glob, fileinput