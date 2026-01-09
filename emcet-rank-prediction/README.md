# EMCET Rank Prediction

## 📌 Project Oveview
This project aims to predict the rank of a student in the EMCET examination based on various background and academic factors. It utilizes machine learning algorithms to provide an estimated rank, helping students understand their potential standing.

## 🎯 Objective
- To analyze historical data of students and their ranks.
- To build a predictive model that estimates a student's rank with high accuracy.
- To identify key factors contributing to better performance.

## 🧠 Concepts & Tech Stack
- **Machine Learning:** Regression Analysis, Random Forest, XGBoost
- **Data Preprocessing:** Label Encoding, Feature Scaling
- **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, Joblib

## 📂 Dataset
The dataset includes student details such as:
- Mock test scores
- Previous academic records
- Demographic information (if applicable)
The processed data is stored in the `data/` directory.

## 🏗️ Approach
1.  **Data Cleaning:** Handling missing values and outliers.
2.  **Feature Engineering:** Encoding categorical variables using LabelEncoder.
3.  **Model Selection:** Evaluated Random Forest and XGBoost.
4.  **Training:** The `XGBoost` model showed the best performance and was saved as `xgb_model.pkl`.
5.  **Evaluation:** Metrics like MAE (Mean Absolute Error) and RMSE were used to validate the model.

## 📊 Results
- The **Random Forest** model achieved robust baseline performance.
- The **XGBoost** model further optimized the prediction accuracy.
- Key predictors identified: Mock test scores and intermediate percentages.

## 🚀 How to Run
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Navigate to `notebooks/` and run the Jupyter Notebook to see the training process or run inference.

## 🔮 Future Improvements
- Deploy the model as a web application (Flask/Streamlit).
- Integrate more granular data points like study hours.
