import pickle
import streamlit as st
import numpy as np
st.set_page_config(page_title = "Calorie Burn")

calorie_model=pickle.load(open('calorie_burnt.sav','rb'))

st.title('Calorie Burnt Prediction')
st.markdown("This Web App, aims to predict the amount of calories burnt during physical activity based on various factors such as the your gender, height, weight, and the type of activity performed. The project uses machine learning algorithms to achieve this goal.")
st.caption('Discover your calorie burn rate for today')
st.caption('Lets Go!')

Gender=st.text_input("Gender")
Age=st.text_input("Age")
Height=st.text_input("Height")
Weight=st.text_input("Weight")
Duration=st.text_input("Duration")
HeartRate=st.text_input("Heart Rate")
BodyTemperature=st.text_input("Body Temperature")

if(Gender == 'Male'):
    Gender = 1
else:
    Gender = 0

caloriesBurnt=None
if(st.button('Find Calories Burnt')):
    inputData=(Gender,Age,Height,Weight,Duration, HeartRate, BodyTemperature)
    numpyArray=np.array(inputData,dtype=float)
    reshapedArray=numpyArray.reshape(1,-1)
    caloriesBurnt=calorie_model.predict(reshapedArray)


    
if caloriesBurnt is not None:
    caloriesBurntStr = "{:.2f}".format(caloriesBurnt[0])
    st.write('Calories Burnt (in kcal): ')
    st.success(caloriesBurntStr)
    st.write(' burnt today, Keep going.')

    


