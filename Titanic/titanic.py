import streamlit as st
import pandas as pd
#import dill as pickle
import numpy as np
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
import streamlit as st
import pickle
with open('../Titanic/model_pickle.pkl','rb') as file:
    model = pickle.load(file)
st.title('Did they survive? :ship:')
# PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
Pclass = st.selectbox("Choose class", [1,2,3])
# name  = st.text_input("Input Passenger Name", 'John Smith')
male = st.select_slider("Choose sex", ['male','female'])
if male == 'male':
    male=1
else:
    male=0

age = st.slider("Choose age",0,100)
# parch = st.slider("Choose parch",0,2)
# ticket = st.text_input("Input Ticket Number", "12345") 
fare = st.number_input("Input Fare Price", 0,1000)
# cabin = st.text_input("Input Cabin", "C52") 
embarked = st.select_slider("Did they Embark?", ['S','Q'])
if embarked == 'S':
    # embark= np.array([1,0]).reshape((2, 1))
    S=1
    Q=0
elif embarked == 'Q':
    # embark= np.array([0,1]).reshape((2, 1))
    S=0
    Q=1

def predict(): 
    row = np.array([Pclass,age,fare,male,S,Q])
    # .reshape((1, -1))
    X = pd.DataFrame([row])
    prediction = model.predict(X)
    if prediction[0] == 'Alive': 
        st.success('Passenger Survived :thumbsup:')
        st.balloons()
    else: 
        st.error('Passenger did not Survive :thumbsdown:') 

trigger = st.button('Predict', on_click=predict)
