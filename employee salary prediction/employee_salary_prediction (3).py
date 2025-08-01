# -*- coding: utf-8 -*-
"""employee salary prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qUR4JcKbqOE3d22lxZryQcMWjTeJy2m4
"""

# employee salary prediction using adult csv
# load your library
import pandas as pd

# data=pd.read_csv("/content/adult3.csv")
# data=pd.read_csv(r"/content/adult 3.csv")
data=pd.read_csv("/content/adult 3.csv")

data

data.shape

data.head()

data.head(8)

data.tail(7)

# finding all the null values
data.isna()

data.isna().sum()

data.head(3)

print(data.occupation.value_counts())

print(data.gender.value_counts())

print(data.education.value_counts())

print(data.workclass.value_counts())

print(data['marital-status'].value_counts())

print(data.workclass.value_counts())

data.occupation.replace({'?':'Others'},inplace=True)

print(data.occupation.value_counts())

data.workclass.replace({'?':'Notlisited'},inplace=True)

print(data.workclass.value_counts())

data=data[data['workclass']!='Without-pay']
data=data[data['workclass']!='Never-worked']

print(data.workclass.value_counts())

data.shape

data=data[data['education']!='5th-6th']
data=data[data['education']!='1st-4th']
data=data[data['education']!='Preschool']

print(data.education.value_counts())

data.shape

# redundancy
data.drop(columns=['education'],inplace=True)

data

# outlier
import matplotlib.pyplot as plt
plt.boxplot(data['age'])
plt.show()

data=data[(data['age']<=75) & (data ['age']>=17)]

plt.boxplot(data.age)
plt.show()

plt.boxplot(data['capital-gain'])
plt.show()

# label encoding
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
data['workclass']=encoder.fit_transform(data['workclass'])
data['marital-status']=encoder.fit_transform(data['marital-status'])
data['occupation']=encoder.fit_transform(data['occupation'])
data['relationship']=encoder.fit_transform(data['relationship'])
data['race']=encoder.fit_transform(data['race'])
data['gender']=encoder.fit_transform(data['gender'])
data['native-country']=encoder.fit_transform(data['native-country'])
data

x=data.drop(columns=['income'])
y=data['income']
x

y

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
x=scaler.fit_transform(x)
x

import pandas as pd
print(pd.DataFrame(x).isnull().sum())  # for features
print(pd.Series(y).isnull().sum())     # for target

import pandas as pd

# Combine x and y to drop rows with any missing values
df = pd.concat([pd.DataFrame(x), pd.Series(y, name='target')], axis=1)
df = df.dropna()

# Separate again
x = df.drop('target', axis=1)
y = df['target']

import pandas as pd
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')  # or "median", "most_frequent", etc.
x = imputer.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=23, stratify=y)

x_train

# machine learning algo

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
knn.fit(x_train,y_train)
# input and output training data
predict=knn.predict(x_test)
predict
# predict value

from sklearn.metrics import accuracy_score
accuracy_score(y_test,predict)

"""data -- machine
x and y input and output
xtrain and xtest ytrain and yteest

xtrain and ytrain are used to make the model learn pattern

model prediction
result after evaluation
ytest - key answers - prediction 80 90 99
"""

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)
# input and output training data
predict1=lr.predict(x_test)
predict1

from sklearn.metrics import accuracy_score
accuracy_score(y_test,predict1)

from sklearn.neural_network import MLPClassifier
clf=MLPClassifier(solver='adam',hidden_layer_sizes=(5,2),random_state=2,max_iter=2000)
clf.fit(x_train,y_train)
# input and output training data
predict2=clf.predict(x_test)
predict2

from sklearn.metrics import accuracy_score
accuracy_score(y_test,predict2)

"""input layer -hidden layer-output layer"""

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

models = {
    "LogisticRegression": LogisticRegression(),
    "RandomForest": RandomForestClassifier(),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(),
    "GradientBoosting": GradientBoostingClassifier()
}

results = {}

for name, model in models.items():
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('model', model)
    ])

    pipe.fit(x_train, y_train)
    ypred = pipe.predict(x_test)
    acc = accuracy_score(y_test, ypred)
    results[name] = acc
    print(f"{name} Accuracy: {acc:.4f}")
    print(classification_report(y_test, ypred))

import matplotlib.pyplot as plt

plt.bar(results.keys(), results.values(), color='skyblue')
plt.ylabel('Accuracy Score')
plt.title('Model Comparison')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Define models
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "RandomForest": RandomForestClassifier(),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(),
    "GradientBoosting": GradientBoostingClassifier()
}

results = {}

# Train and evaluate
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    results[name] = acc
    print(f"{name}: {acc:.4f}")

# Get best model
best_model_name = max(results, key=results.get)
best_model = models[best_model_name]
print(f"\n✅ Best model: {best_model_name} with accuracy {results[best_model_name]:.4f}")

# Save the best model
joblib.dump(best_model, "best_model.pkl")
print("✅ Saved best model as best_model.pkl")

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import pandas as pd
# import joblib
# 
# # Load the trained model
# model = joblib.load("best_model.pkl")
# 
# st.set_page_config(page_title="Employee Salary Classification", page_icon="💼", layout="centered")
# 
# st.title("💼 Employee Salary Classification App")
# st.markdown("Predict whether an employee earns >50K or ≤50K based on input features.")
# 
# # Sidebar inputs (these must match your training feature columns)
# st.sidebar.header("Input Employee Details")
# 
# # ✨ Replace these fields with your dataset's actual input columns
# age = st.sidebar.slider("Age", 18, 65, 30)
# education = st.sidebar.selectbox("Education Level", [
#     "Bachelors", "Masters", "PhD", "HS-grad", "Assoc", "Some-college"
# ])
# occupation = st.sidebar.selectbox("Job Role", [
#     "Tech-support", "Craft-repair", "Other-service", "Sales",
#     "Exec-managerial", "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct",
#     "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv",
#     "Protective-serv", "Armed-Forces"
# ])
# hours_per_week = st.sidebar.slider("Hours per week", 1, 80, 40)
# experience = st.sidebar.slider("Years of Experience", 0, 40, 5)
# 
# # Build input DataFrame (⚠️ must match preprocessing of your training data)
# input_df = pd.DataFrame({
#     'age': [age],
#     'education': [education],
#     'occupation': [occupation],
#     'hours-per-week': [hours_per_week],
#     'experience': [experience]
# })
# 
# st.write("### 🔎 Input Data")
# st.write(input_df)
# 
# # Predict button
# if st.button("Predict Salary Class"):
#     prediction = model.predict(input_df)
#     st.success(f"✅ Prediction: {prediction[0]}")
# 
# # Batch prediction
# st.markdown("---")
# st.markdown("#### 📂 Batch Prediction")
# uploaded_file = st.file_uploader("Upload a CSV file for batch prediction", type="csv")
# 
# if uploaded_file is not None:
#     batch_data = pd.read_csv(uploaded_file)
#     st.write("Uploaded data preview:", batch_data.head())
#     batch_preds = model.predict(batch_data)
#     batch_data['PredictedClass'] = batch_preds
#     st.write("✅ Predictions:")
#     st.write(batch_data.head())
#     csv = batch_data.to_csv(index=False).encode('utf-8')
#     st.download_button("Download Predictions CSV", csv, file_name='predicted_classes.csv', mime='text/csv')

!pip install streamlit pyngrok

!ngrok authtoken 300rxunPtYYPcQVEBgUED9KyV6q_bUVjLvPJwzMVP2L9wWAe

import os
import threading

def run_streamlit():
  os.system('streamlit run app.py --server.port 8800')

thread= threading.Thread(target=run_streamlit)
thread.start()

from pyngrok import ngrok
import time

time.sleep(6)

public_url = ngrok.connect(8800, "http")  # ✅ Use protocol as second argument
print("Your Streamlit app is live here:", public_url)

from pyngrok import ngrok
import time

# Kill any previously running tunnels
ngrok.kill()
time.sleep(1)

# Start a new tunnel
public_url = ngrok.connect(8800, "http")
print("✅ Your Streamlit app is live here:", public_url)

