# Exoplanet Classification Project

<p align="center">
	<img src="./data/Exoplanets.jpg" alt="image01" width="1000">
</p>

## Overview

This project focuses on predicting whether a celestial body is an exoplanet candidate or not using machine learning models. The data used for this project is sourced from the Caltech website and is dated back to 2018.

## Data Analysis, Cleaning, and Model Building

In this Jupyter Notebook, we perform a comprehensive analysis of the dataset, which includes exploration, handling missing values, and addressing outliers. Following data preparation, we proceed to build and evaluate machine learning models for predicting exoplanet candidates.

### Models Used

1. **Logistic Regression**
2. **Decision Tree Classifier**
3. **K-Nearest Neighbors (KNN) Classifier**
4. **Random Forest Classifier**

### Steps

- **Model Creation:** Each model is created and trained using the prepared dataset.
  
- **Model Evaluation:** The ROC curve and confusion matrix are utilized to assess the performance of each model. Additionally, we extract important feature columns to understand the key predictors.

## Model Comparison

The models are ranked based on their accuracy scores:

1. **Random Forest Classifier and Logistic Regression (98% Accuracy)**
2. **Decision Tree Classifier (96% Accuracy)**
3. **K-Nearest Neighbors (KNN) Classifier (79% Accuracy)**

The RandomForest and Logistic Regression models demonstrated superior accuracy in predicting exoplanet candidates.

## Project Structure

The project structure includes the following files:

- `exoplanet_classification.ipynb`: Jupyter Notebook containing both the data analysis and model building.

## Requirements

- Python 3.x
- Jupyter Notebook
- Required Python libraries (NumPy, Pandas, Matplotlib, Scikit-Learn)

## Usage

To reproduce the analysis and train the models:

1. Open `exoplanet_classification.ipynb` in Jupyter Notebook and run the cells sequentially.

Feel free to explore and modify the code to suit your specific needs.

## Conclusion

This project showcases the application of machine learning models for exoplanet classification, providing insights into the performance and predictive capabilities of different algorithms.

