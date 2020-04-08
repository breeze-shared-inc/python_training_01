"""
記述ルール

・AがTrueかつBがTrueでTrueにする時
if 論理式A and 論理式B :
    Trueの時の処理

・AまたはBいずれかがTrueの時の処理
if 論理式A or 論理式B :
    Trueの時の処理

問題：以下を出力させよう

sugakuが60点以上かつkokugoが60点以上
すばらしい

sugakuまたはkokugoが60点以上で
おしい

それ以外は
残念！


"""

sugaku = 67
kokugo = 68

if sugaku >= 60 or kokugo >= 60:
    print("おしい")
elif sugaku >= 60 and kokugo >= 60:
    print("すばらしい")
else:
    print("残念！")