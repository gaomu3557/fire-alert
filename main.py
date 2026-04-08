import requests
import os

def main():
    token = os.environ["LINE_TOKEN"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "message": "🚒 テスト通知（これが来れば成功）"
    }

    r = requests.post(
        "https://notify-api.line.me/api/notify",
        headers=headers,
        data=data
    )

    print(r.status_code)
    print(r.text)

if __name__ == "__main__":
    main()
