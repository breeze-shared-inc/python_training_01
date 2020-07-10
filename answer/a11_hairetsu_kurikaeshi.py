namelist = ["田中", "鈴木", "佐藤"]

# 繰り返し処理でnamelistの情報を出力させよう！
for name in namelist:
    print(name)

profile = {
    "name": "田中",
    "birth": "1999/11/11",
    "bornin": "osaka"
}

# 繰り返し処理でprofileの情報を出力させよう！
for article in profile:
    print(profile[article])


article_list = [
    {
        "title":"初めての遠足",
        "createdAt":"2020/7/10 10:00:00",
        "updatedAt":"2020/7/20 10:00:00",
    },
    {
        "title":"初めてのおつかい",
        "createdAt":"2020/8/10 21:00:00",
        "updatedAt":"2020/8/20 22:00:00",
    },
    {
        "title":"楽しい楽しい学校生活",
        "createdAt":"2020/9/10 16:00:00",
        "updatedAt":"2020/9/20 16:00:00",
    },
]

# 繰り返し処理で全ての情報のtitle、createdAt、updatedAtを出力させよう！
for article in article_list:
    for attribute in article:
        print(article[attribute])