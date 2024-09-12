from langchain import LLMChain, PromptTemplate
from langchain.tools import BaseTool
import pandas as pd
import spacy


class RequirementAnalyzer(BaseTool):
    name = "RequirementAnalyzer"
    description = "Extracts actionable design requirements from market research and feedback data using NLP techniques."
    llm: BaseLLM = None
    nlp = spacy.load('en_core_web_sm')

    def _run(self, input_data: str) -> str:
        """Extract actionable design requirements using NLP."""
        # Process input data
        doc = self.nlp(input_data)

        # Example: Extracting entities that could be design requirements (customize this)
        requirements = [ent.text for ent in doc.ents if ent.label_ in ['ORG', 'PRODUCT', 'GPE']]

        # Analyze and generate output
        if requirements:
            output = "The following design requirements were extracted: " + ", ".join(requirements)
        else:
            output = "No actionable design requirements found."

        return output

    async def _arun(self, input_data: str) -> str:
        """Asynchronous version not implemented."""
        raise NotImplementedError("Async not implemented.")


# Usage example:
analyzer = RequirementAnalyzer()
print(analyzer._run(
    "Based on recent feedback from users and competitor analysis, it is clear that ease of use and better integration with existing products are needed."))
