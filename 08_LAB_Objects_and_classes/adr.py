class Trucks:
    def __init__(self, reg_number, reg_tank, adr_data):
        self.reg_number = reg_number
        self.reg_tank = reg_tank
        self.adr_data = adr_data

    def display_info(self):
        return f"Truck number: {self.reg_number}, Tank number: {self.reg_tank}, ADR data: {self.adr_data}"


truck1 = Trucks('', '', '')

while True:
    command = input("Enter a command ('End' to exit or 'Add' to add a truck): ").strip()
    if command == 'End':
        break
    elif command == 'Add':
        truck_num = input("Enter truck number: ")
        tank_num = input("Enter tank number: ")
        adr = input("Enter ADR data: ")
        truck1 = Trucks(truck_num, tank_num, adr)

print(truck1.display_info())
