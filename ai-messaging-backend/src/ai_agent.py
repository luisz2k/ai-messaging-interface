from dotenv import load_dotenv
import os
from openai import OpenAI
from src.workflow_manager import workflow_manager

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')[:5]}...")  # Print first 5 characters for verification

def get_ai_response(user_message):
    try:
        active_agents = workflow_manager.get_active_agents()
        if not active_agents:
            return "No active workflow set. Please contact an administrator."

        messages = []
        for agent_name in active_agents:
            agent = workflow_manager.agents.get(agent_name)
            if agent:
                messages.append({"role": "system", "content": agent['config']['system_message']})
                messages.append({"role": "user", "content": user_message})
                
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    temperature=0.7,
                )
                
                agent_response = response.choices[0].message.content.strip()
                messages.append({"role": "assistant", "content": agent_response})

        # The last response will be from the "frontend_engineer" who coordinates the final response
        return agent_response

    except Exception as e:
        print(f"Error in get_ai_response: {str(e)}")
        return "Sorry, I encountered an error while processing your message."