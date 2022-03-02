import pickle
from fastapi import FastAPI

#2 Create the app object
app = FastAPI()

with open("../model/model.pkl", "rb") as f:
    model = pickle.load(f)

def classify_message(model, message):
    return {'label': model.predict([message])[0], 'spam_probability': model.predict_proba([message])[0][1]}

@app.get('/')
def index():
    return {'message': 'Spam Detection API'}

@app.get('/query/')
async def get_name(message: str):
    return classify_message(model, message)

@app.get('/path/{message}')
async def get_name(message: str):
    return classify_message(model, message)

#uvicorn main:app --reload