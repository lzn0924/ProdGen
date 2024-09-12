from langchain.tools import BaseTool
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class ConceptGenerator(BaseTool):
    name = "ConceptGenerator"
    description = "Generates creative kitchen design concepts based on design prompts."

    def _run(self, design_prompt: str) -> str:
        """Generate design concepts based on a prompt."""
        # Load the model and tokenizer
        tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()

        # Tokenize the input prompt
        inputs = tokenizer(design_prompt, return_tensors="pt").to('cuda')

        # Generate a response
        with torch.no_grad():
            output = model.generate(**inputs, max_length=100)

        # Decode the output
        concept = tokenizer.decode(output[0], skip_special_tokens=True)
        return concept

    async def _arun(self, design_prompt: str) -> str:
        raise NotImplementedError("Async method is not implemented.")

# Usage Example:
# concept_generator = ConceptGenerator()
# concept = concept_generator._run("sustainable kitchen with minimalistic design")
