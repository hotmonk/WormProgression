import streamlit as st
import random_scan
import local_preference_scan
import random

st.title("Worm Propagation Simulator")

st.header("Comparision between Propagation types")

st.subheader("Random Scanning vs Local Preference Scanning")


st.text("Select the type of propagation you want and click Run")

genre = st.radio(
    "Select the type of propagation you want and click Run",
    ('Random Scanning', 'Local Preference Scanning'))
if genre == 'Random Scanning':
    st.write('You selected Random Scanning')
else:
    st.write("You selected Local Preference Scanning")


if st.button('Run'):
    st.write('Running Simulation')
    if(genre == 'Random Scanning'):
        random.seed()
        methods = ['random_scan']
        for method in methods:
            random_scan.worm_propagation_simulation(method, plot=True)
    else:
        random.seed()
        methods = ['local_preference']
        for method in methods:
            local_preference_scan.worm_propagation_simulation(
                method, plot=True)

else:
    st.write('')
