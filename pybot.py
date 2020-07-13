#python3
#常に条件を満たす
while True:
    #ユーザーからの入力を受け取る
    command = input('pybot> ')
    #[こんにちは]を含む場合
    if 'こんにちは' in command:
        print('コンニチハ')
    #[ありがとう]を含む場合
    elif 'ありがとう' in command:
        print('ドウイタシマシテ')
    #[さようなら]を含む場合
    elif 'さようなら' in command:
        print('サヨウナラ')
        #繰り返し処理を終了する
        break
    #一致しない場合
    else:
        print('ナニヲイッテルカ、ワカラナイヨ！！')
