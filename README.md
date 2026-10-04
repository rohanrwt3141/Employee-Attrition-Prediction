# Employee Attrition Prediction

A Machine Learning project that predicts whether an employee is likely to leave an organization based on various employee-related factors.

The project includes **data cleaning, preprocessing, exploratory data analysis, machine learning model training, evaluation, and a Streamlit web application** for interactive predictions and visualization.

## 🚀 Project Overview

Employee attrition is an important problem for organizations because losing experienced employees can increase recruitment and training costs.

This project uses Machine Learning to analyze employee data and predict the likelihood of employee attrition.

The trained model is integrated with a **Streamlit application**, allowing users to enter employee information and receive a prediction through an interactive interface.

## ✨ Features

* Data cleaning and preprocessing
* Handling missing values
* Exploratory Data Analysis (EDA)
* Data visualization
* Feature preprocessing
* Machine Learning model training
* Model evaluation
* Employee attrition prediction
* Interactive Streamlit web application
* User-friendly input interface
* Prediction results and visualizations

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries & Frameworks

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit
* Joblib

### Tools

* Jupyter Notebook
* PyCharm
* VS Code
* Git & GitHub

## 📂 Project Structure

```text
Employee-Attrition-Prediction/
│
├── app.py
├── Employee_Attrition.ipynb
│
├── model/
│   └── Employee_Attrition_Prediction.pkl
│
├── data/
│   └── README.md
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔄 Machine Learning Workflow

The project follows the following workflow:

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Handling Missing Values
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Data Preprocessing
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model Saving
     ↓
Streamlit Application
     ↓
Employee Attrition Prediction
```

## 📊 Data Preprocessing

The dataset was analyzed and prepared before training the Machine Learning model.

Major preprocessing steps include:

* Identifying missing values
* Handling missing values
* Removing duplicate records
* Detecting and handling inconsistent data
* Encoding categorical variables
* Scaling numerical features where required
* Separating features and target variable

## 🤖 Machine Learning Model

A Machine Learning classification model is trained using employee-related features.

The trained model is saved using **Joblib** and loaded into the Streamlit application for making predictions.

```python
import joblib

model = joblib.load("model/Employee_Attrition_Prediction.pkl")
```

## 🌐 Streamlit Application

The Streamlit application provides an interactive interface where users can enter employee information.

The application then processes the input using the same preprocessing pipeline used during model training and generates an attrition prediction.

To run the application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 📈 Visualization

The application can also provide visual insights into the employee dataset, helping users understand patterns and relationships between different employee attributes and attrition.

Possible visualizations include:

* Attrition distribution
* Age distribution
* Salary distribution
* Department-wise attrition
* Job satisfaction analysis
* Correlation analysis
* Feature importance

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/employee-attrition-prediction.git
```

### 2. Navigate to the project directory

```bash
cd employee-attrition-prediction
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

#### Linux/macOS

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

## 📦 Requirements

The main dependencies used in this project include:

```text
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
joblib
```

A complete list of dependencies is available in `requirements.txt`.

## 🎯 Learning Outcomes

Through this project, I explored:

* Data preprocessing
* Missing-value handling
* Exploratory Data Analysis
* Data visualization
* Feature engineering
* Classification algorithms
* Model evaluation
* Model serialization using Joblib
* Building ML applications using Streamlit
* Deploying Machine Learning models into an interactive application

## 🔮 Future Improvements

Some possible improvements include:

* Hyperparameter tuning
* Comparing multiple Machine Learning models
* Improving model performance
* Adding more interactive visualizations
* Adding feature importance explanations
* Deploying the application online
* Adding probability/confidence scores
* Improving UI/UX

## 👨‍💻 Author

**Rohan Singh Rawat**

B.Tech Artificial Intelligence & Machine Learning
COER University, Roorkee

### Connect with me

* GitHub: https://github.com/YOUR_USERNAME
* LinkedIn: https://www.linkedin.com/in/rohan-rawat-5a930037b

## ⭐ If you found this project useful

Consider giving the repository a ⭐ on GitHub!
