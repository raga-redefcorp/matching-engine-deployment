from fastapi import HTTPException, Header
import pandas as pd
import os

# Formats the incoming payload for the ml model
def format_data(data):
    df = pd.DataFrame(data, index=[0])
    df['status'] = df['status'].replace([20,10],[0,1])
    df['diff_experience'] = df['min_exp'] - df['experience']    
    df["skill_matching_score"] = df['score']
    return df

# Gets the stored secret from .env
def get_secret():
    return os.getenv("MY_SECRET_KEY")

# Checks the incoming secret with the stored secret in .env for authorization
async def verify_secret(secret: str = Header(...)):
    stored_secret = get_secret()
    if secret != stored_secret:
        raise HTTPException(status_code=401, detail="Invalid secret")