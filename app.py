import streamlit as st
import datetime
import requests


'''
# TaxiFareModel front
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''
#date
d = st.date_input(
        'Please enter a date',
        datetime.date(2024, 5, 17)
    )
st.write('Date is set for: ', d)

#time
t = st.time_input('Please enter a time', datetime.time(12,00))
st.write('Time is set for ', t)

#pickup longitude
p_lon = st.number_input('Please enter a pickup longitude')
st.write('Pickup longitude is set as ', p_lon)

#pickup latitude
p_lat = st.number_input('Please enter a pickup latitude')
st.write('Pickup latitude is set as ', p_lat)

#dropoff longitude
d_lon = st.number_input('Please enter a dropoff longitude')
st.write('Dropoff longitude is set as ', d_lon)

#dropoff latitude
d_lat = st.number_input('Please enter a dropoff latitude')
st.write('Dropoff latitude is set as ', d_lat)

#passenger count
passengers = st.slider('Please select number of passengers', 1, 6, 2)
st.write('The number of passengers is ', passengers)
# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''

date_time = f'{d} {t}'
params = {
        'pickup_datetime': date_time,
        'pickup_longitude': p_lon,
        'pickup_latitude': p_lat,
        'dropoff_longitude': d_lon,
        'dropoff_latitude': d_lat,
        'passenger_count': passengers,
        #'fare_amount': 0
        }

results = requests.get(url,params=params)
res_json = results.json()
st.write('You estimated fare will be: ', res_json['fare'])
