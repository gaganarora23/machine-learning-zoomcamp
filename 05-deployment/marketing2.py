import requests

url = "https://cold-brook-3074.fly.dev/predict_subscription"

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}
response = requests.post(url, json=client).json()
print(response)
subscription_probability = response.get("subscription_probability", 0)

print(f"Subscription Probability: {subscription_probability:.3f}")

