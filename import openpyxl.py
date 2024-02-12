import openpyxl

#新しいワークブックを作成
workbook = openpyxl.Workbook()

#アクティブなシートを取得
sheet = workbook.active

#指定のセルに値を設定
sheet[`A1`] = `自動入力された値`

#ファイルに保存
workbook.save(`自動入力.xlsx`)