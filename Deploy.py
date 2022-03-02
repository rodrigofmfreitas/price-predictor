import pandas as pd
import streamlit as st
import joblib

x_numeric = {'host_listings_count': 0, 'latitude': 0, 'longitude': 0,'accommodates': 0, 
             'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0,
             'minimum_nights': 0, 'number_of_reviews': 0, 'year': 0, 'month': 0, 'num_of_amenities': 0}
x_true_false = {'host_is_superhost': 0,  'instant_bookable': 0}
x_lists = {"property_type": ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite',
           'Guesthouse', 'Hostel','House', 'Loft', 'Other', 'Serviced apartment'],
           "room_type": ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
           "cancellation_policy": ['flexible', 'moderate', 'strict',
           'strict_14_with_grace_period', 'super_strict_30', 'super_strict_60']}

x_dict = dict()

for item in x_lists:
    for value in x_lists[item]:
        x_dict[f"{item}_{value}"] = 0

for item in x_numeric:
    if item == "latitude" or item == "longitude":
        value = st.number_input(f"{item}", step=0.00001, value=0.0, format="%.5f")
    elif item == "extra_people":
        value = st.number_input(f"{item}", step=0.01, value=0.0)
    else:
        value = st.number_input(f"{item}", step=1, value=0)
    x_numeric[item] = value

for item in x_true_false:
    value = st.selectbox(f"{item}", ("Yes", "No"))
    if value == "Yes":
        x_true_false[item] = 1
    else:
        x_true_false[item] = 0

for item in x_lists:
    value = st.selectbox(f"{item}", x_lists[item])
    x_dict[f"{item}_{value}"] = 1

button = st.button("Predict")

if button:
    x_dict.update(x_numeric)
    x_dict.update(x_true_false)
    x = pd.DataFrame(x_dict, index=[0])
    model = joblib.load("et_model.joblib")
    price = model.predict(x)
    st.write(price[0])
