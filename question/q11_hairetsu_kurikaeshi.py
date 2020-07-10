"""
8章で行った繰り返し処理と、
10章で行った、listやdictを使って繰り返し処理を行うことができます。

ブログの記事一覧の出力は
dictなどに格納された記事情報を出力するなど、
幅広く使用されています。

逆に考えるとlistやdictで
繰り返し処理が使いこなせると、
プログラミングでできる幅が広がります！！

<問題：以下を出力せよ>
田中
鈴木
佐藤
田中
1999/11/11
osaka
初めての遠足
2020/7/10 10:00:00
2020/7/20 10:00:00
初めてのおつかい
2020/8/10 21:00:00
2020/8/20 22:00:00
楽しい楽しい学校生活
2020/9/10 16:00:00
2020/9/20 16:00:00

"""

namelist = ["田中", "鈴木", "佐藤"]

# 繰り返し処理でnamelistの情報を出力させよう！

    print(name)

profile = {
    "name": "田中",
    "birth": "1999/11/11",
    "bornin": "osaka"
}

# 繰り返し処理でprofileの情報を出力させよう！

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


        print(article[attribute])