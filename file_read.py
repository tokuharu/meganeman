#python3
#ファイルを開く
open_file = open('point.txt')
#データを読み込む
raw_deta = open_file.read()
#開いたらファイルを閉じる
open_file.close()
#データを表示
print(raw_deta)
