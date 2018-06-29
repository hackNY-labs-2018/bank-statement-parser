'''
Generates a random secret key for `instance/config.py`
(used to encrypt cookies and save in browser)

From https://gist.github.com/geoffalday/2021517
'''

import os, binascii
print('\nGenerating a secret key...')
print('Create or edit the file `instance/config.py`, to include the line')
print('SECRET = `xxx` replacing `xxx` with the below:')
print(binascii.hexlify(os.urandom(24)))
print('')