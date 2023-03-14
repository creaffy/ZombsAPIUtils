import uuid, dotenv, os, requests
from datetime import datetime

BASEURL = "https://www.zombsroyale.io/api/"
dotenv.load_dotenv(dotenv.find_dotenv())
USERKEY = os.environ.get("USERKEY")

class log:
    def msg(message:str, console:bool=False) -> None:
      if console: print(f"[LOG] -> {message}")
      with open("log.log", "a") as f:
        f.write(f"\n{datetime.now().strftime('%H:%M:%S')} [LOG] -> {message}")
    def error(message:str, console:bool=False) -> None:
      if console: print(f"[ERROR] -> {message}")
      with open("log.log", "a") as f:
        f.write(f"\n{datetime.now().strftime('%H:%M:%S')} [ERROR] -> {message}")
    def warning(message:str, console:bool=False) -> None:
      if console: print(f"[WARNING] -> {message}")
      with open("log.log", "a") as f:
        f.write(f"\n{datetime.now().strftime('%H:%M:%S')} [WARNING] -> {message}")
           
def resfile(type:str, response:str) -> str:
  filename = f"res_{type}_{uuid.uuid4()}.json"
  with open(filename, "w") as f:
    f.write(response)
    return filename

def validatekey(userkey:str) -> bool:
    res = requests.get(f"{BASEURL}user/{userkey}")
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError as error:
        log.error(error, True)
    else:
        if res.json()['status'] == "error": return False
        else: return True

def makerequest(mode:str, url:str, type:str, params:dict={}) -> None:
  match mode.upper():
    case "POST":
        try:
          res = requests.post(
            url=url,
            params=params
          )
        except requests.exceptions.HTTPError as error:
           log.error(error, True)
        else:
           resobj = res.json()
           filename = resfile(type, res.text)
           if resobj['status'] == "success": log.msg(f"POST Request succeeded. Response saved as {filename}", True)
           else: log.error(f"POST Request delivered but ZR API threw an error. Response saved as {filename}. Error message: {resobj['message']}", True)
    case "GET":
        try:
          res = requests.get(
            url=url,
            params=params
          )
        except requests.exceptions.HTTPError as error:
           log.error(error, True)
        else:
           resobj = res.json()
           filename = resfile(type, res.text)
           if resobj['status'] == "success": log.msg(f"GET Request succeeded. Response saved as {filename}", True)
           else: log.error(f"GET Request delivered but ZR API threw an error. Response saved as {filename}. Error message: {resobj['message']}", True)
