#python3
eto_list = ['子', '丑', '寅',]
#リストに値を追加するメゾット
eto_list.append('卯')
#リストから値を削除するメゾット
eto_list.remove('丑')
#['子', '寅', '卯']が表示される
print(eto_list)
eto_str = '子丑寅卯辰巳午未申酉戌亥'
#指定した文字列の場所(4)を返す
index = eto_str.find('辰')
#指定した文字列(子)を(猫)に変換した文字列を返す
replaced = eto_str.replace('子', '猫')
print(eto_str)
