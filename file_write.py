#python3
#書き込みモードで開く
write_file = open('output.txt', 'w')
#データを書き込む
write_file.write('Hello,Wrold!\n')
write_file.write('Hello,python!\n')
#ファイルを閉じる
write_file.close()
