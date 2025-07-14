from .sub_agents.validator_agent import validator_agent
from .sub_agents.care_advice_agent import care_advice_agent
from google.adk.agents import SequentialAgent

root_agent = SequentialAgent(
    name="manager",
    sub_agents=[validator_agent,care_advice_agent],
    description="A pipeline that validates and provide a care advice for older people",
)
