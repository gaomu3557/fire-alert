# fire-alert
import requests
from bs4 import BeautifulSoup
import hashlib
import os

URL = "http://anzn.net/sp/?p=26100F&pt=sp"
KEYWORD = "京都市"

def get_info():
    res = requests.get(URL)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.text

def send_line(msg):
    token = os.environ["LINE_TOKEN"]
    headers = {"Authorization": f"Bearer {token}"}
    data = {"message": msg}
    requests.post("https://notify-api.line.me/api/notify", headers=headers, data=data)

def main():
    text = get_info()

    if KEYWORD not in text:
        return

    lines = text.split("\n")
    target_lines = [line.strip() for line in lines if KEYWORD in line]

    if not target_lines:
        return

    message = "\n".join(target_lines[:5])

    hash_now = hashlib.md5(message.encode()).hexdigest()

    try:
        with open("last.txt", "r") as f:
            old = f.read()
    except:
        old = ""

    if hash_now != old:
        send_line("🚒【京都市の災害情報】\n\n" + message)
        with open("last.txt", "w") as f:
            f.write(hash_now)

if __name__ == "__main__":
    main()
