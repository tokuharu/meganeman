#python3
import random

#1つを選択
def choice_command(command):
    data = command.split()
    #リストの1番目以降を渡す
    choiced = random.choice(data[1:])
    response = '「{}」ガ選バレマシタ'.format(choiced)
    return response

#数値をランダムに返す
def dice_command():
    num = random.randrange(1, 7)
    response = '「{}」ガ出マシタ'.format(num)
    return response
