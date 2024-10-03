# Customer Churn Prediction Project
![GitHub](https://img.shields.io/github/license/willianadb/gold_purification_prediction)

## 📄 Project Description
This project aims to predict customer churn for a telecommunications company using machine learning techniques. Accurately identifying customers likely to cancel services allows the company to implement proactive strategies to retain customers and improve satisfaction.

The work was developed in two versions: Portuguese and English, aiming to reach an international audience. The project includes an exploratory data analysis, the application of various predictive models, and hyperparameter tuning to achieve the best performance.

## 📂 Project Structure
- `data/`: Directory containing raw and processed data.
  - `raw/`: Original data files.
  - `processed/`: Data after preprocessing.
- `notebooks/`: Jupyter Notebooks containing analysis, modeling, and evaluation.
  - `portuguese/`: Notebook version in Portuguese.
  - `english/`: Notebook version in English.
- `scripts/`: Python scripts for data preprocessing, training, and model evaluation.
  - `portuguese/`
  - `english/`
- `models/`: Trained models saved for future use.
  - `portuguese/`
  - `english/`
- `docs/`:
  - [README_en.md](docs/README_en.md): Project documentation in English (you are here).
  - [README_pt.md](docs/README_pt.md): Project documentation in Portuguese.
  
## 📊 Exploratory Data Analysis
Exploratory Data Analysis (EDA) was performed to better understand the data and identify patterns that may influence customer churn. Some of the analyses included:
- Distribution of categorical and numerical variables.
- Correlation analysis to identify significant relationships between variables.
- Study of the distribution of customers who canceled and retained the service.

## ⚙️ Preprocessing
The `preprocess_data.py` script performs the following data preparation steps:
- Conversion of column names to `snake_case` format.
- Merging multiple data files (`contract.csv`, `personal.csv`, `internet.csv`, `phone.csv`).
- Handling of missing values.
- Encoding of categorical variables using One-Hot Encoding.
- Normalization of numerical variables.
- Creation of the target variable and relevant new features.

## 🧠 Predictive Modeling
Several machine learning models were trained and evaluated, including:
- Logistic Regression.
- Decision Trees.
- Random Forest.
- Gradient Boosting.
- XGBoost.
- LightGBM.

### 🛠️ Hyperparameter Tuning
The most promising models were **XGBoost**, which achieved an AUC-ROC of 0.9113 **without the need for hyperparameter tuning**, followed by the tuned Gradient Boosting with an AUC-ROC of 0.902170. Hyperparameter tuning was performed using `RandomizedSearchCV` and `GridSearchCV`.

## 📈 Evaluation and Results
The best model selected was **XGBoost**, achieving an AUC-ROC of 0.9113. Evaluation metrics, such as accuracy, precision, recall, and f1-score, were analyzed for each model, highlighting the effectiveness of the final model.

## 🚀 Next Steps and Final Considerations
- **Production Deployment:** The model is ready to be deployed in production for real-time churn prediction.
- **Monitoring:** Continuous monitoring of the model's performance with new data is suggested.
- **Future Adjustments:** Further hyperparameter tuning and feature engineering can be performed to improve the model's performance.

## 📂 How to Run the Project
1. Clone this repository: `git clone https://github.com/willianadb/telecom_customer_churn_prediction.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Navigate to the `notebooks` folder and run the desired version (`portuguese` or `english`). It is recommended to start with the Exploratory Data Analysis (`EDA`) before proceeding to modeling.
4. The preprocessing and modeling scripts can be found in the `scripts` folder.

## 📋 Requirements
- Python 3.x
- Libraries: `pandas`, `numpy`, `sklearn`, `xgboost`, `lightgbm`, `matplotlib`, `seaborn`, `joblib`, among others (see `requirements.txt`).

## 🧑‍💼 Author
This project was developed by **Willian Albuquerque**, a data scientist and machine learning specialist. I am available for consultations and projects related to this topic.
