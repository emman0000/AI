import emoji
import random

robot_icon = emoji.emojize(":robot:")
print(robot_icon, "THIS IS BOBBIE THE MEDICINE DELIVERY ROBOT")

class Environment:
    def __init__(self):
        self.rooms = {169: None, 420: None, 666: None, 911: None}
        self.storage = {"Methadone": 10, "Oxycontin": 10, "Fentanyl": 10, "Hydrocodone": 10}
        self.nurse_station = True
        self.patient_prescriptions = {169: "Methadone", 420: "Oxycontin", 666: "Fentanyl", 911: "Hydrocodone"}
        
    def get_patient_prescription(self, room):
        """Get the required medicine for a given room"""
        return self.patient_prescriptions.get(room, None)

    def check_storage(self, medicine):
        """Check if the medicine is available in storage"""
        return self.storage.get(medicine, 0) > 0

    def pick_up_medicine(self, medicine):
        """Pick up medicine if available"""
        if self.storage.get(medicine, 0) > 0:
            self.storage[medicine] -= 1
            return True
        return False

    def nurse_alert(self):
        """Alert the nurse if a medicine is unavailable"""
        print(emoji.emojize(":rotating_light:"), "NURSE ALERT! NURSE ALERT! NURSE ALERT!")

    def display(self):
        """Display hospital environment status"""
        print(emoji.emojize(":hospital:"), "ROOMS:", self.rooms)
        print(emoji.emojize(":pill:"), "STORAGE:", self.storage)
        print(emoji.emojize(":nurse:"), "NURSE STATION:", self.nurse_station)
        print(emoji.emojize(":clipboard:"), "PATIENT PRESCRIPTIONS:", self.patient_prescriptions)

class Robot:
    def __init__(self, environment):
        self.environment = environment
        self.current_room = "Medicine Storage"
        self.current_medicine = None  # Corrected attribute name

    def move(self, location):
        """Move to a specified location"""
        self.current_room = location
        print(emoji.emojize(":robot:"), f"Moving to {location} {emoji.emojize(':pickup_truck:')}")

    def pick_up(self, medicine):
        """Pick up medicine if available"""
        if self.environment.pick_up_medicine(medicine):
            self.current_medicine = medicine
            print(emoji.emojize(":robot:"), f"Picking up {medicine} {emoji.emojize(':pill:')}")
        else:
            print(emoji.emojize(":robot:"), f"Medicine {medicine} not available! {emoji.emojize(':rotating_light:')} Nurse Alert!")
            self.environment.nurse_alert()

    def scan_room(self, room):
        """Scan room before delivering medicine"""
        print(emoji.emojize(":robot:"), f"Scanning room {room} for patient prescription... {emoji.emojize(':satellite:')}")
        prescription = self.environment.get_patient_prescription(room)
        print(emoji.emojize(":check_mark_button:"), f"Scan complete! Patient in room {room} needs {prescription}")

    def deliver_medicine(self, room):
        """Deliver medicine to the patient"""
        if self.current_medicine:
            print(emoji.emojize(":robot:"), f"Delivering {self.current_medicine} to room {room} {emoji.emojize(':package:')}")
            self.current_medicine = None  # Reset medicine after delivery
        else:
            print(emoji.emojize(":warning:"), "No medicine to deliver!")

    def execute_delivery(self):
        """Execute medicine deliveries based on patient prescriptions"""
        for room, medicine_needed in self.environment.patient_prescriptions.items():
            self.move("Medicine Storage")
            if self.environment.check_storage(medicine_needed):
                self.pick_up(medicine_needed)
                self.move(room)
                self.scan_room(room)
                self.deliver_medicine(room)
            else:
                print(emoji.emojize(":robot:"), f"Medicine {medicine_needed} not available! {emoji.emojize(':rotating_light:')} Nurse Alert!")

# Initialize environment and robot
hospital = Environment()
robot = Robot(hospital)

# Run the delivery system
robot.execute_delivery()
