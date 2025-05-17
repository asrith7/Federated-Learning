from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from agents import medical_clinical_agent, federated_learning_agent

app = FastAPI()

# ✅ Add this CORS configuration:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://127.0.0.1:8001"] for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Unified LLM Agent for Clinical Trials and Federated Learning"}

@app.get("/agent/clinical")
def get_clinical_trial_help(question: str = Query(...)):
    result = medical_clinical_agent(question)
    return {"response": result}

@app.get("/agent/federated")
def get_federated_insights():
    result = federated_learning_agent()
    return {"response": result}
