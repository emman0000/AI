import emoji
import time

class Building:
    def __init__(self):
        """Initialize the environment (3x3 grid) with fire and safe rooms"""
        self.grid = {
            'a': "safe", 'b': "safe", 'c': "fire",
            'd': "safe", 'e': "fire", 'f': "safe",
            'g': "safe", 'h': "safe", 'j': "fire"
        }

    def check_fire(self, room):
        """Check if the room has fire"""
        return self.grid[room] == "fire"

    def extinguish_fire(self, room):
        """Extinguish fire in the given room"""
        self.grid[room] = "safe"

    def display_grid(self):
        """Display the building status using emoji keywords"""
        print("\nCurrent Building Status:")
        print(f"a: {emoji.emojize(':check_mark_button:') if self.grid['a'] == 'safe' else emoji.emojize(':fire:')}  "
              f"b: {emoji.emojize(':check_mark_button:') if self.grid['b'] == 'safe' else emoji.emojize(':fire:')}  "
              f"c: {emoji.emojize(':check_mark_button:') if self.grid['c'] == 'safe' else emoji.emojize(':fire:')}")
        print(f"d: {emoji.emojize(':check_mark_button:') if self.grid['d'] == 'safe' else emoji.emojize(':fire:')}  "
              f"e: {emoji.emojize(':check_mark_button:') if self.grid['e'] == 'safe' else emoji.emojize(':fire:')}  "
              f"f: {emoji.emojize(':check_mark_button:') if self.grid['f'] == 'safe' else emoji.emojize(':fire:')}")
        print(f"g: {emoji.emojize(':check_mark_button:') if self.grid['g'] == 'safe' else emoji.emojize(':fire:')}  "
              f"h: {emoji.emojize(':check_mark_button:') if self.grid['h'] == 'safe' else emoji.emojize(':fire:')}  "
              f"j: {emoji.emojize(':check_mark_button:') if self.grid['j'] == 'safe' else emoji.emojize(':fire:')}")
        print("-" * 30)

class FirefightingRobot:
    def __init__(self, environment):
        """Initialize the robot with a reference to the environment"""
        self.environment = environment
        self.robot_icon = ":robot:"
        self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']

    def move(self, room):
        """Move the robot to a room"""
        print(emoji.emojize(self.robot_icon), f"Moving to room {room} :fire_engine:")

    def scan_and_extinguish(self, room):
        """Scan the room for fire and extinguish it if needed"""
        if self.environment.check_fire(room):
            print(emoji.emojize(":fire:"), f"Fire detected in room {room}! Extinguishing fire... (:fire_engine:)")
            self.environment.extinguish_fire(room)
            print(emoji.emojize(":check_mark_button:"), f"Fire in room {room} has been extinguished!")

    def execute_mission(self):
        """Execute the fire extinguishing mission"""
        print(emoji.emojize(":fire_engine:"), "Firefighting Robot Activated!\n")
        self.environment.display_grid()

        for room in self.path:
            self.move(room)
            self.scan_and_extinguish(room)
            time.sleep(1)  # Simulate movement delay
            self.environment.display_grid()

        print(emoji.emojize(":partying_face:"), "All fires have been extinguished! Building is safe! :tada:")

# Initialize environment and robot
building = Building()
robot = FirefightingRobot(building)

# Run the firefighting mission
robot.execute_mission()
