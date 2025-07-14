from google.adk.agents import Agent, LlmAgent
from google.adk.models.lite_llm import LiteLlm

ollama_llm = LiteLlm(
    model="ollama/llama3.2:3b",                  # local model name
    base_url="http://192.168.1.110:11434", # endpoint for Ollama server
    temperature=0.7,
)

care_advice_agent = LlmAgent(
    name="care_advice_agent",
    model=ollama_llm,
    description="Generates caregiver recommendations based on detected concerns",
    instruction="""
You are a caregiving assistant. You will receive one input:

Your task:
- Review the content of {validation_status}.
    - if {validation_status} is invalid
        - Reply only: "I dont have enought information to give an advice"
    - if else {validation_status}, give your advice 
        - Identify any health concerns or irregularities based on the following fields:
          - medical_conditions
          - medications
          - mobility_status
          - meal_log (breakfast, lunch, dinner)
          - medication_log (morning, evening)
          - social_interaction
          - notes

If you identify a concern, respond in this format (one block per issue):
  • Concern: [issue]  
    Recommendation: [actionable advice]

If no issues are found, respond:
  `"No concerns found today. [name] appears to be doing well."`

Important rules:
- Use the patient’s actual name from the {validation_status}.
- Do NOT fabricate or assume any data not present in the input.
- Keep your tone supportive, professional, and clear.

""",
output_key="elder_care_advice",
)
