#python3
#点数をカンマ区切りで入力
your_point = input('点数をカンマ区切りで入力して下さい: ')
#カンマ区切りで点数データをリストに格納
point_list = your_point.split(',')
total = 0

#点数の合計を求める
for point in point_list:
    total += int(point)

#評価基準となる値を求める
subject_number = len(point_list)
excellent = subject_number * 100 * 0.8
good = subject_number * 100 * 0.65
#if, elif, elseで判定
if total >= excellent:
    evaluation = 'Excellent!'
elif total >= good:
    evaluation = 'Good'
else:
    evaluation = 'Bad'

#結果を表示
print('点数の評価は{}です。'.format(evaluation))
