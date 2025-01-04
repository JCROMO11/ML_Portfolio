# Digit Classification with Logistic Regression

This project implements a basic digit classification task using the Logistic Regression model. The dataset used is the [Scikit-learn Digits dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_digits_last_image.html), which consists of 8x8 pixel grayscale images of handwritten digits (0-9).

## Project Overview

- **Dataset**: Scikit-learn's Digits dataset
- **Model**: Logistic Regression
- **Libraries**: 
  - Scikit-learn
  - Matplotlib
  - Pickle
- **Key Outputs**:
  - Visualizations of sample digits and predictions
  - Model accuracy on training and test datasets
  - Confusion matrix for evaluation
  - Saved Logistic Regression model (`estimator.pkl`)

## Features

- **Exploratory Data Analysis (EDA)**:
  - Visualize individual digits and their labels.
  - Display a grid of digit images.
  
- **Model Training**:
  - Train a Logistic Regression classifier on half of the dataset.
  - Test the model on the other half.

- **Performance Evaluation**:
  - Compute and display the confusion matrix.
  - Visualize prediction probabilities alongside digit images.

- **Model Serialization**:
  - Save the trained model using `pickle`.
  - Load the model for future use.