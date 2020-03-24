"""
記述ルール

・AがTrueかつBがTrueでTrueにする時
if 論理式A and 論理式B :
    Trueの時の処理

・AまたはBいずれかがTrueの時の処理
if 論理式A or 論理式B :
    Trueの時の処理


"""
score = 60
score2 = 60

if score >= 60 and score2 >= 60:
    print("全て合格！")

elif score >= 60 and score2 < 60 or score < 60 and score2 >= 60:
    print("ひとつ合格！")

else:
    print("残念！")