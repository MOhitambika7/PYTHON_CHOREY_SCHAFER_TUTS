message = 'Hello World'
print(message.count('Hello'))
print(message.count('H'))
print(message.count('l'))
print(message.count('World'))
print(message.find('World'))
'''World starts at the sixth index of the message variable so it will show 6 in terminal'''

new_message = message.replace('World', 'Universe')
print(new_message)


greeting = 'HELLO'
name = 'Michael'

Message = greeting + ',' + name + '.welcome!'
print(Message)

Message = '{}, {}. Welcome!'.format(greeting, name)
print(Message)
'''For the alternative of format string aove '''

print(dir(name)) 
'''Using dir(name) with name as a string variable (in this case, 'Michael'), it will display the methods and properties specific to string objects in Python.'''

print(help(str))
print(help(str.lower))
