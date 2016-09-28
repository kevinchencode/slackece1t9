"""
#
# Testscript by Mike Vu.
# Used to adapt the piazza api.
# Created: 20/09/2016.
#
"""


def dump_response_to_file (post='', append=False):
    """
    #
    # For debugging: writes the reponse to a file.
    # TODO: check that every time this is called, it doesn't clear the file, and
    #       rather appends to the file.
    #
    """
    f = open('output.txt', 'a' if append else 'w')
    f.write(repr(post))


from piazza_api import Piazza
import post
import json
import getpass

p = Piazza()

email = input('Enter your email: ')
password = getpass.getpass('Enter your password: ')

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
# TODO: catch invalid input.
#
"""
selected_class_string = input('Choose class: ')
selected_class_string = selected_class_string.lower()
selected_class = None
for i in classes:
    print ("{}: {}".format(i['num'],i['num'].lower() == selected_class_string))
    if i['num'].lower() == selected_class_string:
        selected_class = i
        break # because for some reason, selected class is changed every time.
    
print(i)

"""
#
# Get network data for the class.
#
"""
ece241 = p.network(i['nid'])
#ece241.get_post(1)
posts = ece241.iter_all_posts(20) # Post limiting

for post in posts:
    print (post['bucket_name'])
    print (post['history'][0]['subject'])
    #print (post['history'][0]['content'])
    #print (post['history'])
    #print ("\n")
    #print (json.dumps(post, sort_keys=True, indent = 4, separators=(',',': ')))
    
## TODO: CREATE AN OBJECT/CLASS FOR POST?

"""
#
# Structure for post objects:
# see '/post_response_format.txt'
#
"""

"""
#
# Check if the bucket name is "Pinned"
# Skip pinned posts?
# Here would be a good place to branch the function to filter out pinned posts
# or not.
#
"""