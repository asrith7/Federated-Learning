import pandas as pd

class ClinicalDataAgent:
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)

    def analyze_data(self):
        return {"summary": self.data.describe().to_dict()}

    def simulate_federated_learning(self):
        # Simulate 2 hospitals
        df1 = self.data.sample(frac=0.5, random_state=1)
        df2 = self.data.drop(df1.index)

        # Local mean of 'Cl.thickness' per class
        local1 = df1.groupby("Class")["Cl.thickness"].mean()
        local2 = df2.groupby("Class")["Cl.thickness"].mean()

        # Combine by averaging the local models
        combined = (local1 + local2) / 2

        return {
            "Hospital_1": local1.to_dict(),
            "Hospital_2": local2.to_dict(),
            "Federated_Model": combined.to_dict()
        }
