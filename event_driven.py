# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

# 関数birthdayの定義
def birthday():
    messagebox.showinfo("メッセージ","今日は" + entry.get() + "です")
    entry.delete(0,tk.END)

# rootフレームの設定
root = tk.Tk()
root.title("文字列の取得・セット・クリア")
root.geometry("500x300")

# フレームの作成と設置
frame = ttk.Frame(root)
frame.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)

# 各種ウィジェットの作成
label = ttk.Label(frame, text="テキストを入力")
entry = ttk.Entry(frame)
button_execute = ttk.Button(frame, text="実行", command=birthday)

# 各種ウィジェットの設置
label.grid(column=0, row=0)
entry.grid(column=0, row=0)
button_execute.grid(column=0, row=1)

# Entryウィジェットへ文字列のセット
#entry.insert(tk.END,"1999/01/01")

root.mainloop()
