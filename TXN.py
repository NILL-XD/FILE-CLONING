import os
os.system('git pull')
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
  os.system('chmod 777 Nill;./Nill')
