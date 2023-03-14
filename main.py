from utils import *

BASEURL = "https://www.zombsroyale.io/api/"
dotenv.load_dotenv(dotenv.find_dotenv())
USERKEY = os.environ.get("USERKEY")

def newcommand():
    command = input("> ").lower()
    try:
        match command:
            case ".help" | ".h" | ".commands" | ".list":
                print("=== Commands List ===")
                print(".help -> This list")
                print(".mykey -> Dump your default key in console")
                print(".editkey -> Set your default user key")
                print(".clanlist -> List of all clans")
                print(".createclan -> Create a clan")
                print(".joinclan -> Join a clan")
                print(".leaveclan -> Leave a clan")
                print(".userdata -> Get your full userdata")
                print(".zrconfig -> Some weird zr api endpoint idk")
                print(".clearsessions -> Clear sessions (dangerous)")
                print(".changeusername -> Change your username (charges 40 gems)")
                print(".shop -> All cosmetics/packs in game")
                print(".rewardtracks -> Your battlepass progress")
                print(".rewards -> Some weird endpoint 2")
                print(".quests -> Your available quests")
                print(".polls -> Your available polls")
                print(".leadboard -> Current zr leaderboard")
            case ".mykey":
                print(f"Your current default userkey: {USERKEY}")
                if not validatekey(USERKEY): 
                    log.warning("YOUR DEFAULT USERKEY IS INVALID", True)
            case ".editkey":
                newkey = input("Insert new default userkey: ")
                if validatekey:
                    log.msg(f"Changed default userkey from {USERKEY} to {newkey}", True)
                    dotenv.set_key(dotenv.find_dotenv(), "USERKEY", newkey)
            case ".clanlist" | ".cl":
                makerequest(mode="GET", url=f"{BASEURL}clan/available", type="clanavailable")
            case ".createclan" | ".cc":
                clanname = input("CLAN NAME: ").replace(" ", "%20")
                clantag = input("CLAN TAG: ").replace(" ", "%20")
                clandesc = input("CLAN DESCRIPTION (?): ").replace(" ", "%20")
                nondefkey = input("NON-DEFAULT KEY (?): ")
                params = { "userKey": nondefkey if len(nondefkey) > 0 else USERKEY, "tag": clantag, "name": clanname }
                if len(clandesc) > 0: params['description'] = clandesc
                makerequest(mode="POST", url=f"{BASEURL}clan/create", type="clancreate", params=params)
            case ".joinclan" | ".jc":
                clanid = input("CLAN ID: ")
                nondefkey = input("NON-DEFAULT KEY: ")
                params = { "userKey": nondefkey if len(nondefkey) > 0 else USERKEY }
                makerequest(mode="POST", url=f"{BASEURL}clan/{clanid}/join", type="clanjoin", params=params)
            case ".leaveclan" | ".lc":
                clanid = input("CLAN ID: ")
                nondefkey = input("NON-DEFAULT KEY: ")
                params = { "userKey": nondefkey if len(nondefkey) > 0 else USERKEY }
                makerequest(mode="POST", url=f"{BASEURL}clan/{clanid}/leave", type="clanleave", params=params)
            case ".userdata" | ".data":
                nondefkey = input("NON-DEFAULT KEY: ")
                makerequest(mode="GET", url=f"{BASEURL}user/{nondefkey if len(nondefkey) > 0 else USERKEY}", type="userdata")
            case ".zrconfig":
                makerequest(mode="GET", url=f"{BASEURL}config", type="config")
            case ".clearsessions":
                nondefkey = input("NON-DEFAULT KEY: ")
                confirm = input("Are you sure that you want to do this? Write CONFIRM to confirm.")
                if confirm == "CONFIRM": makerequest(mode="POST", url=f"{BASEURL}user/{nondefkey if len(nondefkey) > 0 else USERKEY}/clear-sessions", type="clearsessions")
                else: log.msg("CANCELLED: Clear sessions", True)
            case ".changeusername" | ".changename" | ".editusername" | ".editname":
                newusername = input("NEW USERNAME: ")
                nondefkey = input("NON-DEFAULT KEY: ")
                confirm = input("Are you sure that you want to do this? Write CONFIRM to confirm.")
                params = { "name": newusername }
                if confirm == "CONFIRM": makerequest(mode="POST", url=f"{BASEURL}user/{nondefkey if len(nondefkey) > 0 else USERKEY}/friend-code/update", type="changeusername", params=params)
                else: log.msg("CANCELLED: Friendcode update", True)
            case ".shop":
                makerequest(mode="GET", url=f"{BASEURL}shop/available", type="shopavailable")
            case ".rewardtracks" | ".rewardstracks" | ".rewardtrack" | ".rewardstracks":
                nondefkey = input("NON-DEFAULT KEY: ")
                params = { "userKey": nondefkey if len(nondefkey) > 0 else USERKEY }
                makerequest(mode="GET", url=f"{BASEURL}reward/tracks", type="rewardtracks", params=params)
            case ".rewards" | ".reward":
                nondefkey = input("NON-DEFAULT KEY: ")
                makerequest(mode="GET", url=f"{BASEURL}user/{nondefkey if len(nondefkey) > 0 else USERKEY}/rewards", type="rewards")
            case ".quests" | ".quest":
                nondefkey = input("NON-DEFAULT KEY: ")
                params = { "userKey": nondefkey if len(nondefkey) > 0 else USERKEY }
                makerequest(mode="GET", url=f"{BASEURL}quest/available", type="quests", params=params)
            case ".polls" | ".poll":
                nondefkey = input("NON-DEFAULT KEY: ")
                params = { "userKey": nondefkey if len(nondefkey) > 0 else USERKEY }
                makerequest(mode="GET", url=f"{BASEURL}poll/available", type="polls", params=params)
            case ".leaderboard" | ".lb" | ".leaderboards":
                lbmode = input("MODE: ")
                lbtime = input("TIME RANGE: ")
                lbcat = input("CATEGORY: ")
                params = { "userKey": USERKEY, "mode": lbmode, "time": lbtime, "category": lbcat }
                makerequest(mode="GET", url=f"{BASEURL}leaderboard/live", type="leaderboard", params=params)
    except KeyboardInterrupt:
        log.msg(f"CANCELLED: {command}", True)
    newcommand()
            
print("ZombsRoyale.io API Utils")
print("Run .help for a commands list")
log.msg("Validating your default userkey...", True)
if not validatekey(USERKEY):
    log.warning("YOUR CURRENT DEFAULT USERKEY IS INVALID", True)
log.msg("Done!", True)
newcommand()
