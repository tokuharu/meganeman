#pyhton3
#open()関数でファイルを開く
open_file = open('point.txt')
#データを読み込む
raw_data = open_file.read()
#ファイルを閉じる
open_file.close()
#行ごとのリストへ変換
point_data = raw_data.splitlines()

#空の辞書
point_dict = {}
#１行ずつ処理する
for line in point_data:
    #コロンで分割
    student_name, points_str = line.split(':')
    #辞書にデータを追加
    point_dict[student_name] = points_str

#空の辞書
score_dict = {}
#点数データを繰り返し処理
for student_name in point_dict:
    #点数リストを作成
    point_list = point_dict[student_name].split(',')
    #点数を計算
    subject_number = len(point_list)
    total = 0
    for point in point_list:
        total = total + int(point)
    average = total / subject_number
    #辞書にデータを追加
    score_dict[student_name] = (total, average, subject_number)

#空の辞書を作成
evaluation_dict = {}
#合計点データの繰り返し処理
for student_name in score_dict:
    score_data = score_dict[student_name]
    #合計点などを取り出す
    total = score_data[0]
    average = score_data[1]
    subject_number = score_data[2]

    #評価文字列を作成
    excellent = subject_number * 100 * 0.8
    good = subject_number * 100 * 0.65
    if total >= excellent:
        evaluation = 'Excellent!!'
    elif total >= good:
        evaluation = 'Good!'
    else:
        evaluation ='Bad'
    #辞書にデータを追加
    evaluation_dict[student_name] = evaluation

#ファイルを開く
file_name = 'evaluation.txt'
output_file = open(file_name, 'w')
#合計点データを繰り返し処理
for student_name in score_dict:
    #合計点を取り出す
    score_data = score_dict[student_name]
    total = score_data[0]

    #評価を取り出す
    evaluation = evaluation_dict[student_name]

    #結果を書き込む
    text = '[{}] total: {}, evaluation: {}\n'.format(student_name, total, evaluation)
    output_file.write(text)

#ファイルを閉じる
output_file.close()
print('評価結果を{}に出力しました'.format(file_name))
