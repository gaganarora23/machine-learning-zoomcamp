"""

Now let's serve this model as a web service

Install FastAPI
Write FastAPI code for serving the model
Now score this client using requests:
url = "YOUR_URL"
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}
requests.post(url, json=client).json()
What's the probability that this client will get a subscription?

0.334
0.534
0.734
0.934


"""

import requests

url = "http://localhost:9696/predict_subscription"
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}
resp = requests.post(url, json=client).json()
print(resp)

