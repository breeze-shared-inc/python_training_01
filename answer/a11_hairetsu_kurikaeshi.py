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

"""

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