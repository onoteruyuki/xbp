import pandas as pd

# 家計簿のデータを作成します
data = {
    '日付': ['2023-10-01', '2023-10-05', '2023-10-10'],
    '品目': ['食費', '交通費', '光熱費'],
    '金額': [1000, 500, 2000]
}

# データをpandasのDataFrameに変換します
df = pd.DataFrame(data)

# Excelファイルに出力します
excel_writer = pd.ExcelWriter('家計簿.xlsx', engine='openpyxl')
df.to_excel(excel_writer, index=False, sheet_name='家計簿')
excel_writer.save
excel_writer.close('家計簿.xlsx')



