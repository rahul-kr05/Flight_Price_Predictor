import streamlit as st
import joblib
import pandas as pd

# Load the model
try:
    rf = joblib.load('random_forest_model.pkl')
    st.write("Model loaded successfully.")
except Exception as e:
    st.write(f"Error loading model: {e}")
    rf = None

# Title of the app
st.title("Airline Ticket Price Prediction")

# Mapping dictionaries
airline_map = {'AirAsia': 0, 'Indigo': 1, 'GO_FIRST': 2, 'SpiceJet': 3, 'Air_India': 4, 'Vistara': 5}
source_city_map = {'Delhi': 0, 'Hyderabad': 1, 'Bangalore': 2, 'Mumbai': 3, 'Kolkata': 4, 'Chennai': 5}
departure_time_map = {'Late_Night': 0, 'Afternoon': 1, 'Early_Morning': 2, 'Evening': 3, 'Morning': 4, 'Night': 5}
stops_map = {'zero': 0, 'two_or_more': 1, 'one': 2}
arrival_time_map = {'Late_Night': 0, 'Early_Morning': 1, 'Afternoon': 2, 'Night': 3, 'Morning': 4, 'Evening': 5}
destination_city_map = {'Delhi': 0, 'Hyderabad': 1, 'Mumbai': 2, 'Bangalore': 3, 'Kolkata': 4, 'Chennai': 5}
class_map = {'Economy': 0, 'Business': 1}

# User inputs
airline = st.selectbox('Airline', list(airline_map.keys()))
source_city = st.selectbox('Source City', list(source_city_map.keys()))
departure_time = st.selectbox('Departure Time', list(departure_time_map.keys()))
stops = st.selectbox('Number of Stops', list(stops_map.keys()))
arrival_time = st.selectbox('Arrival Time', list(arrival_time_map.keys()))
destination_city = st.selectbox('Destination City', list(destination_city_map.keys()))
travel_class = st.selectbox('Class', list(class_map.keys()))

# Additional numeric inputs
duration = st.number_input('Duration (in hours)', min_value=0.0, step=0.1)
days_left = st.number_input('Days Left until Flight', min_value=0, step=1, format='%d')

# Prepare the input data as a dictionary
input_data = {
    'airline': airline_map[airline],
    'source_city': source_city_map[source_city],
    'departure_time': departure_time_map[departure_time],
    'stops': stops_map[stops],
    'arrival_time': arrival_time_map[arrival_time],
    'destination_city': destination_city_map[destination_city],
    'class': class_map[travel_class],
    'duration': duration,
    'days_left': int(days_left)  # Ensure this is an integer
}

# Convert the input dictionary to a DataFrame
input_df = pd.DataFrame([input_data])

# Predict button
if st.button('Predict Price'):
    if rf is not None:
        try:
            # Ensure input is in the correct format (numeric and without missing values)
            prediction = rf.predict(input_df)
            st.write(f"Predicted Ticket Price: ${prediction[0]:.2f}")
        except Exception as e:
            st.write(f"Error in prediction: {e}")
    else:
        st.write("Model is not loaded properly.")
