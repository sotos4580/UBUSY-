#Network scanning utility
import subprocess
from subprocess import Popen, PIPE
import re
import time

# Function for current time in minutes from timestamp
current_min_time = lambda: int(round(time.time()) / 60)

def get_active_hosts():
    import firebasenet
    # ----- Bypass Sudo -----
    sudo_password = 'skyrim'
    command = '-'
    command = command.split()

    cmd1 = subprocess.Popen(['echo',sudo_password], stdout=subprocess.PIPE)
    cmd2 = subprocess.Popen(['sudo','echo'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE)
    # ----- End-Bypass Sudo -----

    with Popen(['sudo', 'arp-scan', '-l', '-r', '5'], stdout = PIPE) as proc:
        mac_list = re.compile('\s+((?:[0-9A-Fa-f]{2}:){5}(?:[0-9A-Fa-f]){2})\s+')
        mac_list = mac_list.findall(proc.stdout.read().decode('utf-8'))
        #raw_data = (proc.stdout.read().decode('utf-8'))
    return mac_list

def count_active_hosts():
    return len(get_active_hosts())
