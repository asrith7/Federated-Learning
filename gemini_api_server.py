from fastapi import FastAPI
from clinical_agent import ClinicalDataAgent
from crew_federated import FederatedCrewRunner


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Clinical Research Agent is running"}

@app.get("/analyze")
def analyze():
    agent = ClinicalDataAgent("data/clinical_sample.csv")
    return agent.analyze_data()

@app.get("/federated")
def federated_learning():
    agent = ClinicalDataAgent("data/clinical_sample.csv")
    return agent.simulate_federated_learning()

@app.get("/crew")
def run_crew():
    from clinical_agent import ClinicalDataAgent
    agent = ClinicalDataAgent("data/clinical_sample.csv")

    df1 = agent.data.sample(frac=0.5, random_state=1)
    df2 = agent.data.drop(df1.index)

    result1 = df1.groupby("Class")["Cl.thickness"].mean()
    result2 = df2.groupby("Class")["Cl.thickness"].mean()

    from crew_federated import FederatedCrewRunner
    runner = FederatedCrewRunner(result1, result2)
    result = runner.run()

    return result

