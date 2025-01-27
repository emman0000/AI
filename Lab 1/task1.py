import random

class SecuritySystem:
    def __init__(self):
        # Initialize the system with random vulnerabilities
        self.components = {chr(65 + i): random.choice(['Safe', 'Vulnerable']) for i in range(9)}

    def display_state(self, title):
        """Displays the current state of the system."""
        print(f"\n{title}:")
        for component, status in self.components.items():
            print(f"Component {component}: {status}")

    def patch_component(self, component):
        """Patches a vulnerable component by marking it as safe."""
        self.components[component] = 'Safe'


class SecurityAgent:
    def __init__(self):
        self.vulnerable_list = []

    def scan_system(self, system):
        """Scans the system and logs vulnerabilities."""
        print("\nSystem Scan:")
        for component, status in system.components.items():
            if status == 'Vulnerable':
                print(f"WARNING: Component {component} is vulnerable!")
                self.vulnerable_list.append(component)
            else:
                print(f"SUCCESS: Component {component} is safe.")

    def patch_vulnerabilities(self, system):
        """Patches all vulnerable components."""
        print("\nPatching Vulnerabilities:")
        for component in self.vulnerable_list:
            system.patch_component(component)
            print(f"Component {component} has been patched and is now safe.")
        self.vulnerable_list.clear()


#Execution Block 
if __name__ == '__main__':
    # Initialize the system and agent
    system = SecuritySystem()
    agent = SecurityAgent()

    # Step 1: Initial System Check
    system.display_state("Initial System State")

    # Step 2: System Scan
    agent.scan_system(system)

    # Step 3: Patching Vulnerabilities
    agent.patch_vulnerabilities(system)

    # Step 4: Final System Check
    system.display_state("Final System State")
