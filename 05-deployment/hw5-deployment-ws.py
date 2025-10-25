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

"""

import pickle
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Dict, Any
from typing import Literal
from pydantic import BaseModel, Field

app = FastAPI(title="Model Deployment Service")


# request

class SubscriptionRequest(BaseModel):
    lead_source: Literal["organic_search", "paid_search", "referral", "direct", "social_media"]
    number_of_courses_viewed: int = Field(..., ge=0)
    annual_income: float = Field(..., ge=0.0)


class PredictSubscriptionResponse(BaseModel):
    subscription_probability: float



# Load Model
with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

@app.post("/predict_subscription")
def predict_subscription(subscriptionRequest: SubscriptionRequest) -> PredictSubscriptionResponse:
    req = subscriptionRequest.model_dump()
    print(f"req : {req}")
    probability = pipeline.predict_proba(req) [0, 1]
    print(f"predicted probability: {probability}")
    return PredictSubscriptionResponse(subscription_probability=probability)




if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=9696)