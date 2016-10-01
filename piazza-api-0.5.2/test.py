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
import re
import getpass


def ignore_markup (content):
    """
    #
    # For removing html tags from the content section of a post.
    #
    """
    return re.sub('<.*?>', '', content)

def ignore_html_ascii (content):
    """
    #&
    # Ignore's html ascii codes for special characters.
    #
    """
    return re.sub('&#.*?;', '', content) #this currently isn't working
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
"""
#
#for i in classes:
#    print(i['num'])
## Currently skips printing the classes, since only "ece 241h1f" will be selected
#
"""

"""
#
# Class selector.
# TODO: catch invalid input. However this won't be necessary if the class is
#       statically selected.
# Currently picks "ece 241h1f"
#
"""
#selected_class_string = input('Choose class: ')
#selected_class_string = selected_class_string.lower()
selected_class_string = "ece 241h1f"
selected_class = None
for i in classes:
    # next line currently disabled, used only for debugging
    # print ("{}: {}".format(i['num'],i['num'].lower() == selected_class_string))
    if i['num'].lower() == selected_class_string:
        selected_class = i
        break # because for some reason, selected class is changed every time.

"""
#
# Get network data for the class.
#
"""
ece241 = p.network(i['nid'])
posts = ece241.iter_all_posts(20) # Post limiting

skip_pinned_posts = True; # Temporary testing filter, can be switched off if you want
ignore_content_markup = True;

for post in posts:
    if (skip_pinned_posts and post['bucket_name'] != "Pinned"):
        print ("    TITLE: " + ignore_html_ascii(post['history'][0]['subject']))

        content = post['history'][0]['content']

        # Remove HTML tags, like <p>.
        if (ignore_content_markup):
            content = ignore_markup (content)
        
        # Remove HTML specific ascii characters, such as '&#39;'
        content = ignore_html_ascii(content);
        print (content)
        
        # Print link to post
        print ("See full discussion : LINK=" + "https://piazza.com/class/" + selected_class['nid'] + "?cid=" + str(post['nr']) + "\n")

    #print (post['history'])
    #print ("\n")
    #print (json.dumps(post, sort_keys=True, indent = 4, separators=(',',': ')))

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
