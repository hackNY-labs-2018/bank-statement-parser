'''
Generates a random secret key for `instance/config.py`
(used to encrypt cookies and save in browser)

From https://gist.github.com/geoffalday/2021517
'''

import os, binascii
print('\nGenerating a secret key...')
print('Copy and paste the following in `instance/config.py` as the SECRET entry:')
print(binascii.hexlify(os.urandom(24)))
print('')