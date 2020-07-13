#python3
#ライブラリをインポート
import wikipedia

def wikipedia_command(command):
    #キーワードを抜き出す
    cmd, keyword = command.split(maxsplit=1)
    #言語を指定
    wikipedia.set_lang('ja')
    try:
        #ページを取得
        page = wikipedia.page(keyword)
        title = page.title
        summary = page.summary
        #対応を生成
        response = 'タイトル: {}\n{}'.format(title, summary)
    #ページが見つからない場合
    except wikipedia.exceptions.PageError:
        response = '「{}」ノ意味ガ見ツカリマセンデシタ...'.format(keyword)
    return response
