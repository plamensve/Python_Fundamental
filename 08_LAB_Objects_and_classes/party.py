class Party:
    def __init__(self):
        self.name = []

    def display_info(self):
        return f"Going: {', '.join(self.name)}\nTotal: {len(self.name)}"


party = Party()
command = input()

while command != 'End':
    party.name.append(command)
    command = input()

print(party.display_info())
