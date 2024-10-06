import tkinter as tk
from tkinter import ttk
from datetime import datetime

from timezones import TIMEZONE_DICT

# 定数
BG_COLOR = "#000000"
TEXT_COLOR = "#FFFFFF"
NOTATION_12_HOUR = "12時制"
NOTATION_24_HOUR = "24時制"

# グローバル変数と初期値の設定
current_notation = NOTATION_12_HOUR
current_timezone = "Asia/Tokyo"  # 現在のタイムゾーン

# メインウィンドウの作成
root = tk.Tk()
root.title("デジタル時計")
root.config(bg=BG_COLOR)
root.resizable(width=False, height=False)

# 現在時刻を表示するラベルの作成
label_time = tk.Label(root, font=("Helvetica", 48), fg=TEXT_COLOR, bg=BG_COLOR)
label_time.pack()

# 現在の時刻表記を表示するラベル
label_ampm = tk.Label(
    root, text="AM/PM", font=("Helvetica", 18), fg=TEXT_COLOR, bg=BG_COLOR
)
label_ampm.pack(before=label_time)

# メニューバーの作成
menubar = tk.Menu(root)
root.config(menu=menubar)


# 時刻表記を変更する関数
def switch_notation():
    global current_notation
    current_notation = var_notation.get()
    update_time(False)


# メニューの作成
notation_menu = tk.Menu(menubar, tearoff=False)
var_notation = tk.StringVar(value=current_notation)
notation_menu.add_radiobutton(
    label=NOTATION_12_HOUR,
    variable=var_notation,
    value=NOTATION_12_HOUR,
    command=switch_notation,
)
notation_menu.add_radiobutton(
    label=NOTATION_24_HOUR,
    variable=var_notation,
    value=NOTATION_24_HOUR,
    command=switch_notation,
)
menubar.add_cascade(label="時刻表記", menu=notation_menu)


# タイムゾーンを変更する関数
def switch_timezone(event):
    global current_timezone
    current_timezone = event.widget.get()
    update_time(False)


# タイムゾーンを選択するコンボボックスの作成
combobox_timezone = ttk.Combobox(root, values=list(TIMEZONE_DICT.keys()))
combobox_timezone.set(current_timezone)
combobox_timezone.bind("<<ComboboxSelected>>", switch_timezone)
combobox_timezone.pack(before=label_ampm)  # 時刻表記法の前に配置


# 現在時刻を更新する関数
def update_time(recursion=True):
    now = datetime.now(tz=TIMEZONE_DICT[current_timezone])
    if current_notation == NOTATION_24_HOUR:
        hour = now.hour
        label_ampm.config(text="")
    else:
        is_am = now.hour < 12
        hour = now.hour if is_am else now.hour - 12
        if is_am:
            label_ampm.config(text="AM")
        else:
            label_ampm.config(text="PM")
    minute = now.minute
    second = now.second
    text_time = f"{hour:0>2}:{minute:0>2}:{second:0>2}"
    label_time.config(text=text_time)
    if recursion:
        root.after(1000, update_time)


# メインループの実行
update_time()
root.mainloop()
print("時計アプリを終了しました。")