# Prediction of Car Prices – Regression
## Business Problem
The business problem will be around automobile industry, predicting the prices of used cars. Buying a used car will be difficult task, especially when you are new to the country and don’t know the market value of the cars. Me and my friends have faced many problems while buying a car online, this made me go ahead with this project. So, this project will help user to get the estimate price of the car by providing the basic details such as year, model, company, miles driven etc.
 	I will use various data sources to not only identify useful insights and patterns, but also use the data to predict the used car prices with the help of regression algorithms.
## Dataset
The dataset is a collection of data scraped from the well-known website Craigslist. Dataset has been acquired from : https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data 
## Features of data
It has 426880 Rows and 26 columns. It has all the useful features which will be rquired for the purchase of used car. Here the Target Variable will be the Price Column.
Column Names Datatypes

  * id              - int64  
 
 *   url           	-  object 
 
 *   region       	 - object 
 
 *   region_url   	 - object 
 
 *   price         	 - int64  
 
 *   year          	 - float64
 
 *   manufacturer	 - object 
 
 *   model         	 - object 
 
 *   condition     	 - object 
 
 *   cylinders    	 - object 
 
 *  fuel         	 - object 
 
 *  odometer     	 - float64
 
 *  title_status  	 - object 
 
 *  transmission 	 - object 
 
 *  VIN          	 - object 
 
 *  drive         	 - object 
 
 *  size          	 - object 
 
 *  type          	 - object 
 
 *  paint_color  	 - object 
 
 *  image_url     	 - object 
 
 *  description   	 - object 
 
 *  county       	 - float64
 
 *  state         	 - object 
 
 *  lat           	- float64
 
 *  long          	- float64
 
 *  posting_date   - object 

## ML Models
I will be using Regression machine learning algorithms such as Linear Regression, Random Forest Regression, Lasso Regression,XGBoost Regressor. 
Also, I will be applying Hyperparameter Tuning on different models using the Randomized Search Cv/Grid Search for better outcomes.
In the last, a model with good scores based on metrics such as R2 (Coefficient of determination), RMSE(Root Mean Square Error) will be
selected and will be used for deployment.
## Deployment.
Planning to develop front end web application using Streamlit/ Flask so that user can get the price estimate of the cars
