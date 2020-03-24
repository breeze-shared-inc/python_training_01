"""
配列もプログラミングではよく使われるよ！
配列を繰り返し処理することもよく行われます！

"""

namelist = ["田中", "鈴木", "佐藤"]

for name in namelist:
    print(name)

profile = {
    "name": "田中",
    "birth": "1999/11/11",
    "bornin": "osaka"
}


for article in profile:
    print(profile[article])