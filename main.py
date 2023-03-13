import requests, uuid, os

BASEURL = "https://www.zombsroyale.io/api/"
try: open("key.txt", "x")
except Exception: pass
with open("key.txt", "r") as f:
  USERKEY = f.read()

def resfile(type, response):
  filename = f"res_{type}_{uuid.uuid4()}.json"
  with open(filename, "w") as f:
    f.write(response)
    return filename

def newcommand():
  command = input("> ").lower()
  match command:
    case ".help" | ".h":
      print("=== Commands List ===")
      print(".h -> This list")
      print(".key -> Set your default user key")
      print(".clanlist -> List of all clans")
      print(".joinclan -> Join a clan")
      print(".createclan -> Create a clan")
      print(".leaveclan -> Leave a clan")
      print(".data -> Get your full userdata")
      print(".config -> Some weird zr api endpoint idk")
      print(".clearsessions -> Clear sessions (dangerous)")
      print(".changeusername -> Change your username (charges 40 gems)")
      print(".shop -> All cosmetics/packs in game")
      print(".rewardtracks -> Your battlepass progress")
      print(".rewards -> Some weird endpoint 2")
      print(".quests -> Your available quests")
      print(".polls -> Your available polls")
      print(".leadboards -> Current leaderboard")
    case ".key" | ".k":
      new = input("Insert new user key: ")
      with open("key.txt", "w") as f:
        if new == None or new == "": 
          print("[ERROR] Empty input")
        else: 
          f.write(new)
          print("[SUCCESS] Default key has been changed")
    case ".clanslist" | ".clans" | ".cl":
      res = requests.get(f"{BASEURL}clan/available")
      try:
        res.raise_for_status()
      except requests.exceptions.HTTPError as err:
          print(f"[ERROR] Something went wrong!\n{err}")
      else:
          filename = resfile("clanavailable", res.text)
          print(f"[SUCCESS] Response has been saved at\n{os.path.dirname(os.path.realpath(__file__))}\{filename}")
    case ".joinclan" | ".jc" | ".join":
      if USERKEY is None or USERKEY == "":
        print("[ERROR] YOUR DEFAULT USERKEY IS EMPTY! SET IT UP BEFORE RUNNING COMMANDS!")
      else: 
        clanid = input("Insert Clan ID: ")
        res = requests.post(f"{BASEURL}clan/{clanid}/join?userKey={USERKEY}")
        try:
          res.raise_for_status()
        except requests.exceptions.HTTPError as err:
          print(f"[ERROR] Something went wrong!\n{err}")
        else:
          if res.json()['status'] == "error":
            print(f"[ERROR] Something went wrong!\n{res.json()['message']}")
          else:
            filename = resfile("clanjoin", res.text)
            print(f"[SUCCESS] Response has been saved at\n{os.path.dirname(os.path.realpath(__file__))}\{filename}")
    case ".createclan" | ".cc" | ".create":
      if USERKEY is None or USERKEY == "":
        print("[ERROR] YOUR DEFAULT USERKEY IS EMPTY! SET IT UP BEFORE RUNNING COMMANDS!")
      else:
        clantag = input("Clan Tag: ")
        clanname = input("Clan Name: ")
        clandesc = input("Clan Description(?): ")
        params = {
          "tag": clantag,
          "name": clanname
        }
        if len(clandesc) > 0: 
          params['description'] = clandesc
        res = requests.post(f"{BASEURL}clan/create?userKey={USERKEY}", params=params)
        print(params)
        try:
          res.raise_for_status()
        except requests.exceptions.HTTPError as err:
          print(f"[ERROR] Something went wrong!\n{err}")
        else:
          if res.json()['status'] == "error":
            print(f"[ERROR] Something went wrong!\n{res.json()['message']}")
          else:
            filename = resfile("clancreate", res.text)
            print(f"[SUCCESS] Response has been saved at\n{os.path.dirname(os.path.realpath(__file__))}\{filename}")
    case ".leaveclan" | ".leave" | ".lc":
      if USERKEY is None or USERKEY == "":
        print("[ERROR] YOUR DEFAULT USERKEY IS EMPTY! SET IT UP BEFORE RUNNING COMMANDS!")
      else:
        clanid = input("Insert Clan ID: ")
        res = requests.post(f"{BASEURL}clan/{clanid}/leave?userKey={USERKEY}")
        try:
          res.raise_for_status()
        except requests.exceptions.HTTPError as err:
          print(f"[ERROR] Something went wrong!\n{err}")
        else:
          if res.json()['status'] == "error":
            print(f"[ERROR] Something went wrong!\n{res.json()['message']}")
          else:
            filename = resfile("clanleave", res.text)
            print(f"[SUCCESS] Response has been saved at\n{os.path.dirname(os.path.realpath(__file__))}\{filename}")
    case ".data" | ".userdata" | ".d":
      if USERKEY is None or USERKEY == "":
        print("[ERROR] YOUR DEFAULT USERKEY IS EMPTY! SET IT UP BEFORE RUNNING COMMANDS!")
      else:
        res = requests.get(f"{BASEURL}user/{USERKEY}")
        try:
          res.raise_for_status()
        except requests.exceptions.HTTPError as err:
          print(f"[ERROR] Something went wrong!\n{err}")
        else:
          if res.json()['status'] == "error":
            print(f"[ERROR] Something went wrong!\n{res.json()['message']}")
          else:
            filename = resfile("user", res.text)
            print(f"[SUCCESS] Response has been saved at\n{os.path.dirname(os.path.realpath(__file__))}\{filename}")
    case ".config" | ".cfg":
      res = requests.get(f"{BASEURL}config")
      try:
        res.raise_for_status()
      except requests.exceptions.HTTPError as err:
        print(f"[ERROR] Something went wrong!\n{err}")
      else:
        if res.json()['status'] == "error":
          print(f"[ERROR] Something went wrong!\n{res.json()['message']}")
        else:
          filename = resfile("config", res.text)
          print(f"[SUCCESS] Response has been saved at\n{os.path.dirname(os.path.realpath(__file__))}\{filename}")
    case ".clearsessions" | ".cls":
      if USERKEY is None or USERKEY == "":
        print("[ERROR] YOUR DEFAULT USERKEY IS EMPTY! SET IT UP BEFORE RUNNING COMMANDS!")
      else:
        confirm = input("[WARNING] This will clear all your login sessions. Please write CONFIRM to confirm that you really want to do this")
        if confirm == "CONFIRM":
          res = requests.post(f"{BASEURL}user/{USERKEY}/clear-sessions")
          try:
            res.raise_for_status()
          except requests.exceptions.HTTPError as err:
            print(f"[ERROR] Something went wrong!\n{err}")
          else:
            if res.json()['status'] == "error":
              print(f"[ERROR] Something went wrong!\n{res.json()['message']}")
            else:
              filename = resfile("clearsessions", res.text)
              print(f"[SUCCESS] Response has been saved at\n{os.path.dirname(os.path.realpath(__file__))}\{filename}")
        else:
          print("[WARNING] Action cancelled.")
    case ".changeusername" | ".changename" | ".username":
      if USERKEY is None or USERKEY == "":
        print("[ERROR] YOUR DEFAULT USERKEY IS EMPTY! SET IT UP BEFORE RUNNING COMMANDS!")
      else:
        confirm = input("[WARNING] This will clear all your login sessions. Please write CONFIRM to confirm that you really want to do this")
        if confirm == "CONFIRM":
          username = input("Insert new username: ")
          res = requests.post(f"{BASEURL}user/{USERKEY}/friend-code/update", params = {"name": username})
          try:
            res.raise_for_status()
          except requests.exceptions.HTTPError as err:
            print(f"[ERROR] Something went wrong!\n{err}")
          else:
            if res.json()['status'] == "error":
              print(f"[ERROR] Something went wrong!\n{res.json()['message']}")
            else:
              filename = resfile("friendcodeupdate", res.text)
              print(f"[SUCCESS] Response has been saved at\n{os.path.dirname(os.path.realpath(__file__))}\{filename}")
        else:
          print("[WARNING] Action cancelled.")
    case ".shop" | ".shopavailable":
      res = requests.get(f"{BASEURL}shop/available")
      try:
        res.raise_for_status()
      except requests.exceptions.HTTPError as err:
        print(f"[ERROR] Something went wrong!\n{err}")
      else:
        if res.json()['status'] == "error":
          print(f"[ERROR] Something went wrong!\n{res.json()['message']}")
        else:
          filename = resfile("shopavailable", res.text)
          print(f"[SUCCESS] Response has been saved at\n{os.path.dirname(os.path.realpath(__file__))}\{filename}")
    case ".rewardtracks":
      if USERKEY is None or USERKEY == "":
        print("[ERROR] YOUR DEFAULT USERKEY IS EMPTY! SET IT UP BEFORE RUNNING COMMANDS!")
      else:
        res = requests.get(f"{BASEURL}reward/tracks", params={"userKey":USERKEY})
        try:
          res.raise_for_status()
        except requests.exceptions.HTTPError as err:
          print(f"[ERROR] Something went wrong!\n{err}")
        else:
          if res.json()['status'] == "error":
            print(f"[ERROR] Something went wrong!\n{res.json()['message']}")
          else:
            filename = resfile("rewardtracks", res.text)
            print(f"[SUCCESS] Response has been saved at\n{os.path.dirname(os.path.realpath(__file__))}\{filename}")
    case ".rewards":
      if USERKEY is None or USERKEY == "":
        print("[ERROR] YOUR DEFAULT USERKEY IS EMPTY! SET IT UP BEFORE RUNNING COMMANDS!")
      else:
        res = requests.get(f"{BASEURL}user/{USERKEY}/rewards")
        try:
          res.raise_for_status()
        except requests.exceptions.HTTPError as err:
          print(f"[ERROR] Something went wrong!\n{err}")
        else:
          if res.json()['status'] == "error":
            print(f"[ERROR] Something went wrong!\n{res.json()['message']}")
          else:
            filename = resfile("rewards", res.text)
            print(f"[SUCCESS] Response has been saved at\n{os.path.dirname(os.path.realpath(__file__))}\{filename}")
    case ".quests":
      if USERKEY is None or USERKEY == "":
        print("[ERROR] YOUR DEFAULT USERKEY IS EMPTY! SET IT UP BEFORE RUNNING COMMANDS!")
      else:
        res = requests.get(f"{BASEURL}quest/available", params = {"userKey": USERKEY})
        try:
          res.raise_for_status()
        except requests.exceptions.HTTPError as err:
          print(f"[ERROR] Something went wrong!\n{err}")
        else:
          if res.json()['status'] == "error":
            print(f"[ERROR] Something went wrong!\n{res.json()['message']}")
          else:
            filename = resfile("questsavailable", res.text)
            print(f"[SUCCESS] Response has been saved at\n{os.path.dirname(os.path.realpath(__file__))}\{filename}")
    case ".polls":
      if USERKEY is None or USERKEY == "":
        print("[ERROR] YOUR DEFAULT USERKEY IS EMPTY! SET IT UP BEFORE RUNNING COMMANDS!")
      else:
        res = requests.get(f"{BASEURL}poll/available", params = {"userKey": USERKEY})
        try:
          res.raise_for_status()
        except requests.exceptions.HTTPError as err:
          print(f"[ERROR] Something went wrong!\n{err}")
        else:
          if res.json()['status'] == "error":
            print(f"[ERROR] Something went wrong!\n{res.json()['message']}")
          else:
            filename = resfile("pollsavailable", res.text)
            print(f"[SUCCESS] Response has been saved at\n{os.path.dirname(os.path.realpath(__file__))}\{filename}")
    case ".leaderboards" | ".leaderboard" |".lb":
      if USERKEY is None or USERKEY == "":
        print("[ERROR] YOUR DEFAULT USERKEY IS EMPTY! SET IT UP BEFORE RUNNING COMMANDS!")
      else:
        lbmode = input("Mode: ")
        lbtime = input("Time: ")
        lbcat = input("Category: ")
        params = {
          "userKey": USERKEY,
          "mode": lbmode,
          "time": lbtime,
          "category": lbcat
        }
        res = requests.get(f"{BASEURL}leaderboard/live", params = params)
        try:
          res.raise_for_status()
        except requests.exceptions.HTTPError as err:
          print(f"[ERROR] Something went wrong!\n{err}")
        else:
          if res.json()['status'] == "error":
            print(f"[ERROR] Something went wrong!\n{res.json()['message']}")
          else:
            filename = resfile("leaderboardslive", res.text)
            print(f"[SUCCESS] Response has been saved at\n{os.path.dirname(os.path.realpath(__file__))}\{filename}")
  newcommand()

print("ZombsRoyale.io API Utils")
print("Run .help for a commands list")
if USERKEY is None or USERKEY == "": print("[WARNING] YOUR DEFAULT USERKEY IS EMPTY! SET IT UP BEFORE RUNNING OTHER COMMANDS!")
newcommand()
