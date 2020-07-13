#python3
#学籍番号と点数群を辞書に登録
point_dict = {
    '001': (100, 88, 81),
    '002': (77, 94, 85),
    '003': (80, 52, 99),
}
#辞書の変数をfor文で繰り返し処理にかける
for student_id in point_dict:
    #keyを指定してvalueを取得
    points = point_dict[student_id]
    #教科数を取得
    subject_number = len(points)
    #タプルに入った点数群を多重代入
    japanese, english, mathmatics = points
    #合計を求める
    total = japanese + english + mathmatics

    #評価基準を変数に代入
    excellent = subject_number * 100 * 0.8
    good = subject_number * 100 * 0.65

    #条件分岐する部分を繰り返し処理の中で使う
    if total >= excellent:
        evaluation = 'Excellent!'
    elif total >= good:
        evaluation = 'Good'
    else:
        evaluation = 'Bad'
    print('学籍番号{}: 合計点は{}、評価は{}です。'.format(student_id, total, evaluation))    
