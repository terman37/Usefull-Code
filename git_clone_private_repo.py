import os
from getpass import getpass
import urllib

user = 'terman37'
password = getpass('Password: ')
password = urllib.parse.quote(password) # your password is converted into url format
repo_name = 'Neural_Networks_Counting_Fingers'

cmd_string = 'git clone https://{0}:{1}@github.com/{0}/{2}.git'.format(user, password, repo_name)

os.system(cmd_string)
cmd_string, password = "", "" # removing the password from the variable