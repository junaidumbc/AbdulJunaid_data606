## Libraries
import numpy as np
import pickle
import pandas as pd
import streamlit as st 

## Original data frame for enocding and mapping
og_data = pd.read_csv('veh_ML.csv')
## Loading Model
model_pkl = open("RandomForest_Regressor.pkl","rb")
cost=pickle.load(model_pkl)

## Predictions
def cost_function(year,manufacturer,model,condition,cylinders,fuel,odometer,title_status,transmission,drive,size,type,paint_color,state):
    prediction=cost.predict([[year,manufacturer,model,condition,cylinders,fuel,odometer,title_status,transmission,drive,size,type,paint_color,state]])
    print(prediction)
    return prediction

## Structure of the App
def app():

    st.title("Craigslist Car Price Prediction - Regression")
    st.image('https://m.economictimes.com/thumb/msid-79933399,width-1200,height-900,resizemode-4,imgsize-97551/honda-civic-1.jpg',width=200)

    year = st.number_input('year', 1990, 2020)

    ## manufacturer
    manufacturer = st.selectbox('manufacturer', og_data['manufacturer'].unique())
    manufacturer_encoded = {'ford': 13, 'gmc': 14, 'chevrolet': 7, 'toyota': 39, 'jeep': 20, 'nissan': 31, 'ram': 34, 'mazda': 25, 
           'cadillac': 6, 'honda': 16, 'dodge': 10, 'lexus': 23, 'jaguar': 19, 'buick': 5, 'chrysler': 8, 'volvo': 41,
           'audi': 3, 'infiniti': 18, 'lincoln': 24, 'alfa-romeo': 1, 'subaru': 37, 'acura': 0, 'hyundai': 17,
           'mercedes-benz': 26, 'bmw': 4, 'mitsubishi': 29, 'volkswagen': 40, 'porsche': 33, 'kia': 21, 'rover': 35,
           'mini': 28, 'pontiac': 32, 'fiat': 12, 'tesla': 38, 'saturn': 36, 'mercury': 27, 'harley-davidson': 15,
           'datsun': 9, 'aston-martin': 2, 'land rover': 22, 'morgan': 30, 'ferrari': 11}

    if manufacturer in manufacturer_encoded:
        manufacturer = manufacturer_encoded[manufacturer]

    model = st.number_input('model')

    ## Condition
    condition = st.selectbox('Condition', og_data['condition'].unique())
    #condition = st.text_input('condition')
    if condition == 'excellent':
        condition = 0
    elif condition == 'fair':
        condition = 1
    elif condition == 'good':
        condition = 2
    elif condition == 'like new':
        condition = 3
    elif condition == 'new':
        condition = 4
    elif condition == 'salvage':
        condition = 5

    ##Cylinders
    cylinders = st.selectbox('cylinders', og_data['cylinders'].unique())
    cylinder_encoded = {'8 cylinders': 6, '6 cylinders': 5, '4 cylinders': 3, '5 cylinders': 4, 'other': 7, '3 cylinders': 2, '10 cylinders': 0, '12 cylinders': 1}
    if cylinders in cylinder_encoded:
        cylinders = cylinder_encoded[cylinders]

    
    ##fuel
    fuel = st.selectbox('fuel', og_data['fuel'].unique())
    #fuel = st.text_input('fuel')
    if fuel == 'diesel':
        fuel = 0
    elif fuel == 'electric':
        fuel = 1
    elif fuel == 'gas':
        fuel = 2
    elif fuel == 'hybrid':
        fuel = 3
    elif fuel == 'other':
        fuel = 4

    odometer = st.number_input('odometer')

    ## Title status
    title_status = st.selectbox('title_status', og_data['title_status'].unique())
    #title_status = st.text_input('title_status')
    if title_status == 'clean':
        title_status = 0
    elif title_status == 'lien':
        title_status = 1
    elif title_status == 'missing':
        title_status = 2
    elif title_status == 'parts only':
        title_status = 3
    elif title_status == 'rebuilt':
        title_status = 4
    elif title_status == 'salvage':
        title_status = 5

    ## transmission
    transmission = st.selectbox('transmission', og_data['transmission'].unique())
    #transmission = st.text_input('transmission')
    if transmission == 'automatic':
        transmission = 0
    elif transmission == 'manual':
        transmission = 1
    elif transmission == 'other':
        transmission = 2

    ##drive
    drive = st.selectbox('drive', og_data['drive'].unique())
    if drive == '4wd':
        drive = 0
    elif drive == 'fwd':
        drive = 1
    elif drive == 'rwd':
        drive = 2

    ##size
    size = st.selectbox('size', og_data['size'].unique())
    if size == 'compact':
        size = 0
    elif size == 'full-size':
        size = 1
    elif size == 'mid-size':
        size = 2
    elif size == 'sub-compact':
        size = 3

    ##type
    type = st.selectbox('type', og_data['type'].unique())
    if type == 'SUV':
        type = 0
    elif type == 'hatchback':
        type = 4
    elif type == 'convertible':
        type = 2
    elif type == 'coupe':
        type = 3
    elif type == 'other':
        type = 7
    elif type == 'mini-van':
        type = 5
    elif type == 'offroad':
        type = 6
    elif type == 'bus':
        type = 1
    elif type == 'pickup':
        type = 8
    elif type == 'sedan':
        type = 9
    elif type == 'truck':
        type = 10
    elif type == 'van':
        type = 11
    elif type == 'wagon':
        type = 12

    ## paint_color
    paint_color = st.selectbox('paint_color', og_data['paint_color'].unique())
    if paint_color == 'black':
        paint_color = 0
    elif paint_color == 'blue':
        paint_color = 1
    elif paint_color == 'brown':
        paint_color = 2
    elif paint_color == 'custom':
        paint_color = 3
    elif paint_color == 'green':
        paint_color = 4
    elif paint_color == 'grey':
        paint_color = 5
    elif paint_color == 'orange':
        paint_color = 6
    elif paint_color == 'purple':
        paint_color = 7
    elif paint_color == 'red':
        paint_color = 8
    elif paint_color == 'silver':
        paint_color = 9
    elif paint_color == 'white':
        paint_color = 10
    elif paint_color == 'yellow':
        paint_color = 11

    ## states
    state = st.selectbox('state', og_data['state'].unique())
    ## mapped with their encoded values
    state_encoded = {'az': 3, 'ar': 2, 'fl': 9, 'ma': 19, 'nc': 27, 'ny': 34, 'or': 37, 'pa': 38, 'wa': 47, 'wi': 48, 'al': 1, 'ak': 0, 'ca': 4, 'co': 5, 'ct': 6, 'dc': 7, 'de': 8, 'ga': 10, 'hi': 11, 'id': 13, 'il': 14, 'in': 15, 'ia': 12, 'ks': 16, 'ky': 17, 'la': 18, 'me': 21, 'md': 20, 'mi': 22, 'mn': 23, 'ms': 25, 'mo': 24, 'mt': 26, 'ne': 29, 'nv': 33, 'nj': 31, 'nm': 32, 'nh': 30, 'nd': 28, 'oh': 35, 'ok': 36, 'ri': 39, 'sc': 40, 'sd': 41, 'tn': 42, 'tx': 43, 'ut': 44, 'vt': 46, 'va': 45, 'wv': 49, 'wy': 50}
    if state in state_encoded:
        state = state_encoded[state]

    price=0
    if st.button("Predict"):
        price=cost_function(year,manufacturer,model,condition,cylinders,fuel,odometer,title_status,transmission,drive,size,type,paint_color,state)
    st.success(f'Estimated Price is : $ {price}')

    github_link = "https://github.com/junaidumbc/AbdulJunaid_data606"
    if st.button("Github_Code_Link"):
        st.markdown(f"[Click here to view the code on Github]({github_link})")

if __name__=='__main__':
    app()
    