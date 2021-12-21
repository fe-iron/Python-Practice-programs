'''
    Author: Faiz Elahi
    github Profile: https://github.com/fe-iron
    LinkedIn Profile: https://www.linkedin.com/in/faiz-elahi-13204b132/
    Python | Django Developer
'''

import urllib.request
import json
from urllib.error import HTTPError

ifsc = input("Enter the IFSC of your bank ")
url = f'https://ifsc.razorpay.com/{ifsc}'
data = None
try:
    r = urllib.request.urlopen(url)
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
except HTTPError:
    print("Sorry following IFSC Code is invalid!")

if data:
    print("Bank Name: ", data['BANK'])
    print("Branch: ", data['BRANCH'])
    print("Address: ", data['ADDRESS'])
    print("Contact: ", data['CONTACT'])
    print("City: ", data['CITY'])
    print("District: ",data['DISTRICT'])
    print("State: ",data['STATE'])


