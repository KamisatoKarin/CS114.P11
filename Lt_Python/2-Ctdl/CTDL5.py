import re, sys, math

pattern = r'^([0-9A-F]{2}[-]){5}([0-9A-F]{2})'

def is_valid_mac(mac_address):
    print('true') if mac_address else print('false')

while True:
    s = sys.stdin.readline().strip()
    if s == '.':
        break
    is_valid_mac(re.fullmatch(pattern, s))
