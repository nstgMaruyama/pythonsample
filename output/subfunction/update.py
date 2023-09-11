import output.subfunction.readCsv as readCsv
import subfunction.jsonPrint as jsonPrint
import subfunction.savePrint as savePrint


# 説明：CSVの内容を変更するプログラム
# 第一引数 カラム
# 第二引数 変更前の値
# 第三引数 変更後の値
# 
# 返り値 
def upgrade( fileName:str, column:str, value:str):
    # Csvファイルを読み込んで配列に入れる
    readCsv()
    # 配列中で値を変換する
        # 記入箇所 
    # 変換した内容をcsvファイルに書き込んで保存する
    savePrint()         
    # json形式で出力する
    jsonPrint()
    return 0









    