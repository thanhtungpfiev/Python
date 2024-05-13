todos = open('todos.txt', 'w')
print('Put out the trash.', file=todos)
print('Feed the cat.', file=todos)
print('Prepare tax return.', file=todos)
todos.close()

with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='')
