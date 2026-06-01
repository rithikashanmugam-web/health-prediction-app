import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

data = {
    "glucose": [90, 130, 100, 160, 80, 140, 95],
    "haemoglobin": [13, 12, 10, 11, 14, 12, 13],
    "cholesterol": [170, 220, 180, 250, 160, 240, 175],
    "result": [
        "Healthy",
        "Diabetes Risk",
        "Anemia Risk",
        "High Cholesterol Risk",
        "Healthy",
        "Diabetes Risk",
        "Healthy"
    ]
}

df = pd.DataFrame(data)

X = df[["glucose", "haemoglobin", "cholesterol"]]
y = df["result"]

model = DecisionTreeClassifier()

model.fit(X, y)

pickle.dump(
    model,
    open("models/health_model.pkl", "wb")
)

print("Model saved successfully")