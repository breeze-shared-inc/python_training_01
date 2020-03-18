"""

型とは
文字列や数字など、データに意味を持たせたもの

前提：
変数はメモリに保管される。
メモリを箱で表現する時、8桁の0と1しか入れられない。（←基数変換の講習でやりましたね！）
でもコンピュータが表現するデータ数は8桁（255種類）では表現仕切れない。
なので、あらゆる表現をするには箱を増やすことが必要（平仮名、カタカナ、漢字でも1000種以上）
又、自然言語の文字をメモリに格納するには2進数にしなければいけない
例
あ→000000000000000001
い→000000000000000010
う→000000000000000011


静的型付け言語：C、Java、Go、TypeScript、Kotlin、Swift
動的型付け言語：Python、PHP、Ruby、JavaScript、shellscript

静的型付けが流行る理由
1.保守しやすい（ソースコードが読みやすい）、コンピュータが解析する時に中身が特定しやすい
2.速度(初めから片付けされているので、実行と同時に型付けするより早い)

型一覧
整数型：
浮動小数点型：
文字列型： ""で囲う
真偽型： True or False で表現

リスト型：データの集合、データの追加、削除が可能
　　　　　[]と書く
タプル型：データの集合、データの追加、削除が不可能
        ()と書く
辞書型：リスト型と挙動が一緒だが、要素へのアクセスは一意の値で行う
        {}と書く

練習！：下記を出力させよう！
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'list'>
<class 'tuple'>
<class 'dict'>

"""

hensu_int = 17 #数字
hensu_float = 1.7 #小数点(浮動小数点)
hensu_str = "HelloWorld" #文字列
hensu_bool = True #真偽
hensu_list = [] #リスト
hensu_tuple = () #配列
hensu_dict = {} #辞書型

print(type(hensu_int))
print(type(hensu_float))
print(type(hensu_str))
print(type(hensu_bool))
print(type(hensu_list))
print(type(hensu_tuple))
print(type(hensu_dict))
