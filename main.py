import streamlit as st
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')


with open('FinalHousePriceModel.pickle', 'rb') as f:
    model = pickle.load(f)
with open('AreaTypes.pickle', 'rb') as f:
    AreaTypes = pickle.load(f)
with open('Location.pickle', 'rb') as f:
    Location = pickle.load(f)

AreaTypesClasses = list(AreaTypes.classes_)
AreaTypesClasses.insert(0, 'Select')
LocationClasses = list(Location.classes_)
LocationClasses.insert(0, 'Select')

st.title("Bengaluru House Price Prediction")

st.markdown("### Enter the details of the house to get the price prediction")
st.markdown("")

location = st.selectbox("Location", LocationClasses)
row1_1, row1_2 = st.columns(2)
with row1_1:
    area = st.number_input("Area in sqft", min_value=300, max_value=30000, step=10)
with row1_2:
    areaType = st.selectbox("Area Type", AreaTypesClasses)

row2_1, row2_2, row2_3 = st.columns(3)
with row2_1:
    bhk = st.number_input("BHK", min_value=1, max_value=5, step=1)
with row2_2:
    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=5, step=1)
with row2_3:
    balcony = st.number_input("Balcony", min_value=0, max_value=3, step=1)


if st.button("Predict"):
    if areaType != 'Select' and location != 'Select' and area != 0 and bhk != 0 and bathrooms != 0:
        if (areaType in AreaTypesClasses) and (location in LocationClasses) and (300<=area<=30000) and (1<=bhk<=5) and (1<=bathrooms<=5) and (0<=balcony<=3):
            areaTypeGiven = AreaTypes.transform([areaType])
            locationGiven = Location.transform([location])

            modelInput = [[areaTypeGiven[0], locationGiven[0], area, bathrooms, balcony, bhk]]
            print(modelInput)
            prediction = model.predict(modelInput)
            if prediction[0]<0:
                st.text("Couldn't predict the price! This is due to the lack of data for the given location.")
            else:
                st.text("The predicted price of the house is: " + str(prediction[0]) + " Lakhs")

        else:
            st.text("Please enter valid details!")
    else:
        st.text("Please enter valid details!")


