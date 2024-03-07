dict_abbreviation = {'API': 'Application Programming Interface',
                     'IDE': 'Integrated Development Environment',
                     'SDK': 'Software Development Kit',
                     'UI': 'User Interface'}

dict_abbreviation['UE'] = 'User Experience'
dict_abbreviation['SSH'] = 'Secure Shell'

user_abbreviation = input("Enter an abbreviation: ")

if user_abbreviation in dict_abbreviation:
    for i in dict_abbreviation:
        if user_abbreviation == i:
            print(dict_abbreviation[user_abbreviation])
else:
    print("Abbreviation not found")
