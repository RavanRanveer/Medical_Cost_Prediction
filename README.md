# Medical Expenditure Predictor

The **Medical Expenditure Predictor** is a machine learning application that estimates out-of-pocket medical expenses based on user-provided demographic, health, and insurance-related information. The application integrates an intuitive front-end interface, a trained machine learning model, and Object-Relational Mapping (ORM) for efficient database management.

---

## Features

- **Prediction Model**: Uses a trained XGBoost model to predict medical expenses.
- **Streamlit Interface**: A user-friendly application for data input and predictions.
- **ORM Implementation**: Efficient database interaction using SQLAlchemy.
- **Jupyter Notebook**: Contains the model training process for transparency and further experimentation.
- **Dataset Included**: A structured dataset used for training and testing is provided.

---

## Repository Structure
medical-expenditure-predictor/
│
├── app.py                 # Streamlit app for prediction
├── model/
│   ├── xgboost_model.json  # Trained XGBoost model
│   ├── preprocessor.pkl    # Preprocessor used for the model
│
├── orm/
│   ├── orm_code.py         # ORM implementation with SQLAlchemy
│
├── notebook/
│   ├── model_training.ipynb # Jupyter Notebook for model training
│
├── data/
│   ├── dataset.csv          # Original dataset used for training
│   ├── sample_data.csv      # Sample data (optional for demonstration)
│
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation

---

## Setup Instructions

### Prerequisites

- Python 3.8 or above
- Google SQL instance or MySQL database
- Installed dependencies (see `requirements.txt`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/medical-expenditure-predictor.git
   cd medical-expenditure-predictor

2.	Install dependencies:
   ```bash
   pip install -r requirements.txt

3.	Set up the database:
	•	Configure your MySQL or Google SQL instance.
	•	Update the connection details in orm/orm_code.py.
4.	Add model files:
	•	Place xgboost_model.json and preprocessor.pkl in the model/ directory.



   
