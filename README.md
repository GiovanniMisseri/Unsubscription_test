# Unsubscription_test

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

    t 0 1 2 3
user1 1 1 0 0
user2 1 0 0 0
user3 1 1 1 0
user4 1 1 1 1

Where 1 indicates that user has paid the subscription, 0 that has not, therefore unsubscribing. Once you
see a 0 for a user you won’t see 1 anymore, so this table is redundant. It is enough to have the count of
renewals and the max time T a user has been observed.

 user id renewals T
user1  1   3
user2  0   3
user3  2   3
user4  3   3

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
• uid: random ID assigned to each user
• install timestamp: timestamp when the user downloaded and installed the app
• free trial timestamp: timestamp when the user subscribed to a premium plan (weekly, monthly or
yearly subscription)
• country: country (from the device settings)
• language: language (from the device settings)
• device type: device model
• os version: operating system version
• attribution network: advertising network which took credit for the download. In example, if a user
saw an ad on Facebook and downloaded the app shortly thereafter, the attribution network for the
user is Facebook
• product price tier: price tier associated to the product (a proxy of the price in USD)
• product periodicity: periodicity of the subscription (in days)
• product free trial length: length of the free trial period (in days)
• onboarding birth year: birth year provided by the user during the onboarding
• onboarding gender: gender provided by the user during the onboarding
• net purchases 15d: net purchases generated by the user in the first 15 days since starting the free
trial (net stands for “net of refunds”)
• net purchases 1y: net purchases generated by the user in the first 365 days since starting the free
trial. This is the target variable you want to predict: it’s available to you only in the training set,
while it’s private in the test set and it will be used to evaluate your model’s performance.

