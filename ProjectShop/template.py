import sqlite3
con = sqlite3.connect("main.db")
cursor = con.cursor()
 
cursor.execute("SELECT * FROM Products WHERE Category = 'BrawlSrars' AND name = '30gems' " )
name, cost = cursor.fetchone()

template = [f'''
🎮 {name} 🎮  

💎 Описание:
Пополните свой аккаунт 30 геммами и наслаждайтесь игровым процессом! Отлично подойдёт для приобретения внутриигровых предметов, ускорения прогресса или участия в специальных акциях.

💰 Цена: {cost} рублей
''']

print(template)