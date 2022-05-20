import streamlit as st
import pickle
import pandas as pd

st.write("# Heart Disease Prediction")


gender = st.selectbox("Enter your gender",["Male", "Female"])

col1, col2, col3 = st.columns(3)


age = col1.number_input("Enter your age")

education = col2.selectbox('Please select your education', [1 ,2 ,3 ,4])

isSmoker = col3.slider("Ciggarettes per Day",0,75)

BPMeds = col1.selectbox("Are you currently on BP medication?",["Yes","No"])

stroke = col2.selectbox("Have you ever experienced a stroke?",["Yes","No"])

hyp = col3.selectbox("Do you have hypertension?",["Yes","No"])

diabetes = col1.selectbox("Do you have diabetes?",["Yes","No"])

chol = col2.slider("Enter your cholesterol level" ,100 ,400)

sys_bp = col3.slider("Enter your systolic blood pressure" ,80 ,300)

dia_bp = col1.number_input("Enter your diastolic blood pressure")

bmi = col2.number_input("Enter your BMI")

heart_rate = col3.number_input("Enter your resting heart rate")






df_pred = pd.DataFrame([[gender,age,education,isSmoker,BPMeds,stroke,hyp,diabetes,chol,sys_bp,dia_bp,bmi,heart_rate]],

columns= ['gender','age','education','cigsPerDay','BPMeds','prevalentStroke','prevalentHyp','diabetes','totChol','sysBP','diaBP','BMI','heartRate',])

df_pred['gender'] = df_pred['gender'].apply(lambda x: 1 if x == 'Male' else 0)

df_pred['prevalentHyp'] = df_pred['prevalentHyp'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['prevalentStroke'] = df_pred['prevalentStroke'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['diabetes'] = df_pred['diabetes'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['BPMeds'] = df_pred['BPMeds'].apply(lambda x: 1 if x == 'Yes' else 0)



model = pickle.load(open('/home/f5/Desktop/proj.pkl', 'rb'))
prediction = model.predict(df_pred)



if st.button('Predict'):

    if(prediction[0]==0):
        st.write('<p class="big-font">You likely will not develop heart disease in 10 years.</p>',unsafe_allow_html=True)

    else:
        st.write('<p class="big-font">You are likely to develop heart disease in 10 years.</p>',unsafe_allow_html=True)