# Test Description

## 1 Subscriptions
Auto-renewable subscriptions are a type of contract between service providers and users which is widely
present in business models out there. Examples are: subscriptions to newspapers, rechargeable plans in
phone companies. You basically pay a fixed amount of money, regularly, with a given frequency (e.g.
monthly), unless you explicitly exit the contract (unsubscribe): in this case you won’t pay anymore.
Subscriptions are used to pay for premium features in mobile applications too. For example Whatsapp used
to have cheap yearly subscription, while Tinder has a bit more expansive monthly subscription, and so does
Spotify.
Suppose to have a very simple mathematical model to describe user behavior in a subscription context. A
user lives in discrete positive time t, that starts flowing at the moment they enter the subscription and has
a time step as wide as the subscription period (e.g. one month). Each user has a fixed probability p ∈ [0, 1]
of unsubscribing just before every time step t > 0. This probability is a free parameter of the model, and
has the same value for all users. A model like this leads to patterns of subscription renewals like this:

![image](https://github.com/GiovanniMisseri/Unsubscription_test/assets/28415293/00c7f18b-60c1-4a03-8349-ea5290b43a58)


Where 1 indicates that user has paid the subscription, 0 that has not, therefore unsubscribing. Once you
see a 0 for a user you won’t see 1 anymore, so this table is redundant. It is enough to have the count of
renewals and the max time T a user has been observed.

![image](https://github.com/GiovanniMisseri/Unsubscription_test/assets/28415293/bb86caef-42a2-4f9b-87b8-566f60abedee)


Write a program (in python, R, or your preferred programming language) that, given a parameter p, can
simulate user patterns like the ones shown in the table here: that basically can generate the number of
renewals for a set of N users, given a period of observation T.
Add to the program a functionality to fit data like these, to find the most likely value for the unknown
parameter p. Verify on data you simulated that the fitter actually works.
The attached dataset (file data_subscriptions.csv) contains subscription data from “real-world” users.
Do you think that the model above is a suitable one for describing the behavior of these users? Justify your
answer.

Share the program you wrote in a zip folder. Make sure the code is easy to understand or at least very well
documented. Attaching a step by step guide to help us run the code ourselves is very nice to have (especially
if you use some uncommon libraries or frameworks), but not mandatory.

## 2 Machine Learning Challenge
Let’s assume we have an app which is downloaded by a certain number of people every day. Every user who

downloads the app can choose to unlock some premium features with a weekly, a monthly or a yearly sub-
scription. Every user has the right to cancel the subscription and stop paying at any time. The subscription

might start with a free trial: in that case the user doesn’t pay immediately after the subscription, but only
at the end of the free trial if they don’t cancel the subscription before that time.
When a user downloads the app, we immediately gather some data, like the country and the type of device
which generated the download. At the first opening, the user can complete an onboarding process, providing
additional information like age and gender. If the user starts a subscription, she/he will generate purchases
over time (in example, one purchase a week for weekly subscriptions, for a certain number of weeks).
For business planning and marketing purposes, we’re interested in predicting the total purchases that each
user will make over the course of one year since the start of the subscription, based on the data available up
to 15 days since the subscription.
Your goal is to find a suitable model to solve this problem. You will find two datasets in the attachment
ml.zip: train.csv and test.csv.
Each dataset contains the following columns:
- uid: random ID assigned to each user
- install timestamp: timestamp when the user downloaded and installed the app
- free trial timestamp: timestamp when the user subscribed to a premium plan (weekly, monthly or
yearly subscription)
- country: country (from the device settings)
- language: language (from the device settings)
- device type: device model
- os version: operating system version
- attribution network: advertising network which took credit for the download. In example, if a user
saw an ad on Facebook and downloaded the app shortly thereafter, the attribution network for the
user is Facebook
- product price tier: price tier associated to the product (a proxy of the price in USD)
- product periodicity: periodicity of the subscription (in days)
- product free trial length: length of the free trial period (in days)
- onboarding birth year: birth year provided by the user during the onboarding
- onboarding gender: gender provided by the user during the onboarding
- net purchases 15d: net purchases generated by the user in the first 15 days since starting the free
trial (net stands for “net of refunds”)
- net purchases 1y: net purchases generated by the user in the first 365 days since starting the free
trial. This is the target variable you want to predict: it’s available to you only in the training set,
while it’s private in the test set and it will be used to evaluate your model’s performance.


Your goal is to create a machine learning model (or any other kind of statistical model) to predict the
net purchases 1y variable in the test set based on all the data available, minimizing the root mean

squared error (RMSE) between your prediction and the ground truth. Your solution will include two deliv-
erables:

- An array of predictions, ˆy, in CSV format. Knowing the ground truth net purchases 1y in the test set,
y, we will evaluate your submission by measuring its RMSE, namely

![image](https://github.com/GiovanniMisseri/Unsubscription_test/assets/28415293/f1001dfc-868c-4327-8213-2937335e164c)


You will find an example Python script to import the data, fit a statistical model, generate a prediction
and export it into CSV for submission. The script is available in Jupyter Notebook and HTML format,
in the files example solution.ipynb and example solution.html. Your deliverable will have the
same format as example sumbission.csv.
- The code of your solution, and the steps that led you to that specific solution. Please make sure to
add meaningful comments to the code, to make us understand what you did and why: your reasoning
to reach the solution is as important as the solution itself to us. We provided examples in Python
because that’s the language we usually work with, but you can use whichever language or framework
you prefer, as long as the code is clearly readable or at least well explained. Attaching a step by step
guide to help us run the code ourselves is very nice to have (especially if you use some uncommon
libraries or frameworks), but not mandatory. Be sure to answer these questions (in the code or in a
separate document):
  - Which model did you choose and why?
  - What are the most predictive features?
  - How did you handle outliers and missing values in the dataset?
  - Would it be possible to improve the model’s performance by adding more data available in the
first 15 days since subscription?
  - Did you discover any non-trivial insights in the data which could help you build a better model?
  
Enjoy the challenge, and good luck.

# Provided Soluiton

## 1 Subscriptions
"Unsubscription.zip", a zip folder with the unsubscription program you asked for.
The program is actually a .py and is meant to run on a terminal.
The argument are:
    --simulation_param_p, the probability of unsubscription per time window
    --simulation_param_n, the populazion size for the simulation
    --simulation_param_T, the observation period
    --output_path_simulation, the path where simulation data should be saved
    --path_input_data, path to the input data

To generate synthetic data the attributet simulation_param_p, simulation_param_n, simulation_param_T and output_path_simulation are mandatory.
To estimate the p coefficient path_input_data is mandatory.
Here is an example of working command for simulation: 
python3 Unsubscription.py --simulation_param_p 0.2 --simulation_param_n 100000 --simulation_param_T 15 --output_path_simulation /content/results.csv


Here is an example of working command for estimating the p parameter: 
python3 Unsubscription.py --path_input_data /content/data_subscriptions.csv

"Unsubscriptions.ipynb" contains the study and commented code used to create the program.

## 2 Machine Learning Challenge
"ML_challenge.ipynb" is a notebook with code and comments relative to the prediction challenge.
"submission.csv" containing the test predictions.
