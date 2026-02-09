name=input('Hello and welcome, What is your name? ')
age=int(input('DOB; '))
age=(2026-age)
if age>=18:
    print(f'You are welcome {name}, your are {age} years old')
    print(f'Welcome {name} to home of amazing deals.')
    print('0 Help menu')
    print('1 People close to you')
    print('2 Find a friend')
    print('3 Meet like minded people')
    print('4 Share contct info')
    choose=int(input('Pick your prefferd deal; '))
    choice=int(choose)
    if choice==0:
        print('Help menu')
    elif choice==1:
            print('People close to you')
    elif choice==2:
        print('Find a friend')
    elif choice==3:
        print('Meet like minded people')
    elif choice==4:
            print('Share contact info')
    else:
        print('invalid choice')
else:
    print(f'Sorry {name},{age} years old, is underge')

