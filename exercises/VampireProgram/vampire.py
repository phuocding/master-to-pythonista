
 # This program is for those whose names is Alice. it will crash if name is otherwise

name  = str(input('Enter name:'))

age = int(input('Enter age:'))

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
