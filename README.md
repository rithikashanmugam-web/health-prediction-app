# Health Prediction Application

## Project Overview

This project was developed as part of the Technical Assessment (Task 1) for the Junior AI/ML Developer role at Gokul Infocare.

The application helps manage patient blood test records and predicts possible health conditions using a machine learning model.

The system stores patient details such as:

- Full Name
- Date of Birth
- Email Address
- Glucose
- Haemoglobin
- Cholesterol
- Remarks (AI-generated prediction)

Based on blood test values entered by the user, the machine learning model predicts a possible health condition and automatically displays it in the Remarks field.

---

## Features

### CRUD Operations

- Add new patient record
- View all patient records
- Update patient details
- Delete patient records

### AI/ML Prediction

Predicts health condition using blood values:

- Healthy
- Diabetes Risk
- Anemia Risk
- High Cholesterol Risk

### Data Storage

- SQLite database used for persistent storage

### User Interface

- Simple and user-friendly interface
- Built using HTML and Bootstrap

---

## Tech Stack

### Backend
- Python
- Flask

### Frontend
- HTML
- Bootstrap

### Database
- SQLite

### Machine Learning
- Scikit-learn
- Decision Tree Classifier

---

## Project Structure

```bash
health-prediction-app/
│
├── app.py
├── model.py
├── database.db
├── requirements.txt
├── README.md
├── health_model.pkl
│
├── templates/
│   ├── index.html
│   ├── add.html
│   └── edit.html
│
└── static/
    └── style.css
```

---

## Installation

Clone repository:

```bash
git clone <repository-link>
```

Move to project folder:

```bash
cd health-prediction-app
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Machine Learning Model

Train and generate model:

```bash
python model.py
```

---

## Run Application

Start Flask application:

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

## Workflow

1. User enters patient details
2. Blood values are validated
3. Machine learning model predicts possible health condition
4. Prediction displayed in Remarks field
5. Record stored in SQLite database
6. User can edit or delete records

---

## Challenges Faced

- Connecting machine learning model with Flask backend
- Storing predictions automatically in database
- Implementing CRUD operations with SQLite
- Organizing templates and project structure

---

## Future Improvements

- Use real medical dataset
- Add authentication/login
- Improve prediction accuracy with larger dataset
- Deploy application online
- Add charts and analytics dashboard

---

## Author

Rithika S
B.Tech - Artificial Intelligence and Machine Learning
