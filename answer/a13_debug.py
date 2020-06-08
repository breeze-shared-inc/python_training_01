import requests as req
import json

def check():
    r = req.get("https://script.google.com/macros/s/AKfycbx59mSU5gTZ_FExAwaZrgjEorUcuki0AqGnh_XYn5uyZi_RSYzJ/exec")
    r = json.loads(r.text)

    for one in r:
        for profile in one:
            if profile == "name":
                print("{}さんの".format(one[profile]))
            if profile == "birth":
                print("誕生日は{}。".format(one[profile]))
            if profile == "born":
                print("出身地は{}。".format(one[profile]))


check()