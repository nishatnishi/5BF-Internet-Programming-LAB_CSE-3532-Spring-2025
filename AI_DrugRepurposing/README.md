# **🧪 AI for Drug Repurposing – Discovering New Uses for Existing Drugs**
An AI-powered system designed to identify potential new applications for existing drugs by leveraging machine learning and open biomedical datasets.

---

## 📌 **About This Project**
**AI for Drug Repurposing** is a cutting-edge project that applies machine learning (ML) techniques to predict whether existing drugs can be repurposed to treat different diseases. This open-source project leverages public datasets like DrugBank, ChEMBL, and PubChem, providing an opportunity to speed up drug discovery and optimize the use of existing medications.

The project begins with a basic ML model and aims to expand to more advanced deep learning techniques in the future.

---

## 👤 **Team Member** 
| 				Name           | Role      | ID        |
|------------------------|-----------|-----------|
| *Sharmin Akter Shorna* | Developer | C231443   |
|    *Trishita Paul*     | Developer | C231471   |

---

## 🛠 **Technologies Used**
### **AI/ML (Backend)**
- Python: Core language for implementing machine learning algorithms
- Pandas & NumPy: For data manipulation and processing
- Scikit-Learn: For implementing machine learning models like Logistic Regression and Decision Trees
- Flask/Django: To expose the trained ML model via an API
- GoLab: For data exploration, testing, and visualizations
### **Web Development (Frontend & Deployment)**
- Django: Web framework for backend development
- HTML, CSS, JavaScript: For frontend user interface
- Bootstrap: To design a clean, responsive user interface
- Chart.js / Plotly: For interactive data visualizations (drug repurposing effectiveness)
- SQLite / PostgreSQL: Database for storing results and queries
- Docker (Optional): For easy deployment
  
---

## 🌟 **Key Features**

- **AI-Powered Drug Repurposing**: Predicts new uses for existing drugs using machine learning models to help identify potential treatments for other diseases.
- **Simple Machine Learning Models**: Initially uses **Logistic Regression** and **Decision Trees** to predict drug repurposing.
- **Public Datasets**: Utilizes open datasets like **DrugBank**, **ChEMBL**, and **PubChem** for training and testing the model.
- **Interactive User Interface**: Allows users to input a drug name or symptoms and see the predicted repurposed drugs.
- **Data Visualization**: Includes **Chart.js** or **Plotly** for visualizing the effectiveness of the repurposed drugs.
- **Customizable and Open-Source**: Open for further improvements and customization for various use cases in drug discovery.

---

## 🚀 **Development Roadmap**

### 📅 **Phase 1 - Initial Model Development**

- **Goal**: Build a basic ML model to predict whether a drug can be repurposed for a different disease.
- **Tasks**:
  - Collect open-source datasets (e.g., DrugBank, ChEMBL, PubChem).
  - Preprocess and clean the data using **Pandas** and **NumPy**.
  - Train a basic machine learning model (e.g., Logistic Regression, Decision Trees) using **Scikit-learn**.
  - Evaluate model performance (Accuracy, Precision, Recall).
  - Build a basic **Django web application** to input drug names and symptoms and display predictions.
  - Visualize the results using **Chart.js** or **Plotly** for a clean and interactive dashboard.

### 📅 **Phase 2 - Advanced Model Development**

- **Goal**: Improve predictions using advanced AI techniques and larger, more complex datasets.
- **Tasks**:
  - Implement **Deep Learning models** like **Transformers** or **Graph Neural Networks** for more accurate drug repurposing predictions.
  - Collect more complex datasets, such as **clinical trial data** and **genetic data**.
  - Validate the model with **medical experts** to improve accuracy and reliability.
  - Write a research paper based on findings and submit to relevant **journals or conferences**.
  - Enhance the web app with additional features such as real-time data processing and user feedback.

### 📅 **Phase 3 - Deployment & Testing**

- **Goal**: Deploy the model and web application for public use.
- **Tasks**:
  - Deploy the Django web app using cloud hosting platforms like **Heroku**, **Vercel**, or **Render**.
  - Test the web application for bugs and performance issues.
  - Add basic **documentation** and tutorials for users to understand how to use the system.

