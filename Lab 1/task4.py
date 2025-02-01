#utility based agent - we reach a conclusion after evaluating the utility of the action
import random 

class Environment:
    def __init__(self):
        self.components = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.vulnerabilities = {comp: random.choice(["Safe", "Low Risk", "High Risk"]) for comp in self.components} 
    def get_percept(self, component):
        return self.vulnerabilities[component]
    def update_status(self, component, new_status):
        self.vulnerabilities[component] = new_status
    def display_vulnerabilities(self):
        print("Vunerability of components: ")
        for component, status in self.vulnerabilities.items():
            print(f"{component}: {status}")
            
class SecurityAgent:
    def __init__(self, environment):
        self.environment = environment
    def scan_system(self):
        """Scan the system and log the vulnerability status of each component."""
        print("\nScanning system for vulnerabilities...")
        for component in self.environment.components:
            status = self.environment.get_percept(component)
            if status == "Safe":
                print(f"✅ Component {component} is Safe.")
            elif status == "High Risk":
                print(f"🚨 WARNING! High Risk Vulnerability detected in {component}. Requires premium service!")
            elif status == "Low Risk":
                print(f"⚠️ Warning: Low Risk Vulnerability detected in {component}. Patching now...")
                self.environment.update_status(component, "Safe")
    def run_security_checks(self):
        print("Initial Vulnerability Status:")
        self.environment.display_vulnerabilities()
        
        self.scan_system()
        
        print("\nUpdated Vulnerability Status:")
        self.environment.display_vulnerabilities()
        
environment = Environment()
agent = SecurityAgent(environment)
agent.run_security_checks()
