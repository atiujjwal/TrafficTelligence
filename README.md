# 🚦 PredictPath

### Advanced Traffic Volume Estimation with Machine Learning

**PredictPath** is a machine learning-based system designed to predict traffic volume with high accuracy. By integrating multiple data sources—including weather conditions, historical traffic patterns, and holiday data—it provides actionable insights for commuters and city planners.

This project uses a **Flask** web application with a **Gamified "Command Center" UI** to visualize predictions in real-time.

---

## 🌟 Key Features

- **Machine Learning Prediction:** Uses advanced algorithms (Random Forest / XGBoost) to estimate traffic volume based on complex variables.
- **Immersive 3D Interface:** A gamified "Command Center" featuring a 3D moving road, animated vehicles, and glassmorphism styling.
- **Dynamic Environment:**
  - **Day/Night Cycle:** Background and lighting change based on the input time.
  - **Weather Effects:** Visual rain, snow, fog, and cloud animations based on selected weather conditions.
- **Smart Inputs:**
  - Unified Date/Time picker (auto-parsed for ML features)
  - Input validation using scientific units (Kelvin for temp, mm for rain/snow)
- **Data-Driven:** Considers holidays (Thanksgiving, Christmas) and weather details (mist, haze, thunderstorm) for accurate estimation.

---

## 🛠️ Tech Stack

| Layer            | Technologies                        |
| ---------------- | ----------------------------------- |
| Frontend         | HTML5, CSS3, JavaScript             |
| Backend          | Python, Flask                       |
| Machine Learning | Scikit-Learn, Pandas, Numpy, Pickle |
| Development      | Jupyter Notebook                    |

---

## ⚙️ Installation & Setup

> The `model.pkl` and `scaler.pkl` files must be generated locally. Follow these steps **in order**.

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/PredictPath.git
cd PredictPath
```

### Step 2: Create a Virtual Environment (Recommended)

#### Windows

python -m venv venv
venv\Scripts\activate

#### Mac/Linux

python3 -m venv venv
source venv/bin/activate

### Step 3: Install Dependencies

Flask
pandas
numpy
scikit-learn
matplotlib
seaborn
xgboost
joblib
jupyter

#### Then install:

pip install -r requirements.txt

### Step 4: Generate Model Files (Mandatory)

**Since model.pkl and scaler.pkl are not uploaded due to size limits:**

```bash
cd model
jupyter notebook model.ipynb
```

-**Run All Cells:** This will train the model using traffic.csv
_Confirm model.pkl and scaler.pkl are created._

-Return to project root:

```bash
cd ..
```

### Step 5: Run the Application

python app.py

### Project Structure

```bash
PredictPath/
├── media/
│   ├── PredictPath Empathy Map.png
│   └── assets/
├── static/
│   ├── index.css
│   └── assets/
├── templates/
│   ├── index.html
├── model/
│   ├── The_Model.ipynb
│   ├── model.pkl
│   ├── scaler.pkl
│   └── trafficVolumeData.csv
├── app.py
├── requirements.txt
└── README.md
```
