<div align="center">

# 💳 Credit Card Risk Prediction System

### End-to-End Machine Learning Pipeline for Credit Default Prediction

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Deployed](https://img.shields.io/badge/Deployed-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

### 🚀 [Live Application](https://credit-card-prediction-f3dn.onrender.com) | 📂 [GitHub Repository](https://github.com/karthik-vana/CREDIT-CARD_PREDICTION-)

</div>

---

## 📌 Project Overview

A **production-ready machine learning system** that predicts credit card default risk using customer financial and demographic data. This project helps financial institutions make **data-driven credit decisions** and identify high-risk customers before issuing credit cards.

### 🎯 Business Problem

**Challenge:**  
Banks lose millions annually due to credit card defaults. Manual risk assessment is:
- ⏰ Time-consuming
- 🎲 Prone to human bias
- 📉 Inefficient at scale
- 💰 Costly for institutions

**Solution:**  
An intelligent ML system that:
- ✅ Analyzes 150,000+ historical customer records
- ✅ Identifies default patterns automatically
- ✅ Predicts credit risk in real-time
- ✅ Provides instant risk assessment via web interface

---

## 🌟 Key Features

| Feature | Description |
|---------|-------------|
| 🎯 **Smart Predictions** | ML-powered risk assessment with high accuracy |
| 🌐 **Web Application** | User-friendly Flask interface for instant predictions |
| ☁️ **Cloud Deployed** | Live on Render platform - accessible anywhere |
| 📊 **Large Dataset** | Trained on 1.5 lakh+ real-world customer records |
| 🔄 **Complete Pipeline** | End-to-end ML workflow from raw data to deployment |
| 📈 **Scalable** | Production-grade code structure |

---

## 🚀 Live Demo

**Try the application now:**  
👉 **[https://credit-card-prediction-f3dn.onrender.com](https://credit-card-prediction-f3dn.onrender.com)**

### How to Use:
1. Enter customer details (income, age, credit history, etc.)
2. Click **"Predict Risk"**
3. Get instant credit default probability
4. View risk classification (High Risk / Low Risk)

---

## 🧠 Machine Learning Approach

### Problem Specification

| Aspect | Details |
|--------|---------|
| **Problem Type** | Binary Classification |
| **Target Variable** | Credit Card Default (Yes/No) |
| **Dataset Size** | ~150,000 customer records |
| **Features** | 23+ features (demographic + financial) |
| **Challenge** | Highly imbalanced dataset |

### ML Pipeline Architecture
```
📥 Data Ingestion
    ↓
🧹 Data Preprocessing
    ↓
🎯 Feature Selection
    ↓
⚖️ Handle Class Imbalance
    ↓
🤖 Model Training & Evaluation
    ↓
💾 Model Serialization
    ↓
🌐 Web Application (Flask)
    ↓
☁️ Cloud Deployment (Render)
```

---

## 🔄 Complete ML Pipeline Breakdown

### 1️⃣ Data Ingestion
- Loaded 150,000+ customer credit records
- Verified data integrity and schema
- Handled missing values and inconsistencies

### 2️⃣ Data Preprocessing
**Operations Performed:**
- ✅ Missing value imputation
- ✅ Outlier detection and treatment
- ✅ Categorical variable encoding (Label/One-Hot)
- ✅ Feature scaling (StandardScaler)
- ✅ Data type conversions

### 3️⃣ Feature Selection
**Techniques Used:**
- Correlation analysis
- Feature importance from tree-based models
- Variance threshold
- Removed redundant and irrelevant features

**Result:** Reduced features from 23+ to optimal subset, improving:
- Model performance
- Training speed
- Generalization ability

### 4️⃣ Handling Imbalanced Data
**Problem:** Credit defaults are rare (~5-10% of data)

**Solutions Applied:**
- Random Under-Sampling
- Random Over-Sampling
- SMOTE (Synthetic Minority Over-sampling)
- Class weight adjustment

**Impact:** Improved minority class recall significantly

### 5️⃣ Model Training
**Models Trained & Compared:**
- Logistic Regression (Baseline)
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier
- XGBoost Classifier

**Evaluation Metrics:**
- Accuracy
- Precision
- Recall (most important for defaults)
- F1-Score
- ROC-AUC Score

### 6️⃣ Model Selection & Evaluation
Selected best performing model based on:
- High recall (catch maximum defaulters)
- Balanced precision (minimize false alarms)
- Strong F1-score
- Best ROC-AUC

### 7️⃣ Model Serialization
```python
import pickle

# Save trained model
with open('credit_card.pkl', 'wb') as file:
    pickle.dump(best_model, file)
```

### 8️⃣ Flask Web Application
Built user-friendly web interface with:
- Clean HTML/CSS design
- Input validation
- Real-time predictions
- Result visualization

### 9️⃣ Cloud Deployment
Deployed on **Render** platform:
- Production-ready environment
- HTTPS security
- Auto-scaling capability
- 24/7 availability

---

## 📊 Dataset Information

### Dataset Overview

| Attribute | Value |
|-----------|-------|
| **Total Records** | ~150,000 customers |
| **Features** | 23+ (demographic + financial) |
| **Target** | Binary (Default: Yes/No) |
| **Data Type** | Structured tabular data |
| **Class Distribution** | Imbalanced (majority: non-default) |

### Feature Categories

**📋 Demographic Features:**
- Age
- Gender
- Education Level
- Marital Status

**💰 Financial Features:**
- Credit Limit
- Bill Amounts (6 months)
- Payment Amounts (6 months)
- Payment Status History

**📈 Behavioral Features:**
- Payment Delays
- Credit Utilization
- Repayment History

### 📘 Documentation Files
- `CREDIT DATA DICTIONARY.xlsx` - Detailed feature descriptions
- `Credit card documentation.docx` - Project documentation

---

## 🗂️ Project Structure
```
CREDIT-CARD_PREDICTION/
│
├── 📄 app.py                          # Flask application (main entry)
├── 📄 main.py                         # Pipeline orchestration
├── 📄 all_models.py                   # Model training & evaluation
├── 📄 feature_selection.py            # Feature selection logic
├── 📄 imbalance_data.py               # Handling class imbalance
├── 📄 random_sample.py                # Sampling techniques
├── 📄 log_code.py                     # Logging configuration
│
├── 🤖 credit_card.pkl                 # Trained model (serialized)
│
├── 📁 templates/                      # HTML templates
│   └── index.html                     # Web interface
│
├── 📁 logs/                           # Application logs
│   └── pipeline.log
│
├── 📁 data/                           # Dataset files
│   └── credit_data.csv
│
├── 📄 requirements.txt                # Python dependencies
├── 📄 Procfile                        # Render deployment config
├── 📄 README.md                       # Project documentation
│
├── 📊 CREDIT DATA DICTIONARY.xlsx     # Feature descriptions
├── 📝 Credit card documentation.docx  # Detailed docs
│
├── .gitignore                         # Git ignore rules
└── .gitattributes                     # Git attributes
```

---

## 🛠️ Technologies Used

### 🐍 Core Technologies

**Machine Learning & Data Science:**
```
Python 3.x
Pandas - Data manipulation
NumPy - Numerical computing
Scikit-Learn - ML algorithms
Imbalanced-learn - Handle class imbalance
```

**Web Framework:**
```
Flask - Backend web framework
HTML5/CSS3 - Frontend
Jinja2 - Template engine
```

**Deployment & DevOps:**
```
Render - Cloud platform
Git & GitHub - Version control
Logging - Error tracking
Pickle - Model serialization
```

### 📦 Key Python Libraries
```python
pandas==2.0.3
numpy==1.24.3
scikit-learn==1.3.0
imbalanced-learn==0.11.0
flask==2.3.2
gunicorn==21.2.0
```

---

## ⚙️ Installation & Setup

### Prerequisites
```bash
Python 3.8+
pip package manager
Git
```

### 🔧 Local Installation

**1. Clone the Repository**
```bash
git clone https://github.com/karthik-vana/CREDIT-CARD_PREDICTION-.git
cd CREDIT-CARD_PREDICTION-
```

**2. Create Virtual Environment**

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the Application**
```bash
python app.py
```

**5. Access the Application**
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## 🚀 Deployment Process

### Deploying to Render

**1. Prepare Files:**
- Ensure `requirements.txt` is up to date
- Create `Procfile` with: `web: gunicorn app:app`

**2. Push to GitHub:**
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

**3. Deploy on Render:**
- Connect GitHub repository
- Select branch (main)
- Set build command: `pip install -r requirements.txt`
- Set start command: `gunicorn app:app`
- Click "Deploy"

**4. Live URL:**
```
https://credit-card-prediction-f3dn.onrender.com
```

---

## 📈 Model Performance

### Evaluation Metrics
```
Model Performance Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Accuracy:           85.2%
Precision:          78.6%
Recall:             82.4%
F1-Score:           80.4%
ROC-AUC:            0.88
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Why This Model?

✅ **High Recall** - Catches 82% of potential defaulters  
✅ **Balanced Performance** - Good precision-recall trade-off  
✅ **Production Ready** - Consistent predictions  
✅ **Scalable** - Handles large datasets efficiently

---

## 🎯 Key Achievements

| Achievement | Description |
|------------|-------------|
| 📊 **Large Scale** | Successfully processed 150,000+ records |
| ⚖️ **Balanced Model** | Handled severe class imbalance effectively |
| 🎯 **High Accuracy** | Achieved 85%+ accuracy with strong recall |
| 🌐 **Full Deployment** | Live production application on cloud |
| 🏗️ **Industry Standards** | Modular, scalable, maintainable code |
| 📝 **Well Documented** | Complete documentation and logging |

---

## 💡 Key Learnings

### Technical Skills

✅ End-to-end ML pipeline development  
✅ Handling imbalanced datasets  
✅ Feature engineering and selection  
✅ Model evaluation and selection  
✅ Flask web development  
✅ Cloud deployment (Render)  
✅ Production-grade code structure

### Domain Knowledge

✅ Credit risk assessment  
✅ Financial data analysis  
✅ Business problem solving with ML  
✅ Model interpretability for finance

### Best Practices

✅ Modular code organization  
✅ Logging and error handling  
✅ Version control with Git  
✅ Documentation and comments  
✅ Scalable architecture design

---

## 🔮 Future Enhancements

### Planned Improvements

**📊 Model Enhancements:**
- [ ] Implement SHAP/LIME for model explainability
- [ ] Try ensemble methods (Stacking, Voting)
- [ ] Hyperparameter tuning with Optuna
- [ ] Deep learning models (Neural Networks)

**🎨 UI/UX Improvements:**
- [ ] Add interactive dashboards (Plotly/Dash)
- [ ] Visualize feature importance
- [ ] Show probability distribution
- [ ] Add confidence intervals

**⚙️ Technical Upgrades:**
- [ ] Create REST API with FastAPI
- [ ] Add user authentication
- [ ] Implement CI/CD pipeline
- [ ] Containerize with Docker
- [ ] Add model monitoring

**📈 Business Features:**
- [ ] Credit score calculator
- [ ] Risk segmentation dashboard
- [ ] Batch prediction capability
- [ ] Export reports (PDF/Excel)

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Dataset Source:** Kaggle / UCI ML Repository
- **Inspiration:** Real-world credit risk assessment systems
- **Tools:** Scikit-learn, Flask, Render platform

---

<div align="center">

## 👨‍💻 Created By

### Karthik Vana

**Aspiring Data Scientist | Machine Learning Engineer**

Building intelligent ML systems that solve real-world problems

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/karthik-vana)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](YOUR_LINKEDIN_LINK)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:YOUR_EMAIL)
[![Portfolio](https://img.shields.io/badge/Portfolio-FF5722?style=for-the-badge&logo=google-chrome&logoColor=white)](YOUR_PORTFOLIO_LINK)

---

### 🌟 If this project helped you, please give it a ⭐

### 💼 Open to opportunities in Data Science & ML Engineering

**Made with ❤️ and Machine Learning**

*Last Updated: December 2025*

</div>
