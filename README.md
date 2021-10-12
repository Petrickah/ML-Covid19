# Machine Learning COVID-19 Predictor

### This project proposes a linear regression predictor for Covid-19 outcome </br>

Using Python, Pandas, Scikit-Learn I've wrote a linear regression predictor with Machine Learning to predict the outcome of the current COVID-19 pandemic.

I started from a linear time series and transformed it using the 1000 people ratio split in weeks. I've tried to use the values as a Finance evolution diagram (candle sticks diagram).

For each week I've calculated the staring value (Open value), ending value (Close value) and the minimum and maximum value (Low and High values) of the current week. The prediction is "With which value the next week will open during the pandemic?". Based on that, the prediction is the value increasing or decreasing in the next week based on the current known one.

The starting value and ending value, maximum and minimum was the training data for a liniear regression model. Using Polynomial, and ElasticNet models I've descovered that the Polynomial model is the best one obtaining an 98.6% score on the testing dataset.