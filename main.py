import random
import requests
import time
import threading
import base64
from termcolor import cprint
file1 = open('Groups.txt', 'r')
Lines = file1.readlines()
file2 = open('People.txt', 'r')
Line = file2.readlines()
file3 = open('Proxies.txt', 'r')
proxies = file3.readlines()
file4 = open('UserAgents.txt', 'r')
userAgents = file4.readlines()
nl = []

for i in userAgents:
  nl.append(i.replace('\n', ''))
userAgents = nl

nl = []
for i in proxies:
  nl.append(i.replace('\n', ''))
proxies = nl

file1.close()
file2.close()
file3.close()
file4.close()

list = []

proxy = random.choice(proxies)
cprint('Enter your token below: ', 'yellow')
token = input("")
headers = {"Authorization":str(token), "User-Agent": random.choice(userAgents)}
response = requests.get("https://discord.com/api/v9/users/787056370288427008/profile?with_mutual_guilds=true", headers=headers, proxies={"http":random.choice(proxies)})

def check(response): 
  if response.status_code == 401:
    cprint('Invalid Token', 'red')
    time.sleep(1)
    print("\033[H\033[J", end="")
    cprint('Enter your token below: ', 'yellow')
    token = input("")
    Nresponse = requests.get("https://discord.com/api/v9/users/787056370288427008/profile?with_mutual_guilds=true", headers={"Authorization":str(token), "User-Agent": random.choice(userAgents)}, proxies={"http":random.choice(proxies)})
    check(Nresponse)

check(response)
print(response.json())
keep_going = True
def key_capture_thread():
    global keep_going
    input()
    keep_going = False

def create():
  c = 0
  threading.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
  cprint('Press enter at any time to stop', 'yellow')
  while c < 100:
    if keep_going:
      c = c + 1
      time.sleep(1)
      data = {'recipients': []}
      response = requests.post("https://discord.com/api/v9/users/@me/channels",headers={"Authorization":str(token), "User-Agent": random.choice(userAgents)},json=data, proxies={"http":random.choice(proxies)})
      try:
        ids = response.json()['id']
        f = open("Groups.txt", "a")
        f.write(f'{ids}')
        f.write(f'\n')
        f.close()
      except:
        cprint("Rate Limited", 'red')
        cprint(response.json(), 'blue')
        time.sleep(int(response.json()['retry_after']))
    else:
      break

def addUser(id):
  for line in Lines:
    line = line.replace('\n', '')
  r = requests.put(f'https://discord.com/api/v9/channels/{line}/recipients/{id}', headers={"Authorization":str(token), "User-Agent": random.choice(userAgents)}, proxies={"http":random.choice(proxies)})
  if r.text == '{"message": "Unknown User", "code": 10013}':
      cprint('Invalid User Id', 'red')
      time.sleep(1)
      ask()
  else:
    f = open("People.txt", "a")
    f.write(f'{id}')
    f.write("\n")
    f.close()

def removeUser(id):
  line = []
  for lines in Line:
    line.append(lines.replace('\n', ''))
  if id in line:
    file = open("People.txt","r+")
    file.truncate(0)
    file.close()
    for i in line:
      f = open("People.txt", "a")
      if not i == id:
        f.write(i)
        f.write("\n")
      f.close()
    cprint('Removed successfully', 'green')
  else:
    cprint('User not found', 'red')

def remove(id):
  for line in Lines:
    line = line.replace('\n', '')
    requests.delete(f"https://discord.com/api/v9/channels/{line}/recipients/{id}", headers={"Authorization":str(token), "User-Agent": random.choice(userAgents)})
class delete:

  def delete(line):
    requests.delete(f"https://discord.com/api/v9/channels/{line}", headers={"Authorization":str(token), "User-Agent": random.choice(userAgents)})

  def start(self):
    for line in Lines:
      threading.Tread(target=self.delete(line))
      lines = []
      lines.append(line.replace('\n', ''))
      file = open("Groups.txt","r+")
      file.truncate(0)
      file.close()
      f = open("Groups.txt", "a")
      lines = []
      for i in Lines:
        lines.append(i.replace('\n', ''))
      file = open("Groups.txt","r+")
      file.truncate(0)
      file.close()
      for i in lines:
        f = open("Groups.txt", "a")
        if not i == line:
          f.write(i)
          f.write("\n")
        f.close()

def clean(list):
  for line in list:
    lines = []
    for i in Lines:
      lines.append(i.replace('\n', ''))
    file = open("Groups.txt","r+")
    file.truncate(0)
    file.close()
    for i in lines:
      f = open("Groups.txt", "a")
      if not i == line:
        f.write(i)
        f.write("\n")
      f.close()
      cprint('Invalid channel. Deleted from id list', 'red')

def ping(gc, user):
  requests.put(f'https://discord.com/api/v9/channels/{gc}/recipients/{user}', headers={"Authorization":str(token), "User-Agent": random.choice(userAgents)}, proxies={"http":random.choice(proxies)})
  requests.delete(f'https://discord.com/api/v9/channels/{gc}/recipients/{user}', headers={"Authorization":str(token), "User-Agent": random.choice(userAgents)}, proxies={"http":random.choice(proxies)})

def add(gc, user):
  r = requests.put(f'https://discord.com/api/v9/channels/{gc}/recipients/{user}', headers={"Authorization":str(token), "User-Agent": random.choice(userAgents)}, proxies={"http":random.choice(proxies)})
  if r.text == '{"message": "Unknown User", "code": 10013}':
      cprint('Invalid User Id', 'red')
      time.sleep(1)
      ask()
  elif r.text == '{"message": "Unknown Channel", "code": 10003}':
    lines = []
    for i in Lines:
      lines.append(i.replace('\n', ''))
    file = open("Groups.txt","r+")
    file.truncate(0)
    file.close()
    list.append(gc)
  else:
    cprint('Added to group chat', 'blue')
    cprint('Press eneter to exit at anytime', 'yellow')

def spam(id):
  threads = []
  for line in Lines:
    threading.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    if keep_going:
      line = line.replace('\n', '')
      t = threading.Thread(target=add,args=(line, id))
      t.start()
      threads.append(t)
    else:
      break
  for thread in threads:
    thread.join()
  threads = []
  for line in Lines:
    threading.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    if keep_going:
      line = line.replace('\n', '')
      for lines in Line:
        lines = lines.replace('\n', '')
        t = threading.Thread(target=ping,args=(line, lines))
        t.start()
        threads.append(t)
      for thread in threads:
        thread.join()
    else:
      break
  if not list == []:
    clean(list)

def rename(name):
  cprint('Press eneter to exit at anytime', 'yellow')
  for line in Lines:
    threading.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    if keep_going:
      print('Renamed groupchat')
      line = line.replace('\n', '')
      requests.patch(f"https://discord.com/api/v9/channels/{line}", headers={"Authorization":str(token), "User-Agent": random.choice(userAgents)}, json={'name': name})
    else:
      break

def changeImg(url):
  cprint('Press eneter to exit at anytime', 'yellow')
  for line in Lines:
    threading.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    if keep_going:
      print('Changed Icon')
      line = line.replace('\n', '')
      requests.patch(f"https://discord.com/api/v9/channels/{line}", headers={"Authorization":str(token), "User-Agent": random.choice(userAgents)}, json={'icon': url})
    else:
      break

def ask():
  options = ['Add User To The Spammer','Remove User From Spammer','Remove User From All Groupchats','Delete Groupchats','Rename Groupchats','Spam User','Change group icon','Help']
  print("\033[H\033[J", end="")
  print('[ ', end='', flush=True)
  cprint('1', 'green', end='', flush=True)
  print(' ] ', end='', flush=True)
  print('Create Groupchats', end='', flush=True)
  for x, i in enumerate(options):
    print()
    print()
    print('[ ', end='', flush=True)
    cprint(x + 2, 'green', end='', flush=True)
    print(' ] ', end='', flush=True)
    print(i, end='', flush=True)
  print()
  print()

  choice = input("> ")

  try:
    if int(choice) == 1:
      cprint('Creating Groupchats...', 'green')
      create()
      time.sleep(1)
      ask()
    elif int(choice) == 2:
      cprint('Enter user id below', 'yellow')
      id = input("")
      addUser(id)
      cprint('Added user!', 'green')
      time.sleep(1)
      ask()
    elif int(choice) == 3:
      cprint('Enter user id below', 'yellow')
      id = input("")
      removeUser(id)
      time.sleep(1)
      ask()
    elif int(choice) == 4:
      cprint('Enter user id below', 'yellow')
      id = input("")
      remove(id)
      cprint('Removed from all groupchats', 'green')
      time.sleep(1)
    elif int(choice) == 5:
      threading.Thread(target=delete.start).start()
      cprint('Deleted all groupchats', 'green')
      time.sleep(1)
      ask()
    elif int(choice) == 6:
      cprint('Enter group chat names below', 'yellow')
      name = input("")
      threading.Thread(target=rename(str(name))).start()
      time.sleep(1)
      ask()
    elif int(choice) == 7:
      cprint('Enter user id below', 'yellow')
      id = input("")
      spam(id)
      for char in 'Done spamming':
        time.sleep(0.1)
        cprint(char, 'magenta', end='', flush=True)
      time.sleep(5)
      ask()
    elif int(choice) == 8:
      cprint('Enter url to image below', 'yellow')
      url = input("")
      try:
        base64.b64encode(requests.get(url).content)
      except:
        cprint('Invalid Url', 'red')
        time.sleep(1.5)
        ask()
      url = str(base64.b64encode(requests.get(url).content)).replace("b'", '')
      changeImg(f'data:image/png;base64,{url}')
      ask()
    elif int(choice) == 9:
      cprint("1.)To create groupchats is to prepare groupchats to add them to. The more groupchats the more pings for them. \n\n2.)To add someone to the spammer is to add them to the list of people who get removed and added to increase the amount of pings. MAKE SURE YOU HAVE THEM ADDED And to remove them is vice versa. You don't need to have them added to remove them.\n\n3.)To delete the group chats is self explanatory. To remove someone from all the groupchats is just to kick them from the groups you just added them to. To spam them is to start the spammer. My discord for help is https://discord.gg/hit and my discord is Ice Bear#8828", 'green')
      input("Press Enter To Exit")
      ask()
    else:
      ask()
  except:
    ask()
ask()
