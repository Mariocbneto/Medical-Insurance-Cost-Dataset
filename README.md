# Medical Insurance Cost Analysis

This project explores a dataset containing medical insurance cost information for individuals in the United States.  
It includes data cleaning, exploratory analysis, visualization, and a predictive model using Machine Learning.

**Dataset:** [Medical Insurance Cost Dataset](https://www.kaggle.com/datasets/mosapabdelghany/medical-insurance-cost-dataset/data)

---
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://medical-insurance-cost-dataset-jvq2dwcqwxgloq9wlcfcgm.streamlit.app/) < - - - - Open

<img width="1158" height="652" alt="POWERBI" src="https://github.com/user-attachments/assets/11a4a21c-b2a2-4eae-9839-659d8ccd4c5a" />

## Project Overview

The goal of this project is to:

- Analyze medical insurance costs based on demographic and health-related factors
- Explore how variables such as smoking status, BMI, and number of children affect insurance costs
- Build a predictive model to estimate individual insurance charges
- Extract actionable insights from the data
- Create visual dashboards for interactive data exploration

---

## Insights

- The **average annual insurance cost** in the dataset is approximately **$13,279**.
- **Smokers** pay significantly more than non-smokers, showing a strong correlation between smoking and higher insurance costs.
- **BMI** influences costs: individuals categorized as obese tend to have higher insurance charges compared to normal or underweight categories.
- The **number of children** covered in the insurance plan also affects costs, although some anomalies exist (e.g., families with 5 children paying less than families with 2–3 children).
- Machine Learning using **Random Forest Regression** achieved an **R² score of 0.88** with a **root mean squared error (RMSE) of $4,702**, indicating strong predictive performance.

---

## Visualizations

- **Bar Charts**
  - Average insurance cost by BMI category
  - Average insurance cost by number of children
- **Scatter Plots**
  - Age vs. insurance cost with smoking status as hue
- **Cards / KPI**
  - Average monthly insurance cost
  - Average monthly cost for smokers
  - Average monthly cost for non-smokers
- **Predictions**
  - ML model predicts individual insurance costs based on user features

---

## Tools and Technologies Used

- **Python** – data processing and analysis  
- **Pandas** – data manipulation and cleaning  
- **Matplotlib & Seaborn** – data visualization  
- **Scikit-learn** – machine learning (Random Forest Regression)  
- **Jupyter Notebook** – interactive coding and exploration  
- **Power BI** – interactive dashboards  
- **Streamlit** – web-based dashboard for sharing ML predictions  
- **Git & GitHub** – version control and project sharing  

---

## How to Run the Code

1. Clone the repository:

```bash
git clone https://github.com/Mariocbneto/Medical-Insurance-Cost-Dataset.git
cd Medical-Insurance-Cost-Dataset
pip install -r requirements.txt
streamlit run insurance_dashboard.py
