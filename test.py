import re

import tkinter
from tkinter import *
from pyad import pyad, aduser
import random
import string
from tkinter import ttk
import secrets


# def connection_to_server():
#
#     pyad.set_defaults(ldap_server="KMSAD02.kubis.ru",
#                               username="f.burov",
#                               password="MSUMCFZZ342511m")
#     user = aduser.ADUser.from_cn('Fedor Burov')
#     return str(user)
#
# assert connection_to_server() == "<ADUser 'CN=Fedor Burov,OU=GPO Test,OU=Servicedesk,OU=IT,OU=USERS MSK,DC=kubis,DC=ru'>", 'Проверьте подключение к серверу'

# def create_password():
#
#     length = 8
#     chars = string.ascii_letters + string.digits + '!@#$%^*()'
#     while True:
#         user_password = ''.join(secrets.choice(chars) for i in range(length))
#         if (sum(c.islower() for c in user_password) == 2
#                 and sum(c.isupper() for c in user_password) == 2
#                 and sum(c.isdigit() for c in user_password) == 2):
#             break
#
#     return user_password
#
#
# for i in range(1000):
#     print(create_password())




