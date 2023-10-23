class Comment:
    def __init__(self, username, content):
        self.username = username
        self.content = content

    def display_info(self):
        return f"{self.username}\n{self.content}"


# Създаваме списък, в който ще съхраняваме коментарите
comments = []

while True:
    command = input()

    if command == 'Stop':
        break

    username, content = command.split(', ')
    comment = Comment(username, content)
    comments.append(comment)


# Показваме информацията за всички коментари
for comment in comments:
    print(comment.display_info())
