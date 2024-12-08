from imp import *

class TelebotClass:
# token    
    def __init__(self, token) -> None:
        self.bot = telebot.TeleBot(token)
        self.cash_data = 0
        self.rndNumm = rnd.randint(1,12)

        self.bot.message_handler(commands=['start'])(self.lobby)
        self.bot.message_handler(commands=['admin'])(self.Admin)
        self.bot.callback_query_handler(func=lambda call: True)(self.inline_message_handler)



    def lobby(self, message):
        keyboard = types.InlineKeyboardMarkup()
        products = types.InlineKeyboardButton("Продукты🎮", callback_data="products_button")
        profile = types.InlineKeyboardButton("Профиль👤", callback_data="profile_button")
        Revocation = types.InlineKeyboardButton("Отзывы🦻", callback_data="Revocation_button") 
        shopping_cart = types.InlineKeyboardButton("Корзина🛒", callback_data="shopping_cart_button")
        support = types.InlineKeyboardButton("Поддержка⚙", callback_data="support_button")
        keyboard.add(products,profile,Revocation, shopping_cart,support)
        # print(message)

        self.bot.send_message(message.chat.id, "Вы в главном меню", reply_markup=keyboard)

    def products(self, message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        product1 = types.InlineKeyboardButton("BrawlStars", callback_data= "brawlstars_button")
        product2 = types.InlineKeyboardButton("Valorant", callback_data="Valorant_button")
        product4 = types.InlineKeyboardButton("Fortnite", callback_data="Fortnite_button")
        product3 = types.InlineKeyboardButton("Steam", callback_data="Steam_button")
        product5 = types.InlineKeyboardButton("Clash Royale", callback_data="Clash_royale_button")
        product6 = types.InlineKeyboardButton("Twitch", callback_data="Twitch_button")
        product7 = types.InlineKeyboardButton("Discord", callback_data="Discord_button")
        product8 = types.InlineKeyboardButton("Spotify", callback_data="Spotyfy_button")
        product9 = types.InlineKeyboardButton("Clash of Clans", callback_data="Clash_of_Clans_button")
        product10 = types.InlineKeyboardButton("Genshin Impact", callback_data="Genshin_Impact_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")
        keyboard.add(product1,product2,product3,product4,product5,product6,product7,product8,product9,product10)
        keyboard.add(product11)
        self.bot.send_message(message.chat.id, "Раздел с продуктами", reply_markup=keyboard)

    def profile(self, message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        # profile_button = types.InlineKeyboardButton(text="Мой профиль", callback_data="profile_info")
        balance_button = types.InlineKeyboardButton("Пополнить баланс", callback_data="top_up_balance")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")
        keyboard.add(product11, balance_button)


        
        user_balance = self.get_user_balance(message.chat.id)  # Эта функция должна вернуть реальный баланс
        user_History = self.get_user_History(message.chat.id)

        response_text = f"""
        👤 Ваш профиль:
        ID: {message.chat.id}
        💰 Баланс: {user_balance} $
        ⏳ Сделано покупок: {user_History}

        """

        self.bot.send_message(message.chat.id, response_text, reply_markup=keyboard)

    
    def get_user_balance(self):
        return 0
    
    def shopping_cart(self, message):

        keyboard = types.InlineKeyboardMarkup(row_width=2)
        back_up = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")
        delite_product= types.InlineKeyboardButton("Очистить корзину", callback_data="delite_product_button")
        checkout = types.InlineKeyboardButton("Оформить заказ", callback_data="checkout_button")

        keyboard.add(checkout,delite_product,back_up)
        shopping_cart_text = f'''
        🛒 Корзина:   
        Список всех добавленных товаров:
        заказ №1
        заказ №2
        заказ №3
        Сумма заказа: 1000 ₽
        '''

        self.bot.send_message(message.chat.id, shopping_cart_text, reply_markup=keyboard)

    def Revocation(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        add_Revocation = types.InlineKeyboardButton("Оставить отзывы", callback_data="add_Revocation_button")
        see_Revocation = types.InlineKeyboardButton("посмотреть отзывы", callback_data="see_Revocation_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")
        keyboard.add(add_Revocation,see_Revocation,product11)
        self.bot.send_message(message.chat.id, f'Ваши отзывы очень важны для нас😉', reply_markup=keyboard)

    def print_Revocation(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        back_product = types.InlineKeyboardButton("Назад", callback_data="Revocation_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")   
        next_revocation = types.InlineKeyboardButton("далее", callback_data="next_revocation_button")
        keyboard.add(next_revocation)   
        keyboard.add(back_product,product11)
        
        if self.rndNumm == 1:
                self.bot.send_message(message.chat.id, f'Всё отлично! Донат прошёл моментально, а бонусы зачислились сразу. Удобно и быстро!', reply_markup=keyboard)
        elif self.rndNumm == 2:
                self.bot.send_message(message.chat.id, f'Теперь донатить стало намного проще. Бот работает без нареканий, всё оперативно и надёжно.', reply_markup=keyboard)
        elif self.rndNumm == 3:
                self.bot.send_message(message.chat.id, f'Сервис просто топ! Закинул деньги через бота, и сразу получил всё в игре. Очень доволен!', reply_markup=keyboard)
        elif self.rndNumm == 4:
                self.bot.send_message(message.chat.id, f'Этот бот — настоящее спасение! Никаких сложных операций, пара кликов — и донат уже на аккаунте.', reply_markup=keyboard)
        elif self.rndNumm == 5:
                self.bot.send_message(message.chat.id, f'Быстрая и понятная система донатов. Поддержка всегда на связи, если что-то непонятно. Рекомендую!', reply_markup=keyboard)
        elif self.rndNumm == 6:
                self.bot.send_message(message.chat.id, f'Пользуюсь этим ботом постоянно. Всё чётко и без задержек. Донаты поступают моментально!', reply_markup=keyboard)
        elif self.rndNumm == 7:
                self.bot.send_message(message.chat.id, f'Донат прошёл за пару секунд, а награды в игре уже на месте. Очень удобно, спасибо за сервис!', reply_markup=keyboard)
        elif self.rndNumm == 8:
                self.bot.send_message(message.chat.id, f'Отличный бот для геймеров! Теперь не нужно мучиться с долгими переводами. Всё быстро и надёжно!', reply_markup=keyboard)
        elif self.rndNumm == 9:
                self.bot.send_message(message.chat.id, f'Просто лучший бот для донатов! Быстро, понятно и безопасно. Пользуюсь регулярно.', reply_markup=keyboard)
        elif self.rndNumm == 10:
                self.bot.send_message(message.chat.id, f'Донатить через этого бота — одно удовольствие. Всё прозрачно и без проблем. Деньги доходят сразу.', reply_markup=keyboard)
        elif self.rndNumm == 11:
                self.bot.send_message(message.chat.id, f'Крутой бот! Поддерживает много игр, а процесс доната занимает пару минут. Очень удобно!', reply_markup=keyboard)
        elif self.rndNumm == 12:
                self.bot.send_message(message.chat.id, f'Реально рабочий бот! Донаты поступают сразу, а бонусы ни разу не задерживались. Спасибо за отличную работу!', reply_markup=keyboard)
        else: 
            self.bot.send_message(message.chat.id, f'Извините, у нас закончились отзывы, но вы всегда можете их оставить' , reply_markup=keyboard)       
       

    

    def Brawlstars(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        gems30 = types.InlineKeyboardButton("💎30 гемов💎", callback_data="gems30_button")
        gems80 = types.InlineKeyboardButton("💎80 гемов💎", callback_data="gems80_button")
        gems170 = types.InlineKeyboardButton("💎170 гемов💎", callback_data="gems170_button")
        gems360 = types.InlineKeyboardButton("💎360 гемов💎", callback_data="gems360_button")
        gems950 = types.InlineKeyboardButton("💎950 гемов💎", callback_data="gems950_button")
        gems2000 = types.InlineKeyboardButton("💎2000 гемов💎", callback_data="gems2000_button")
        BrawlPass = types.InlineKeyboardButton("🎟Brawl Pass🎟", callback_data="BrawlPass_button")
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(gems30,gems80,gems170,gems360,gems950,gems2000,BrawlPass)
        keyboard.add(back_product)
        keyboard.add(product11)
        img = open('photo/5370741520455558161.jpg','rb')
        self.bot.send_photo(message.chat.id,img, f'Выберите услугу:', reply_markup=keyboard)
        img.close()

    def gems30(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="brawlstars_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💎30 гемов💎')
        cost = ('410')
        template = [f'''
{name} 
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def gems80(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="brawlstars_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💎80 гемов💎')
        cost = ('888')
        template = [f'''
{name}
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def gems170(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="brawlstars_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💎170 гемов💎')
        cost = ('1776')
        template = [f'''
{name}
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def gems360(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="brawlstars_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💎360 гемов💎')
        cost = ('3279')
        template = [f'''
{name} 
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def gems950(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="brawlstars_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💎950 гемов💎')
        cost = ('7514')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def gems2000(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="brawlstars_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💎2000 гемов💎')
        cost = ('15028')
        template = [f'''
{name} 
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def BrawlPass(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="brawlstars_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('🎟BrawlPass🎟')
        cost = ('1776')
        template = [f'''
 {name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)


    def Valorant(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        TurcAc = types.InlineKeyboardButton("👤Аккаунт(Турция)", callback_data="TurcAc_button")
        vp475 = types.InlineKeyboardButton("🔑475 VP", callback_data="vp475_button")
        vp1000 = types.InlineKeyboardButton("🔑1000 VP", callback_data="vp1000_button")
        vp2050 = types.InlineKeyboardButton("🔑2050 VP", callback_data="vp2050_button")
        vp3650  = types.InlineKeyboardButton("🔑3650 VP", callback_data="vp3650_button")
        vp5350 = types.InlineKeyboardButton("🔑5350 VP", callback_data="vp5350_button")
        vp11000 = types.InlineKeyboardButton("🔑11000 VP", callback_data="vp11000_button")
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(TurcAc,vp475,vp1000,vp2050,vp3650,vp5350,vp11000)
        keyboard.add(back_product)
        keyboard.add(product11)
        img = open('photo/5371084482184078186.jpg','rb')
        self.bot.send_photo(message.chat.id,img, f'Выберите услугу:', reply_markup=keyboard)
        img.close()
    def TurcAc(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Valorant_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('👤Аккаунт(Турция)')
        cost = ('29')
        template = [f'''
 {name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def vp475(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Valorant_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('🔑475 VP')
        cost = ('337')
        template = [f'''
 {name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)
    
    def vp1000(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Valorant_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('🔑1000 VP')
        cost = ('769')
        template = [f'''
 {name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def vp2050(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Valorant_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('🔑2050 VP')
        cost = ('1399')
        template = [f'''
 {name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def vp3650(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Valorant_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('🔑3650 VP')
        cost = ('1399')
        template = [f'''
 {name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def vp5350(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Valorant_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('🔑5350 VP')
        cost = ('3441')
        template = [f'''
 {name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def vp11000(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Valorant_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('🔑11000 VP')
        cost = ('6850')
        template = [f'''
 {name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    


    def Fortnite(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        Vb2800 = types.InlineKeyboardButton("💰2800 Vb", callback_data="Vb2800_button")
        Vb5000 = types.InlineKeyboardButton("💰5000 Vb", callback_data="Vb5000_button")
        Vb13500 = types.InlineKeyboardButton("💰13500 Vb", callback_data="Vb13500_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")  
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")    
        keyboard.add(Vb2800, Vb5000, Vb13500)
        keyboard.add(back_product)
        keyboard.add(product11)
        img = open('photo/5348519471335206136.jpg','rb')
        self.bot.send_photo(message.chat.id,img, f'Выберите услугу:', reply_markup=keyboard)
        img.close()
    def Vb2800(self,message):
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
            go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
            back_product = types.InlineKeyboardButton("Назад🔙", callback_data="brawlstars_button")
            product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
            keyboard.add(buy,go_shoping_cart,back_product)
            keyboard.add(product11)
            name = ('💰2800 Vb')
            cost = ('3222')
            template = [f'''
    {name}  
    💰 Цена: {cost} рублей
    '''] 
            self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def Vb5000(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="brawlstars_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💰5000 Vb')
        cost = ('5125')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def Vb13500(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="brawlstars_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💰13500 Vb')
        cost = ('11469')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def Steam(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        TurcAc = types.InlineKeyboardButton("👤Аккаунт(Турция)", callback_data="Steam_TurcAc_button")
        st5 = types.InlineKeyboardButton("💳Карта на 5 USD для турецкого региона ", callback_data="st5_button")
        st10 = types.InlineKeyboardButton("💳Карта на 10 USD для турецкого региона", callback_data="st10_button")
        st20 = types.InlineKeyboardButton("💳Карта на 20 USD для турецкого региона", callback_data="st20_button")
        st50  = types.InlineKeyboardButton("💳Карта на 50 USD для турецкого региона", callback_data="st50_button")
        st100 = types.InlineKeyboardButton("💳Карта на 100 USD для турецкого региона", callback_data="st100_button")
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(TurcAc,st5,st10,st20,st50,st100)
        keyboard.add(back_product)
        keyboard.add(product11)
        img = open('photo/5371084482184078035.jpg','rb')
        self.bot.send_photo(message.chat.id,img, f'Выберите услугу:', reply_markup=keyboard)
        img.close()

    def Steam_TurcAc(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Steam_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('👤Аккаунт(Турция)')
        cost = ('40')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def st5(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Steam_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💳Карта на 5 USD для турецкого региона')
        cost = ('563')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def st10(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Steam_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💳Карта на 10 USD для турецкого региона')
        cost = ('1113')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def st20(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Steam_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💳Карта на 20 USD для турецкого региона')
        cost = ('2226')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def st50(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Steam_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💳Карта на 50 USD для турецкого региона')
        cost = ('5562')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def st100(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Steam_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💳Карта на 100 USD для турецкого региона')
        cost = ('11097')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def Twitch(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        speed_1mnth = types.InlineKeyboardButton("⏳ Подписка на 1 месяц ", callback_data="speed_1mnth_button")
        mnth1 = types.InlineKeyboardButton("⚡ Подписка на 1 месяц", callback_data="mnth1_button")
        mnth1_2lvl = types.InlineKeyboardButton("⚡ Подписка 2 уровня на 1 месяц", callback_data="mnth1_2lvl_button")
        mnth1_3lvl = types.InlineKeyboardButton("⚡ Подписка 3 уровня на 1 месяц", callback_data="mnth1_3lvl_button")
        mnth6  = types.InlineKeyboardButton("⚡ Подписка на 6 месяцев", callback_data="mnth6_button")
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(speed_1mnth,mnth1,mnth1_2lvl,mnth1_3lvl,mnth6)
        keyboard.add(back_product)
        keyboard.add(product11)
        img = open('photo/5327765132798977611.jpg','rb')
        self.bot.send_photo(message.chat.id,img, f'Выберите услугу:', reply_markup=keyboard)
        img.close()

    def speed_1mnth(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Twitch_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⏳ Подписка на 1 месяц')
        cost = ('99')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def mnth1(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Twitch_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⚡ Подписка на 1 месяц')
        cost = ('149')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def mnth1_2lvl(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Twitch_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⚡ Подписка 2 уровня на 1 месяц')
        cost = ('292')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def mnth1_3lvl(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Twitch_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⚡ Подписка 3 уровня на 1 месяц')
        cost = ('392')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)        

    def mnth6(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Twitch_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⚡ Подписка на 6 месяцев')
        cost = ('734')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)


    def Clash_Roale(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        CRgem80 = types.InlineKeyboardButton("⚡ 80 гемов ", callback_data="CRgem80_button")
        CRgem500 = types.InlineKeyboardButton("⚡ 500 гемов", callback_data="CRgem500_button")
        CRgem2500 = types.InlineKeyboardButton("⚡ 2500 гемов", callback_data="CRgem2500_button")
        CRgem14000 = types.InlineKeyboardButton("⚡ 14000 гемов", callback_data="CRgem14000_button")
        DIAMOND_PASS = types.InlineKeyboardButton("💳DIAMOND PASS ROYALE", callback_data="DIAMOND_PASS_button")
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(CRgem80,CRgem500,CRgem2500,CRgem14000,DIAMOND_PASS)
        keyboard.add(back_product)
        keyboard.add(product11)
        img = open('photo/5371084482184078094.jpg','rb')
        self.bot.send_photo(message.chat.id,img, f'Выберите услугу:', reply_markup=keyboard)
        img.close()

    def CRgem80(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Clash_royale_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⚡ 80 гемов')
        cost = ('196')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def CRgem500(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Clash_royale_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⚡ 500 гемов')
        cost = ('980')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def CRgem2500(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Clash_royale_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⚡2500 гемов')
        cost = ('2875')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def CRgem14000(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Clash_royale_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⚡14000 гемов')
        cost = ('15028')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)        

    def DIAMOND_PASS(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Clash_royale_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💳DIAMOND PASS ROYALE')
        cost = ('2039')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def Discord(self,message):
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            Nitro1 = types.InlineKeyboardButton("💳Discord Nitro на 1 месяц со входом в аккаунт", callback_data="Nitro1_button")
            Nitro12 = types.InlineKeyboardButton("💳Discord Nitro на 12 месяцев со входом в аккаунт", callback_data="Nitro12_button")
            Basic1 = types.InlineKeyboardButton("💳Discord Basic на 1 месяц со входом в аккаунт", callback_data="Basic1_button")
            Basic12  = types.InlineKeyboardButton("💳Discord Basic на 12 месяц со входом в аккаунт", callback_data="Basic12_button")
            back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
            product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
            keyboard.add(Nitro1,Nitro12,Basic1,Basic12)
            keyboard.add(back_product)
            keyboard.add(product11)
            img = open('photo/5368489720641875298.jpg','rb')
            self.bot.send_photo(message.chat.id,img, f'Выберите услугу:', reply_markup=keyboard)
            img.close()

    def Nitro1(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Discord_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💳Discord Nitro на 1 месяц со входом в аккаунт')
        cost = ('516')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def Nitro12(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Discord_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💳Discord Nitro на 12 месяц со входом в аккаунт')
        cost = ('4030')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def Basic1(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Discord_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💳Discord Basic на 1 месяц со входом в аккаунт')
        cost = ('267')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def Basic12(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Discord_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💳Discord Basic на 12 месяц со входом в аккаунт')
        cost = ('1539')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)


    def Genshin(self,message):
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            crista60 = types.InlineKeyboardButton("🌟60 + 60 Кристаллов Сотворения (пополнение по UID)", callback_data="crista60_button")
            crista300 = types.InlineKeyboardButton("🌟300 + 300 Кристаллов Сотворения (пополнение по UID)", callback_data="crista300_button")
            crista980 = types.InlineKeyboardButton("🌟980 + 980 Кристаллов Сотворения (пополнение по UID)", callback_data="crista980_button")
            crista1980  = types.InlineKeyboardButton("🌟1980 + 1980 Кристаллов Сотворения (пополнение по UID)", callback_data="crista1980_button")
            crista3280  = types.InlineKeyboardButton("🌟3280 + 3280 Кристаллов Сотворения (пополнение по UID)", callback_data="crista3280_button")
            crista6480  = types.InlineKeyboardButton("🌟6480 + 6480 Кристаллов Сотворения (пополнение по UID)", callback_data="crista6480_button")
            Moon  = types.InlineKeyboardButton("🌙Благословение Полой Луны (пополнение по UID)", callback_data="Moon_button")
            back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
            product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
            keyboard.add(crista60,crista300,crista980,crista1980,crista3280,crista6480,Moon)
            keyboard.add(back_product)
            keyboard.add(product11)
            img = open('photo/5370741520455558179.jpg','rb')
            self.bot.send_photo(message.chat.id,img, f'Выберите услугу:', reply_markup=keyboard)
            img.close()

    def crista60(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Genshin_Impact_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('🌟60 + 60 Кристаллов Сотворения (пополнение по UID)')
        cost = ('115')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def crista60(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Genshin_Impact_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('🌟300 + 300 Кристаллов Сотворения (пополнение по UID)')
        cost = ('586')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def crista980(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Genshin_Impact_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('🌟980 + 980 Кристаллов Сотворения (пополнение по UID)')
        cost = ('1736')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def crista1980(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Genshin_Impact_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('🌟1980 + 1980 Кристаллов Сотворения (пополнение по UID)')
        cost = ('3764')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def crista3280(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Genshin_Impact_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('🌟3280 + 3280 Кристаллов Сотворения (пополнение по UID)')
        cost = ('5789')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def crista6480(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Genshin_Impact_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('🌟6480 + 6480 Кристаллов Сотворения (пополнение по UID)')
        cost = ('11581')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def Moon(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Genshin_Impact_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('🌙Благословение Полой Луны (пополнение по UID)')
        cost = ('586')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def Clash_of_Clans(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        CCgem80 = types.InlineKeyboardButton("⚡80 гемов ", callback_data="CCgem80_button")
        CCgem500 = types.InlineKeyboardButton("⚡500 гемов", callback_data="CCgem500_button")
        CCgem1200 = types.InlineKeyboardButton("⚡1200 гемов", callback_data="CCgem1200_button")
        CCgem2500 = types.InlineKeyboardButton("⚡ 2500 гемов", callback_data="CCgem2500_button")
        CCgem6500 = types.InlineKeyboardButton("⚡ 2500 гемов", callback_data="CCgem6500_button")
        CCgem14000   = types.InlineKeyboardButton("⚡ 14000 гемов", callback_data="CCgem14000_button")
        Golden_PASS    = types.InlineKeyboardButton("💳GOLDENPASS", callback_data="Golden_PASS_button")
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(CCgem80,CCgem500,CCgem1200,CCgem2500,CCgem6500,CCgem14000,Golden_PASS)
        keyboard.add(back_product)
        keyboard.add(product11)
        img = open('photo/5371084482184078402.jpg','rb')
        self.bot.send_photo(message.chat.id,img, f'Выберите услугу:', reply_markup=keyboard)
        img.close()

    def CCgem80(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Clash_of_Clans_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⚡80 гемов')
        cost = ('195')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def CCgem500(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Clash_of_Clans_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⚡500 гемов')
        cost = ('979')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def CCgem1200(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Clash_of_Clans_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⚡1200 гемов')
        cost = ('1959')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def CCgem2500(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Clash_of_Clans_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⚡2500 гемов')
        cost = ('3919')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def CCgem6500(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Clash_of_Clans_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⚡6500 гемов')
        cost = ('7513')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def CCgem14000(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Clash_of_Clans_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⚡14000 гемов')
        cost = ('14373')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)


    def Golden_PASS(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Clash_of_Clans_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('💳GOLDENPASS')
        cost = ('1188')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)


    def Spotyfy(self,message):
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            BrAcc = types.InlineKeyboardButton("👤Аккаунт Spotify(Бразилия)", callback_data="BrAcc_button")
            Individual_1 = types.InlineKeyboardButton("⭐Spotify Individual 1 месяц", callback_data="Individual_1_button")
            Individual_3 = types.InlineKeyboardButton("⭐Spotify Individual 3 месяц", callback_data="Individual_3_button")
            Individual_6  = types.InlineKeyboardButton("⭐Spotify Individual 6 месяц", callback_data="Individual_6_button")
            Individual_12  = types.InlineKeyboardButton("⭐Spotify Individual 12 месяц", callback_data="Individual_12_button")
            back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
            product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
            keyboard.add(BrAcc,Individual_1,Individual_3,Individual_6,Individual_12)
            keyboard.add(back_product)
            keyboard.add(product11)
            img = open('photo/5371084482184078322.jpg','rb')
            self.bot.send_photo(message.chat.id,img, f'Выберите услугу:', reply_markup=keyboard)
            img.close()

    def BrAcc(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Spotyfy_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('👤Аккаунт Spotify(Бразилия)')
        cost = ('49')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def Individual_1(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Spotyfy_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⭐Spotify Individual 1 месяц')
        cost = ('762')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def Individual_3(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Spotyfy_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⭐Spotify Individual 3 месяц')
        cost = ('1769')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def Individual_6(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Spotyfy_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⭐Spotify Individual 6 месяц')
        cost = ('3462')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)

    def Individual_12(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buy = types.InlineKeyboardButton("Купить🛍", callback_data="buy_button")
        go_shoping_cart = types.InlineKeyboardButton("Добавить в корзину🛒", callback_data="go_shoping_cart_button")      
        back_product = types.InlineKeyboardButton("Назад🔙", callback_data="Spotyfy_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")      
        keyboard.add(buy,go_shoping_cart,back_product)
        keyboard.add(product11)
        name = ('⭐Spotify Individual 12 месяц')
        cost = ('6206')
        template = [f'''
{name}  
💰 Цена: {cost} рублей
'''] 
        self.bot.send_message(message.chat.id,template, reply_markup=keyboard)


    def get_user_History(self,message):
        return 0
    
    def support(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")
        keyboard.add(product11)
        self.bot.send_message(message.chat.id, f'Вы всегда можете связаться с нашей тех.поддержкой @AssMaser', reply_markup=keyboard)



    def delete_msg(self, message):
        self.bot.delete_message(message.chat.id, message.message_id)


    def inline_message_handler(self, call):
        data = call.data
        match data:
            case "products_button":
                self.delete_msg(call.message)
                self.products(call.message)
            case "profile_button":
                self.delete_msg(call.message)
                self.profile(call.message)
            case "topup_button":
                self.delete_msg(call.message)
                self.delete_msg(call.message)
            case "nazad_button":
                self.delete_msg(call.message)
                self.lobby(call.message)
            case "money_button":
                self.delete_msg(call.message)
                self.money_game(call.message)
            case "shopping_cart_button":
                self.delete_msg(call.message)
                self.shopping_cart(call.message)
            case 'support_button':
                self.delete_msg(call.message)
                self.support(call.message)
            case 'brawlstars_button':
                self.delete_msg(call.message)
                self.Brawlstars(call.message)
            case "gems30_button":
                self.delete_msg(call.message)
                self.gems30(call.message)
            case "gems80_button":
                self.delete_msg(call.message)
                self.gems80(call.message)
            case "gems170_button":
                self.delete_msg(call.message)
                self.gems170(call.message)
            case "gems360_button":
                self.delete_msg(call.message)
                self.gems360(call.message)
            case "gems950_button":
                self.delete_msg(call.message)
                self.gems950(call.message)
            case "gems2000_button":
                self.delete_msg(call.message)
                self.gems2000(call.message)
            case "BrawlPass_button":
                self.delete_msg(call.message)
                self.BrawlPass(call.message)
            case 'Valorant_button':
                self.delete_msg(call.message)
                self.Valorant(call.message)
            case 'TurcAc_button':
                self.delete_msg(call.message)
                self.TurcAc(call.message)
            case 'vp475_button':
                self.delete_msg(call.message)
                self.vp475(call.message)
            case 'vp1000_button':
                self.delete_msg(call.message)
                self.vp1000(call.message)
            case 'vp2050_button':
                self.delete_msg(call.message)
                self.vp2050(call.message)
            case 'vp3650_button':
                self.delete_msg(call.message)
                self.vp3650(call.message)
            case 'vp5350_button':
                self.delete_msg(call.message)
                self.vp5350(call.message)
            case 'vp11000_button':
                self.delete_msg(call.message)
                self.vp11000(call.message) 
            case 'Fortnite_button':
                self.delete_msg(call.message)
                self.Fortnite(call.message)
            case 'Vb2800_button':
                self.delete_msg(call.message)
                self.Vb2800(call.message) 
            case 'Vb5000_button':
                self.delete_msg(call.message)
                self.Vb5000(call.message) 
            case 'Vb13500_button':
                self.delete_msg(call.message)
                self.Vb13500(call.message) 
            case 'Steam_button':
                self.delete_msg(call.message)
                self.Steam(call.message)
            case 'st5_button':
                self.delete_msg(call.message)
                self.st5(call.message)
            case 'st20_button':
                self.delete_msg(call.message)
                self.st20(call.message)
            case 'st10_button':
                self.delete_msg(call.message)
                self.st10(call.message)
            case 'st50_button':
                self.delete_msg(call.message)
                self.st50(call.message)
            case 'st100_button':
                self.delete_msg(call.message)
                self.st100(call.message)
            case 'Steam_TurcAc_button':
                self.delete_msg(call.message)
                self.Steam_TurcAc(call.message)    
            case 'Clash_royale_button': 
                self.delete_msg(call.message)
                self.Clash_Roale(call.message)
            case 'CRgem80_button': 
                self.delete_msg(call.message)
                self.CRgem80(call.message)
            case 'CRgem500_button': 
                self.delete_msg(call.message)
                self.CRgem500(call.message)
            case 'CRgem2500_button': 
                self.delete_msg(call.message)
                self.CRgem2500(call.message)
            case 'CRgem14000_button': 
                self.delete_msg(call.message)
                self.CRgem14000(call.message)
            case 'DIAMOND_PASS_button': 
                self.delete_msg(call.message)
                self.DIAMOND_PASS(call.message)
            case 'Twitch_button':
                self.delete_msg(call.message)
                self.Twitch(call.message)
            case 'speed_1mnth_button':
                self.delete_msg(call.message)
                self.speed_1mnth(call.message)
            case 'mnth1_button':
                self.delete_msg(call.message)
                self.mnth1(call.message)
            case 'mnth1_2lvl_button':
                self.delete_msg(call.message)
                self.mnth1_2lvl(call.message)
            case 'mnth1_3lvl_button':
                self.delete_msg(call.message)
                self.mnth1_3lvl(call.message)
            case 'mnth6_button':
                self.delete_msg(call.message)
                self.mnth6(call.message)
            case 'Discord_button':
                self.delete_msg(call.message)
                self.Discord(call.message)
            case 'Nitro1_button':
                self.delete_msg(call.message)
                self.Nitro1(call.message)
            case 'Nitro12_button':
                self.delete_msg(call.message)
                self.Nitro12(call.message)
            case 'Basic1_button':
                self.delete_msg(call.message)
                self.Basic1(call.message)
            case 'Basic12_button':
                self.delete_msg(call.message)
                self.Basic12(call.message)
            case 'Spotyfy_button':
                self.delete_msg(call.message)
                self.Spotyfy(call.message)
            case 'BrAcc_button':
                self.delete_msg(call.message)
                self.BrAcc(call.message)
            case 'Individual_1_button':
                self.delete_msg(call.message)
                self.Individual_1(call.message)
            case 'Individual_3_button':
                self.delete_msg(call.message)
                self.Individual_3(call.message)
            case 'Individual_6_button':
                self.delete_msg(call.message)
                self.Individual_6(call.message)
            case 'Individual_12_button':
                self.delete_msg(call.message)
                self.Individual_12(call.message)                                                                             
            case 'Genshin_Impact_button':
                self.delete_msg(call.message)
                self.Genshin(call.message)
            case 'crista60_button':
                self.delete_msg(call.message)
                self.crista60(call.message)
            case 'crista300_button':
                self.delete_msg(call.message)
                self.crista300(call.message) 
            case 'crista980_button':
                self.delete_msg(call.message)
                self.crista980(call.message)
            case 'crista1980_button':
                self.delete_msg(call.message)
                self.crista1980(call.message)
            case 'crista3280_button':
                self.delete_msg(call.message)
                self.crista3280(call.message)
            case 'crista6480_button':
                self.delete_msg(call.message)
                self.crista6480(call.message)
            case 'Moon_button':
                self.delete_msg(call.message)
                self.Moon(call.message)                                                                                   
            case 'Clash_of_Clans_button':
                self.delete_msg(call.message)
                self.Clash_of_Clans(call.message)
            case 'CCgem80_button':
                self.delete_msg(call.message)
                self.CCgem80(call.message)
            case 'CCgem500_button':
                self.delete_msg(call.message)
                self.CCgem500(call.message)
            case 'CCgem1200_button':
                self.delete_msg(call.message)
                self.CCgem1200(call.message)
            case 'CCgem2500_button':
                self.delete_msg(call.message)
                self.CCgem2500(call.message)
            case 'CCgem6500_button':
                self.delete_msg(call.message)
                self.CCgem6500(call.message)
            case 'CCgem14000_button':
                self.delete_msg(call.message)
                self.CCgem14000(call.message)
            case 'Golden_PASS_button':
                self.delete_msg(call.message)
                self.Golden_PASS(call.message)
            case 'back_button':
                self.delete_msg(call.message)
                self.products(call.message)
            case 'Revocation_button':
                self.delete_msg(call.message)
                self.Revocation(call.message)
            case "table_button":
                self.delete_msg(call.message)
                self.create_table(call.message)
            case "user_table_button":
                self.delete_msg(call.message)
                self.user_table_panel(call.message)
            case "delite_user_table_button":
                self.delete_msg(call.message)
                self.delite_user_table(call.message)
            case "admin_button":
                self.delete_msg(call.message)
                self.Admin(call.message)
            case "Update_user_table_button":
                self.delete_msg(call.message)
                self.Update_user_table(call.message)
            case "product_table_button":
                self.delete_msg(call.message)
                self.product_table_panel(call.message)
            case "Update_product_table_button":
                self.delete_msg(call.message)
                self.Update_product_table(call.message)
            case "delite_product_table_button":
                self.delete_msg(call.message)
                self.delite_Product_table(call.message)
            case "see_Revocation_button":
                self.delete_msg(call.message)
                self.print_Revocation(call.message)
            case "next_revocation_button":
                self.delete_msg(call.message)
                self.rndNumm += 1  
                self.print_Revocation(call.message)             
                




    def create_table(self, message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        admin_back_up = types.InlineKeyboardButton("В главное меню", callback_data="admin_button")
        Products_table = types.InlineKeyboardButton("Product table🗃", callback_data="product_table_button")
        User_table = types.InlineKeyboardButton("User table🗃", callback_data="user_table_button")
        keyboard.add(Products_table,User_table,admin_back_up)
        self.bot.send_message(message.chat.id, f'Добро пожаловать', reply_markup=keyboard)

        con = sqlite3.connect("main.db")
        cursor = con.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS Products
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                Category TEXT,
                name TEXT,
                cost INTEGER,
                nalichie INTEGER)
            """) 
        
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS user
            (id INTEGER PRIMARY KEY AUTOINCREMENT,  
            name TEXT,
            Chat_id INTEGER)
        """)
   
    def user_table_panel(self, message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        admin_back_up = types.InlineKeyboardButton("В главное меню", callback_data="admin_button")
        delite_User_table = types.InlineKeyboardButton("delite", callback_data="delite_user_table_button")
        Update_User_table = types.InlineKeyboardButton("Update", callback_data="Update_user_table_button")
        keyboard.add(delite_User_table,Update_User_table,admin_back_up)
        self.bot.send_message(message.chat.id, f'Добро пожаловать', reply_markup=keyboard) 




    def delite_user_table(self,message):
        con = sqlite3.connect("main.db") 
        cursor = con.cursor()
        cursor.execute(f"""DROP TABLE user""")
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        admin_back_up = types.InlineKeyboardButton("В главное меню", callback_data="admin_button")
        keyboard.add(admin_back_up)
        self.bot.send_message(message.chat.id, f'таблица user удалена', reply_markup=keyboard) 
        
    def Update_user_table(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        admin_back_up = types.InlineKeyboardButton("В главное меню", callback_data="admin_button")
        keyboard.add(admin_back_up)      
        self.bot.send_message(message.chat.id, f'таблица Products удалена', reply_markup=keyboard) 

        con = sqlite3.connect("main.db")
        cursor = con.cursor()
        params = [
            ("srydgthufh", 2335434),
            ("sryufhssd", 135434),
            ("sryufh", 12335434),
            ("sryasdfufh", 12434),
            ("sryugjsfh", 123334),
            ("sryuudgfh", 1235434),
            ("sryuffsgcmghndfgjkndh", 123354)
        ]

        for i in params:
            cursor.execute(f"INSERT INTO user (name, id) VALUES (?, ?)", i)
        con.commit()        


    # def get_user_data(self,message):
    #     self.insert_data(self.table_name,message.from_user.first_name,message.chat.id)

    def product_table(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        admin_back_up = types.InlineKeyboardButton("В главное меню", callback_data="admin_button")
        delit_table = types.InlineKeyboardButton("delite", callback_data="delite_product_table_button")
        Update_table = types.InlineKeyboardButton("Update", callback_data="Update_product_table_button")
        keyboard.add(delit_table,Update_table,admin_back_up)
        self.bot.send_message(message.chat.id, f'Добро пожаловать', reply_markup=keyboard) 
        
    def product_table_panel(self, message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        admin_back_up = types.InlineKeyboardButton("В главное меню", callback_data="admin_button")
        delite_table = types.InlineKeyboardButton("delite", callback_data="delite_product_table_button")
        Update_table = types.InlineKeyboardButton("Update", callback_data="Update_product_table_button")
        keyboard.add(delite_table,Update_table,admin_back_up)
        self.bot.send_message(message.chat.id, f'Добро пожаловать', reply_markup=keyboard) 

    def delite_Product_table(self,message):
        con = sqlite3.connect("main.db")
        cursor = con.cursor()
        cursor.execute(f"""DROP TABLE Products""")
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        admin_back_up = types.InlineKeyboardButton("В главное меню", callback_data="admin_button")
        keyboard.add(admin_back_up)
        self.bot.send_message(message.chat.id, f'таблица Products удалена', reply_markup=keyboard) 
        
    def Update_product_table(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        admin_back_up = types.InlineKeyboardButton("В главное меню", callback_data="admin_button")
        keyboard.add(admin_back_up)      
        self.bot.send_message(message.chat.id, f'таблица Products обновлена', reply_markup=keyboard) 
                                                    
        con = sqlite3.connect("main.db")
        cursor = con.cursor()
        params = [
            ("BrawlSrars","gems", 999, 1 ),
            # ("BrawlSrars","gems", 999, 1 )
            # ("sryufhssd", 135434),
            # ("sryufh", 12335434),
            # ("sryasdfufh", 12434),
            # ("sryugjsfh", 123334),
            # ("sryuudgfh", 1235434),
            # ("sryuffsgcmghndfgjkndh", 123354)
        ]

        for i in params:
            cursor.execute(f"INSERT INTO Products (Category, name, cost, nalichie) VALUES (?,?,?,?)", i)
        con.commit()  



            
    def Admin(self,message):
        user = message.from_user.username
        if user == "AssMaser":
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            back_up = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")
            delite_product= types.InlineKeyboardButton("Очистить корзину", callback_data="delite_product_button")
            table = types.InlineKeyboardButton("table🗃", callback_data="table_button")
            keyboard.add(table,delite_product,back_up)
            self.bot.send_message(message.chat.id, f'Добро пожаловать', reply_markup=keyboard)
        else:
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            back_up = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")
            keyboard.add(back_up)
            self.bot.send_message(message.chat.id, f'У вас нет прав администратора :(', reply_markup=keyboard)
            
               
            
        



    def run(self):
        self.bot.infinity_polling()