# Prediction of Car Prices - Regression Algorithms(Machine Learning)
![image](https://raw.githubusercontent.com/junaidumbc/AbdulJunaid_data606/main/docs/images/usedcars_images22.jpg)

Under the guidance: **Prof. Wang, Chaojie**

Presented By :     **Abdul Junaid Mohammed**


#### Link to Dataset: [data](https://github.com/junaidumbc/AbdulJunaid_data606/tree/main/data)
#### Link to Presentation: [Final presentation](https://github.com/junaidumbc/AbdulJunaid_data606/blob/main/docs/Capstone_Presentation.pdf)
#### Link to Code: [notebooks](https://github.com/junaidumbc/AbdulJunaid_data606/tree/main/src)
#### Link to Youtube: [Youtube](https://www.youtube.com/watch?v=4feiwZIg-tg)

## Abstract
Buying a used car can be a challenging task, especially if you're new to the country and unfamiliar with the market value of cars. The used car market is extensive, and people can sometimes get cheated when they don't know the fair purchase or sale price of a pre-owned car. The main objective here is to develop a machine-learning model that predicts the price of used cars based on fundamental details, such as the year, model, make, and mileage.

## Introduction
The used car market is a significant sector in the United States and is expected to continue growing in the coming years due to factors such as rising new car prices, better condition of used cars, and low interest rates. As a result, many people turn to the used/pre-owned car market as a more affordable option (PMR, 2020). For this project, I developed a front-end web application using Streamlit that provides users with an interface to estimate the price of used cars by inputting relevant information using Regression algorithms.

## Data
The dataset used in this project consists of 26 attributes and 426,880 records, collected by scraping data from the Craigslist website. The dataset includes cars manufactured from 1920 to 2020 and encompasses almost all the essential features required for building an accurate prediction model. The attributes cover various types of information, including price, odometer reading, condition, type, fuel, year, transmission, etc. These attributes are classified into three data types: integer, string, and datetime format. The detailed data available made it easy to determine which features were relevant and which were not important for the model.

## Data Cleaning and Pre processing
In the data cleaning and preprocessing stage, redundant columns that were not relevant to the model, such as County, Id, Lat, Long, region, and VIN, were removed, leaving around 14 relevant attributes. Missing values in the dataset were handled by applying imputation techniques such as filling categorical column missing values with the mode of their respective columns, bfill(), ffill() and numerical columns missing values with the mean of their respective columns. Additionally, duplicate records were removed from the dataset.
To handle outliers in columns such as Odometer and Price, the Interquartile Range (IQR) technique was used. For categorical encoding, I have used label encoding to all categorical features so that the machine could understand the data. Data scaling was then applied using MinMaxScaler() as the data did not have a normal distribution and scaling was necessary to achieve a specific range, such as between 0 and 1

## Modelling
Before modelling, the dependent variable was selected as the PRICE column (Y), and the rest of the columns were selected as independent variables (X). The dataset was split into 70% training and 30% testing sets. Five supervised machine learning prediction models were used, namely:

*	Linear Regression

*	Decision Tree Regressor
*	Random Forest Regressor
*	XG Boost Regressor
*	Lasso Regression

Each of these models was trained on the training set and evaluated on the testing set using metrics such as coefficient of determination (R^2), Root mean squared error (RMSE), and Mean absolute error (MAE). However, the accuracy scores were not as expected, so to improve the scores, hyperparameter tuning was performed using randomized search CV on each of the models. Finally, the **Random Forest Regressor** model with the best accuracy score of **86%** was selected.

## Results
![image](https://raw.githubusercontent.com/junaidumbc/AbdulJunaid_data606/main/docs/images/Results.png)

* Higher R-squared values and lower MAE, MSE, and RMSE values indicate better model performance.

## Deployment
The best model, i.e. the Random Forest Regressor, was saved as a pickle file. This model was connected to the web app with a user interface that takes in car feature details and outputs the estimated price of the car. The web interface was designed to make it easy for users to interact with the model and get quick and accurate results.

![image](https://raw.githubusercontent.com/junaidumbc/AbdulJunaid_data606/main/docs/images/Streamlit_ScreenShot.png)


## Conclusion
In conclusion, this project demonstrated the use of machine learning algorithms to predict the price of used cars based on fundamental details. The project used a large dataset collected from the Craigslist website, and various data preprocessing techniques were applied to handle missing values, duplicates, and outliers. Five supervised machine learning algorithms were evaluated, and the Random Forest Regressor algorithm was selected based on its accuracy score. A web application was developed to provide a user-friendly interface for users to input car details and obtain accurate price predictions.

## References
* https://www.jiffylubesocal.com/jiffy-lube-blog/2015/10/drive-type-faq-awd-rear-wheel-front-wheel-whats-the-big-deal/
* https://www.census.gov/quickfacts/CA
* https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/
* https://mobilityforesights.com/product/used-car-market-in-us/
* https://docs.streamlit.io/knowledge-base/tutorials/deploy
