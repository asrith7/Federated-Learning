from crewai import Agent, Task, Crew
from crewai import Crew, Agent, Task
from langchain.llms.fake import FakeListLLM


class FederatedCrewRunner:
    def __init__(self, hospital_1_data, hospital_2_data):
        self.hospital_1_data = hospital_1_data
        self.hospital_2_data = hospital_2_data

    def run(self):
        # Simulate Hospital A local training
        result1 = self.hospital_1_data.to_dict()

        # Simulate Hospital B local training
        result2 = self.hospital_2_data.to_dict()

        # Combine results
        combined = (self.hospital_1_data + self.hospital_2_data) / 2
        combined_result = combined.to_dict()

        return {
            "Hospital_1_Result": result1,
            "Hospital_2_Result": result2,
            "Federated_Model": combined_result
        }
