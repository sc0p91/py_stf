#!/usr/bin/python3.7

################### SWANE LÖSIG ##########################
#user={'admin': False, 'active': False, 'name': "swan"}
#
#if user['admin'] and user['active']:
#    print(f"ACTIVE - (ADMIN) {user['name']}")
#
#elif user['admin']:
#    print(f"(ADMIN) {user['name']}")
#
#elif user['active']:
#    print(f"ACTIVE {user['name']}")
#
#else:
#    print(f"Not active, nor admin {user['name']}")

################### RICHTIGI LÖSIG #######################
user = { 'admin': True, 'active': True, 'name': 'Kevin' }
prefix = ""

if user['admin'] and user['active']:
    prefix = "ACTIVE - (ADMIN) "
elif user['admin']:
    prefix = "(ADMIN) "
elif user['active']:
    prefix = "ACTIVE - "

print(prefix + user['name'])
