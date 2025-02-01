   #create 5 servers 
    #each server has a three states underloaded , overloaded , balanced
    #load balancer agent scans the system overload -> underload  to balance the system 
    #after balancing load display the updated status of the servers
import random #we will take a random server to check the status of the server
class Environment:
    def __init__(self):
        self.servers = ['underloaded','overloaded','balanced','underloaded','overloaded']
    def get_percept(self, server):
        return self.servers[server]
    def change_status(self, server , new_state):
        self.servers[server] = new_state
    def display_servers(self):
        print("Status of Server: ",self.servers)
        
class LoadBalancerAgent:
    def __init__(self,environment):
        self.environment = environment
    def balance_load(self):
       underloaded_servers = []
       overloaded_servers = []
       
       for i in range(len(self.environment.servers)):
           status = self.environment.get_percept(i)
           if status == 'underloaded':
                 underloaded_servers.append(i)
           elif status == 'overloaded':
                 overloaded_servers.append(i)
        
       while overloaded_servers and underloaded_servers:
           over = overloaded_servers.pop()
           under = underloaded_servers.pop()
        
           self.environment.change_status(over,'balanced')
           self.environment.change_status(under,'balanced')
           print(f"Balancing Server {over} and Server {under}")
           
    def run(self):
        print("Server Status Before Balancing: ")
        self.environment.display_servers()
        
        print("\n Balancing Servers...")
        self.balance_load()
        
        print("/nServer Status After Balancing: ")
        self.environment.display_servers()        
environment = Environment()
agent = LoadBalancerAgent(environment)
agent.run()
              
              
        
            
             
