"""
#
# Testscript by Mike Vu.
# Used to adapt the piazza api.
# Created: 20/09/2016.
#
"""

from piazza_api import Piazza
import getpass

p = Piazza()
"""
#
# email = input('Enter your email: ')
# password = getpass.getpass('Enter your password: ')
#
"""
email = "mike.vu@mail.utoronto.ca"
password = "i1puvehtoD"[::-1]

p.user_login(email, password)

"""
#
# Get user profile and classes.
#
"""
user_profile = p.get_user_profile()
classes = p.get_user_classes()
for i in classes:
    print(i['num'])

"""
#
# Class selector.
#
"""
selected_class_string = input('Choose class: ')
selected_class_string = selected_class_string.lower()
selected_class = None
for i in classes:
    if i['num'].lower() == selected_class_string:
        selected_class = i
    
print(i)

"""
#
# Get network data for the class.
#
"""
ece241 = p.network(i['nid'])
#ece241.get_post(1)
posts = ece241.iter_all_posts(1)
for post in posts:
    print(post)
    
## TODO: CREATE A OBJECT/CLASS FOR POST

"""
#
# Structure for post objects:
# see '/post_response_format.txt'
#
"""