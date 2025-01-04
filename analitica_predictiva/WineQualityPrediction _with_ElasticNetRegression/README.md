# Wine Quality Prediction with ElasticNet Regression

This project implements a workflow for training, evaluating, and selecting the best regression model based on ElasticNet to predict wine quality using the UCI Red Wine Quality dataset.

## Project Description

The primary objective is to predict wine quality based on its chemical properties. The ElasticNet model combines L1 (Lasso) and L2 (Ridge) penalties. The workflow includes hyperparameter tuning and cross-validation to optimize the model's performance.

## Project Structure

### Key Features
1. **Data Loading**:
   - The dataset is downloaded from the [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv).
   - The data includes chemical properties and wine quality ratings.

2. **Model Training**:
   - ElasticNet is used as the regression model.
   - Models are evaluated using metrics:
     - Mean Squared Error (MSE)
     - Mean Absolute Error (MAE)
     - R² Score

3. **Best Model Management**:
   - The best model is saved as a `.pickle` file.
   - Each trained model is compared against the best saved model, and updates are made if necessary.

4. **Hyperparameter Tuning**:
   - `GridSearchCV` is implemented to explore combinations of hyperparameters (`alpha`, `l1_ratio`) with cross-validation.

### Code Structure
- **`load_data()`**: Loads and splits the dataset into features (`x`) and target (`y`).
- **`make_train_test_split()`**: Splits data into training and testing sets.
- **`train_estimator()`**: Trains and evaluates the model with provided hyperparameters.
- **`check_estimator()`**: Verifies the performance of the best saved model.
- **`make_hyperparameters_search()`**: Explores hyperparameter combinations.
- **`save_best_estimator()` and `load_best_estimator()`**: Save and load the best model.

## Requirements

Make sure you have the following packages installed:
- Python 3.8+
- Pandas
- NumPy
- Scikit-learn