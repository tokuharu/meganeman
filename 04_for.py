#python3
#リストを作成
point_list = [75, 80, 91]
#合計点数を計算するために0を代入して初期化
total = 0
for point in point_list:
    #点数を足していく
    total = total + point
#リストの長さを取得
number_of_subjects = len(point_list)
#合計点を全体の個数で割って平均点を出す
average = total / number_of_subjects
#結果を表示
print('合計点は{}、平均点は{}です。'.format(total, average))
