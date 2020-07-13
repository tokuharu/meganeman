import requests

#インプレスブックスのwebページにアクセス
r = requests.get('http://book.impress.co.jp/')
#結果を表示
print(r.status_code)
