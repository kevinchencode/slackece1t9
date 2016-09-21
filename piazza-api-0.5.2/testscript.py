from piazza_api import Piazza

p = Piazza()

email = input('Enter your email: ')
password = input('Enter your password: ')
p.user_login(email, password)

user_profile = p.get_user_profile()
classes = p.get_user_classes()
for i in classes:
    print(i['num'])

selected_class = input('Choose class: ')
selected_class = selected_class.lower()
for i in classes:
    if i['num'].lower() == selected_class:
        print ('Course selected, ID = ')
        print (str(i['nid']))
        