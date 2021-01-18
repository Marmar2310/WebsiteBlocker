import time
from datetime import datetime as dt

sites_blocked = [
    "www.twitter.com", "twitter.com",
    "www.instagram.com", "instagram.com"
]

Linux_host = "/etc/hosts"            # Also works for Apple OS
Windows_host = r"C:\Windows\System32\drivers\etc\host"
host_used = Linux_host
redirect = "127.0.0.1"

def block_websites(start_hour, end_hour):
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, start_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,end_hour):
            print("Concentrate on your work man!")
            with open(host_used, 'r+') as hostfile:
                hosts = hostfile.read()
                for site in sites_blocked:
                    if site not in hosts:
                        hostfile.write(redirect + ' ' + site + '\n')
        else:
            with open(host_used, 'r+') as hostfile:
                hosts = hostfile.readlines()
                hostfile.seek(0)
                for host in hosts:
                    if not any(site in host for site in sites_blocked):
                        hostfile.write(host)
                hostfile.truncate()
            print("Good job, you can rest now!")
        time.sleep(3)

if __name__ == '__main__':
    block_websites(16, 17)