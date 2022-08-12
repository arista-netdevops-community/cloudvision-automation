"""
pygnmi script
"""

from pprint import pprint as pp
import json
from pygnmi.client import gNMIclient

with open("token.tok") as f:
    TOKEN = f.read().strip('\n')

host = ('192.168.0.5', '443')
with gNMIclient(target=host, token=TOKEN, override="192.168.0.5") as gc:
    result = gc.capabilities()

pp(result) 
