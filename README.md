# House Price Regression 🏠

👋 Hello and welcome to Welcome to the House Price Regression project! 🏠 This notebook showcases my solution for predicting the sale price of residential properties in Ames, Iowa. With a top 12% ranking in the competition 🥳, I am excited to share my approach and insights with you, you will find everything you need to train and test the model, as well as some additional tools and resources to help you get started.🚀

## Getting Started 🚀

To understand the project, you will need to have some knowledge of machine learning and data analysis. You will also need to have Python 3.x installed on your system, along with the following libraries:

- Pandas 🐼
- Numpy 🔢
- Scikit-learn 🧮
- Matplotlib 📈
- xgboost 🚀

## Data 📊

The data used in this project is a sample dataset from the [Kaggle House Prices competition](https://www.kaggle.com/c/house-prices-advanced-regression-techniques). It includes information on the sale prices and features of residential properties in Ames, Iowa. We have preprocessed and cleaned the data to make it easier to use, but you can also explore the original dataset if you're interested.

## Model 🔍

### XGBoosting

After some experiments the final version was made with XGBoosting, XGBoost is based on the gradient boosting framework, which involves iteratively adding weak learners (simple models) to the ensemble, each time focusing on the samples that were poorly predicted by the previous models. 

### Hyper-parameter tuning and model optimization

I created 200 optuna studies to find the best hyper-parameters based on the root mean squared error of the logarithm of the target values which is the valuation metric for the competition. After the training and validation for the best model I used feature importances to delete all columns which where not important for the prediction, which made my model faster and simpler.

## Evaluation 📈

To evaluate the performance of the model, I used various metrics such as mean squared error, root mean squared error, and mean absolute percentage error. I validated the model during training using the root mean squared error of the logarithm of the target values.

## Results 🎉

This model got top 568 or ~12% for the <a href="https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/leaderboard#">Kaggle competition</a> 🏆, which is a very good result taking in account that the test results got <a href="https://www.kaggle.com/code/nitindantu/100-accurate">leaked</a>. 

## Conclusion 🙌

We hope you find this House Price Regression project useful and informative. Please feel free to explore the code and data, and make any modifications or improvements you see fit. If you have any questions or suggestions, please don't hesitate to contact us. Happy coding!
