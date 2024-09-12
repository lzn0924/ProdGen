from langchain.tools import BaseTool
from py2neo import Graph

class DesignGenerator(BaseTool):
    name = "DesignGenerator"
    description = "Generates comprehensive kitchen designs by retrieving cases from a knowledge graph."

    def __init__(self, kg_uri, kg_user, kg_password):
        self.graph = Graph(kg_uri, auth=(kg_user, kg_password))

    def _run(self, user_requirements: str) -> str:
        """Retrieve relevant design cases from the knowledge graph."""
        query = f"MATCH (d:DesignCase) WHERE d.requirements CONTAINS '{user_requirements}' RETURN d LIMIT 5"
        results = self.graph.run(query).data()

        if results:
            return "Top 5 design cases: " + ", ".join([result['d']['name'] for result in results])
        else:
            return "No matching design cases found."

    async def _arun(self, user_requirements: str) -> str:
        raise NotImplementedError("Async method is not implemented.")

# Usage Example:
# design_generator = DesignGenerator("bolt://localhost:7687", "neo4j", "password")
# cases = design_generator._run("minimalistic design")
