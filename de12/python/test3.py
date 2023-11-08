from openpyxl import Workbook

# ワークブックを作成し、アクティブなシートを取得します
wb = Workbook()
ws = wb.active

# ヘッダーを設定します
ws.append(["日付", "品目", "金額"])
select=""

while select != "いいえ":
    data = [input("日付"), input("品目"), input("金額")]
    select=(input("書き足す場合は「はい」終了する場合は「いいえ」と記入してください"))




for row in data:
    ws.append(row)


# ファイルを保存します
wb.save("家計簿テンプレート.xlsx")