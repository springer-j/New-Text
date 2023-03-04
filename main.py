
#------------------------------------------------------

# Newtxt 2.0
# Python 3.10.9
# 3/4/23

from datetime import datetime
import json

#------------------------------------------------------
# Default variables

config_file = "/home/banta/Data/config_newtxt.json"
date_string = "%m/%d/%y"

#------------------------------------------------------
# Import settings from JSON

with open(config_file, 'r') as file:
    config = json.load(file)

use_extension = config['extension']
line_width = config['line_width']
system_name = config['system']

#------------------------------------------------------

def get_date():
    now = datetime.now()
    return now.strftime(date_string)


def divider():
    return '-' * line_width


def format_doc(title):
    return f'''
{divider()}

- Title:    {title} 
- Date:     {get_date()}
- System:   {system_name}

{divider()}



{divider()}

'''


def main():
    file_name = input("[?] File name: ")
    title = input("[?] Document title: ")
    if use_extension:
        file_name += '.txt'
    with open(file_name, 'w') as file:
        file.write(format_doc(title))
    print("[!] File created.")
    return

main()
    
    