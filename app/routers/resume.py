import pickle
from fastapi import APIRouter, Depends

from app.models.ResumeModel import ResumeModel
from app.utils import format_data, verify_secret

router = APIRouter(
  prefix = "/resume",
  tags = ["Resume"]
)

@router.get("/")
async def root():    
    return {"message": "Welcome to the matching engine API!!"}

@router.post("/get-prediction/", dependencies=[Depends(verify_secret)])
async def get_resume_score(data: ResumeModel):
    data = data.dict()
    df = format_data(data)
    model = pickle.load(open('rf_model.pkl', 'rb'))
    y_pred = model.predict(df[["diff_experience","skill_matching_score"]])
    y_pred_proba = model.predict_proba(df[["diff_experience","skill_matching_score"]])
    y_pred = y_pred.reshape(-1)[0]
    y_pred_proba = y_pred_proba.reshape(-1)[y_pred]
    return {'matching_percentage': y_pred_proba}
