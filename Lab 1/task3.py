#reflexive agent 
#create an environment with list of backup tasks either completed or failed
#randomly successful tasks after retrying

import random 

class Environment:
    def __init__(self):
        self.backups = [random.choice(["Completed", "Failed"]) for _ in range(5)]
    def get_percept(self, index):
        return self.backups[index]
    def update_status(self, index, new_status):
        self.backups[index] = new_status
    def display_backups(self):
        print("Backup Status: ", self.backups)
        
class BackupAgent:
    def __init__(self, environment):
        self.environment = environment
        self.environment = environment
    def retry_backup(self):
        for i in range(len(self.environment.backups)):
            status = self.environment.get_percept(i)
            if status == "Failed":
                print(f"Retrying Backup {i}")
                if random.choice([True, False]):
                    self.environment.update_status(i, "Completed")
                    print(f"Backup {i} completed successfully.")
                else:
                    print(f"Backup {i} failed again.")
                    
    def run(self):
        print("Initial Backup Status:")
        self.environment.display_backups()
        
        print("\nRetrying Backups...")
        self.retry_backup()
        
        print("\nUpdated Backup Status:")
        self.environment.display_backups()
        
    
environment = Environment()
agent = BackupAgent(environment)
agent.run()
