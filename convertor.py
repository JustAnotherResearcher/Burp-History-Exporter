import sys
import xml.etree.ElementTree as ET
import base64
import random

file_name = sys.argv[1]

tree = ET.parse(file_name)
root = tree.getroot()

# get the request from the xml file
for item in root.iter('item'):
    request_data = item.find('request')
    # convert base64 encoded request to bytes
    request_bytes = request_data.text.encode('utf-8')
    # decode the bytes
    request_decoded = base64.b64decode(request_bytes).decode("utf-8")
    # save the decoded request to a new file
    with open("request_" + str(random.randint(0,50000000)) + ".txt", "w") as f:
        f.write(request_decoded)