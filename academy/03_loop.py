#!/usr/bin/python3.7

users = [
   { 'admin': True, 'active': True, 'name': 'swan' },
   { 'admin': False, 'active': True, 'name': 'bude' },
   { 'admin': False, 'active': False, 'name': 'geru' }
]

for user in users:
    prefix = ""
    if user['admin'] and user['active']:
        prefix = "ACTIVE - (ADMIN) "
    elif user['admin']:
        prefix = "INACTIVE - (ADMIN) "
    elif user['active']:
        prefix = "ACTIVE - "
    else:
        prefix = "INACTIVE - "
    print(prefix + user['name'])
