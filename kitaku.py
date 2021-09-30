import time
import datetime
import keyboard
import openpyxl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd


"""""""""""""""""""""
時間の記録
"""""""""""""""""""""    
def kiroku():
    t = time.time()
    #時間取得
    dt = datetime.datetime.now()
    y = dt.year
    m = dt.month
    d = dt.day
    H = dt.hour
    M = dt.minute
    S = dt.second
    print(str(y) + "/" + str(m) + "/" + str(d))
    print(str(H) + ":" + str(M) + ":" + str(S))
    print("")
    time.sleep(1)
        
    #時間をexcelに記録
    jikoku = openpyxl.load_workbook("date.xlsx")
    sheet = jikoku["Sheet1"]
        
    sheet["A" + str(d)] = m
    sheet["B" + str(d)] = d
    sheet["C" + str(d)] = H
    sheet["D" + str(d)] = M
    jikoku.save("date.xlsx")

    print("正常に保存できました。\n")


"""""""""""""""""""""
グラフの表示
"""""""""""""""""""""
def graph():
    month = []
    day = []
    day_str = []
    hour = []
    minu = []
    time = []
    a = 0
    #記録用エクセルの取得
    file = openpyxl.load_workbook("date.xlsx")
    sheet = file["Sheet1"]

    #記録用配列に値を入力
    for i in range(1, 32):
        try:
            month.append(int(sheet["A" + str(i)].value))
            day.append(int(sheet["B" + str(i)].value))   #int型に変換してNoneを省く
            hour.append(int(sheet["C" + str(i)].value))
            minu.append(int(sheet["D" + str(i)].value))
        
            day_str.append(str(month[a]) + "/" + str(day[a]))
            time.append(str(hour[a]) + ":" + str(minu[a])) #時間に変換するときに「：」で分と秒を区別するので、いったんstring型に変換
            a += 1
        except:
            pass

    time = pd.to_datetime(time, format = "%H:%M")            #時間に変換

    #グラフの設定
    fig = plt.figure("帰宅時間")
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(day_str, time)

    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45)   #ラベルを45°傾ける

    plt.show()      #グラフの表示
    

"""""""""""""""""""""
LINE処理
"""""""""""""""""""""