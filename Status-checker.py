import subprocess
import time
import requests
import json

#You must edit this variable
url = "FFmpeg-stream-URL" #Replace
webhook_url = "Discord-Webhook" #Replace

#Send message to discord
def send_to_discord(message):
    data = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    if response.status_code != 204:
        print(f"Failed to send message to Discord. Response code: {response.status_code}")


def main():
    while True:
        try:
            #Checks stream status
            #Timeout makes a time gap to get an online status. You can increas it depending on your internet speed
            result = subprocess.run(["ffmpeg", "-i", url], capture_output=True, timeout=10)
            if result.returncode == 1:
                print("Online")
                send_to_discord("Streamer is online!")
                main()
            else:
                #If somthing went wrong!
                print("Something went wrong!!")
                send_to_discord("Something went wrong!! Help Bot ASAP")
                break
        except subprocess.TimeoutExpired:
            print("Offline")
            send_to_discord("Stream is offline!!")
            main()

        time.sleep(3)

if __name__ == "__main__":
    main()
