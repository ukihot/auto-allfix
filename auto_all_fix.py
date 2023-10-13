#!/usr/bin/env python3
import time
import pyautogui
import csv

JG = 40

# ファイルのパス
file_path = 'target.csv'

# テキストを格納するリスト
target = []

# CSVファイルを読み込み、オブジェクトとして格納
with open(file_path, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        target.append(row)
# Close the CSV file
csvfile.close()

# 対象事業所
previous_jgcd = JG
# 売上処理をクリック
pyautogui.moveTo(300, 300)
pyautogui.click()
# 売上伝票入力をクリック
pyautogui.moveTo(560, 190)
pyautogui.click()
# 画面待ち
time.sleep(2)

# 区分を２
pyautogui.write("2", 0.5)
pyautogui.press('enter')

for index, row in enumerate(target):
    # 必要な値を取得
    jgcd = int(row['number']) if row.get('number') else None
    zaichoku = row['code'][0] if row.get(
        'code') and len(row['code']) > 0 else None
    denpyo_code = row['code'][1:] if row.get(
        'code') and len(row['code']) > 1 else None

    if jgcd != previous_jgcd or zaichoku == "#":
        continue

    print(jgcd, zaichoku, denpyo_code)
    # 事業所コード更新
    previous_jgcd = jgcd
    # 画面待ち
    time.sleep(1)
    # 在直
    pyautogui.write(zaichoku, 0.3)
    pyautogui.press('enter')
    # 画面待ち
    time.sleep(1)
    # 伝票
    pyautogui.write(denpyo_code, 0.1)
    pyautogui.press('enter')
    # 画面待ち
    time.sleep(4)
    # 修正確定
    pyautogui.press('F9')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    print('CSV{}行目の処理完了'.format(index))
    time.sleep(5)
