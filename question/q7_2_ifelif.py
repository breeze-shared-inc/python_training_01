"""

記述ルール

・Trueになる条件が複数ある時
if 論理式1 :
    論理式1がTrueの時の処理

elif 論理式2 :
    論理式2がTrueの時の処理

else:
    Falseの時の処理

"""
# 年数が10年以上でゴールド、
# 年数５年以上でシルバー、
# それ以外はブロンズ

nennsu = 100
if nennsu >= 10:
    print("ゴールド")
elif nennsu >= 5:
    print("シルバー")
else:
    print("ブロンズ")