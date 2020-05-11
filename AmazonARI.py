import csv
import os
import tkinter, tkinter.filedialog, tkinter.messagebox

#エラーメッセージ実装していないので注意！

#Tkinter設定
root = tkinter.Tk()
root.withdraw()
filetype = [("", "*.csv")]
dirpath = os.path.abspath(os.path.dirname(__file__))
filepath = tkinter.filedialog.askopenfilename(filetypes = filetype, initialdir = dirpath)

#CSV読み込み
f = open(filepath,'r', encoding="utf-8")
reader = csv.reader(f)
header = next(reader)  # ヘッダーを読み飛ばし
date = []
name = []
price = []
total_cost = []

for row in reader:
    date.append(row[0])
    name.append(row[2])
    price.append(row[4])
    total_cost.append(row[11])

csv_date = []
csv_name = []
csv_cost = []
temp_name = "AZ-"

for i in range(len(date)):
    if not total_cost[i] == "":
        csv_cost.append(total_cost[i]) #合計金額
        csv_date.append(date[i])    #日付
        csv_name.append(temp_name)
        temp_name = "AZ-"   #商品名リセット

    if not price[i] == "":  #購入商品名を取得
        if not temp_name == "AZ-":
            temp_name = temp_name + "/" + name[i]
        else:
            temp_name = temp_name + name[i]

csv_name.append(temp_name) #ループから漏れた商品名をリストに追加
csv_name.pop(0) #商品名最初は空欄なので消去
f.close
#CSV書き出しセクション
with open('output.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['日付', '合計金額', '商品名'])
    print(csv_date)
    for i in range(len(csv_date)):
        print(csv_date[i],"/内容:",csv_name[i],"/値段:",csv_cost[i],"円")
        writer.writerow([csv_date[i],csv_cost[i],csv_name[i]])