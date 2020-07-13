#python3
#range()関数
#0,1,2,...9,を返す
for number in range(10):
    print(number)
#1,2,...99,を返す
for number in range(1,100):
    print(number)
#indexで順番を取得
for index, color in enumerate(['red', 'blue', 'green']):
    print("No.{} is {}".format(index, color))
    
