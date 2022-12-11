# Yelp-Recommendation-System

## Data Preprocessing
We used Yelp database as our data source. In consideration of real-world situation, we decided to recommend businesses to users within the city. Thus, we picked Ballwin as our sample city, filter out all the review data about the businesses in this city. Our sample preprocessed data is saved as `/yelpdata/All Reviews.csv` with tags `review_id`,	`user_id`,	`business_id`,	`name`,	`stars_x`,	`text`,	`city`

## Rule-based Model
1. Run rule_based_recommendation.py with two extra command line parameters to get rule-based model recommendation. The first argument is the path of review.csv, the second argument is the user_id. The result is a business name list.
2. If the parameters are not correct, the file will print a the recommendation result of the default file (All_Reviews.csv) and a default user id ('N3udcZJAoPzkKkGFt2vHTA').

## SVD Model
1. Install the surprise package.
Run SVD.py with one extra command line parameter indicating the path of review file. If no command line parameter added,we will use the default review file All_Reviews.csv.
2. If the path and the review file is correct, the result is a table containing the 10 best predictions.

Pass in preprocessed `CSV` data file in form of `{'review_id':str,'user_id':str,'business_id':str,'stars':int,'date':str,'text':str,'useful':int,'funny':int,'cool':int} ` to function

## Node2Vec Model
1. Open the .ipynb file in the Node2Vec folder in Node2Vec folder
2. Do not change anything. Run the cells as it is.
3. Follow the text in the file. First load the datasets df, df_b which contain user-reviews and business information by executing the cells under the heading ‘Load Dataset’
4. Load model by executing the cells beneath the heading ‘Load Model’. The model is pre-trained by us. We will use this model for predictions
5. Generate Predictions using this model by executing the cells beneath ‘Model Predictions’

## Neural Collaborative Filtering
1. Open the .ipynb file in the NCF folder
2. Do not change anything. Run the cells as it is.
3. Follow the text in the file. First load the dataset df which contains user-reviews information and do the train and test split by executing all the cells beneath the heading ‘Load Dataset and Train and Test Split’
4. Train and Test the 3 models by executing all the cells corresponding to the models as described in the text of the .ipynb file

