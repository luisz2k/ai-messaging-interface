import json
import os

class WorkflowManager:
    def __init__(self):
        self.workflows = {}
        self.agents = {}
        self.active_workflow = None

    def load_workflows(self, directory):
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                with open(os.path.join(directory, filename), 'r') as f:
                    data = json.load(f)
                    if data.get('type') == 'assistant':
                        self.agents[data['config']['name']] = data
                    elif 'name' in data and 'receiver' in data:
                        self.workflows[data['name']] = data

    def set_active_workflow(self, workflow_name):
        if workflow_name in self.workflows:
            self.active_workflow = self.workflows[workflow_name]
            return True
        return False

    def get_active_agents(self):
        if not self.active_workflow:
            return []
        return [agent['config']['name'] for agent in self.active_workflow['receiver']['groupchat_config']['agents']]

workflow_manager = WorkflowManager()