from subprocess import check_output
from platform import uname
from time import ctime
PATH_TO_UPDATE_FILE = '/home/infosec-trial-7/update_file'
sys_info = uname()

PAYLOAD = f"""SYSTEM INFORMATION FOR CATS.
(Last updated at {ctime()}.)

{sys_info.version}
{sys_info.system}@{sys_info.release}

Arch is {sys_info.processor}.
Netstat output...

{check_output('netstat', universal_newlines=True)}
"""

with open(PATH_TO_UPDATE_FILE, 'w') as f:
    f.write(PAYLOAD)

