"""

記述ルール

・Trueになる条件が複数ある時
if 論理式1 :
    論理式1がTrueの時の処理

elif 論理式2 :
    論理式2がTrueの時の処理

else:
    Falseの時の処理

問題：以下を出力せよ
nensu に10が入力されている状態
ゴールド

nensu に5が入力されている状態
シルバー

nensu が5未満
ブロンズ

"""

nensu = 10

if nensu >= 10:
    print("ゴールド")
elif nensu >= 5:
    print("シルバー")
else:
    print("ブロンズ")

