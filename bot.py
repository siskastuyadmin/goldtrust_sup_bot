# -*- coding: utf-8 -*-
# ------------------------------
# GoldTrust Support Bot - FINAL FIXED VERSION
# ------------------------------

import telebot
from telebot import types

TOKEN = "8499056222:AAG2p_tSmvOZIhCILvgeA_wD3khiAF6rebc"  # встав свій токен сюди
BOT_USERNAME = "GoldTrustSupport_bot"
SUPPORT_USERNAME = "@GoldTrustSupport"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

user_state = {}
user_data = {}

# ====== ТЕКСТИ ======
TEXTS = {
    "ru": {
        "welcome": "👋 <b>Добро пожаловать в GoldTrust!</b>\n\nВаш надёжный партнёр для безопасных сделок.",
        "profile": "👤 <b>Профиль</b>\n🔹 Пользователь: @{username}\n🔹 ID: <code>{user_id_str}</code>\n🔹 Язык: Русский",

        "create_ticket": "📝 <b>Создать обращение</b>\n\nВыберите тип проблемы:",
        "problem_types": ["🔸 Проблема со сделкой", "🔸 Проблема с оплатой", "🔸 Проблема с выводом", "🔸 Другое"],

        "enter_deal_code": "🔢 <b>Введите код сделки:</b>",
        "enter_agent_description": "📝 <b>Опишите ситуацию по вашей сделке/оплате:</b>",

        "enter_amount": "💰 <b>Введите сумму сделки:</b>\n\n<i>Только число</i>",
        "currency_choice": "💱 <b>Выберите валюту:</b>",

        "min_withdraw": (
            "⚠️ <b>Уважаемые пользователи!</b>\n\n"
            "В связи со сбоем сервиса автоматического вывода средств в валюте {currency}, "
            "временно введено ограничение: минимальная сумма для вывода составляет {amount} {currency}.\n\n"
            "Ваши балансы остаются в сохранности и доступны к выводу от {amount} {currency}. "
            "Чтобы вывести средства в валюте {currency}, необходимо совершить сделку(-и) на недостающую сумму, "
            "чтобы достичь минимального порога вывода.\n\n"
            "Мы уже работаем над устранением проблемы. Спасибо за понимание!"
        ),

        "agent_notification": "✅ <b>Спасибо за обращение!</b>\n\nВаша заявка будет передана агентам. Мы свяжемся с вами после проверки.",
        "support_contact": "📞 <b>Свяжитесь с агентом техподдержки:</b>\n\n👤 {support_username}\n\nОпишите ситуацию и наши специалисты помогут вам.",

        "enter_custom_problem": "📝 Пожалуйста, напишите ваше обращение (опишите проблему или предложение):",
        "verify_data": "🔍 <b>Проверьте свои данные:</b>\n\n👤 Пользователь: @{username}\n📋 Раздел: Другое\n💬 Обращение: {problem}\n\nВсё верно?",
        "data_correct": "✅ Спасибо! Ваша заявка передана агентам.",
        "data_incorrect": "📝 Хорошо, напишите обращение заново:",

        "language_changed": "🌍 <b>Язык изменён на Русский</b>",

        "back": "🔙 Назад",
        "contact_agent": "📨 Связаться с агентом"
    },

     "en": {
            "welcome": "👋 <b>Welcome to GoldTrust!</b>\n\nYour reliable partner for secure deals.",
            "profile": "👤 <b>Profile</b>\n🔹 User: @{username}\n🔹 ID: <code>{user_id_str}</code>\n🔹 Language: English",

        "create_ticket": "📝 <b>Create Ticket</b>\n\nSelect problem type:",
        "problem_types": ["🔸 Deal problem", "🔸 Payment problem", "🔸 Withdrawal problem", "🔸 Other"],

        "enter_deal_code": "🔢 <b>Enter deal code:</b>",
        "enter_agent_description": "📝 <b>Describe your situation for the deal/payment:</b>",

        "enter_amount": "💰 <b>Enter deal amount:</b>\n\n<i>Numbers only</i>",
        "currency_choice": "💱 <b>Select currency:</b>",

        "min_withdraw": (
            "⚠️ <b>Dear users!</b>\n\n"
            "Due to a failure in the automatic withdrawal service in {currency}, "
            "a temporary restriction has been introduced: the minimum withdrawal amount is {amount} {currency}.\n\n"
            "Your balances remain safe and available for withdrawal from {amount} {currency}. "
            "To withdraw funds in {currency}, please complete deal(s) for the missing amount to reach the threshold.\n\n"
            "We are working on a fix. Thank you for understanding!"
        ),

        "agent_notification": "✅ <b>Thank you!</b>\n\nYour ticket has been forwarded to our agents. We will contact you after review.",
        "support_contact": "📞 <b>Contact a support agent:</b>\n\n👤 {support_username}",

        "enter_custom_problem": "📝 Please write your request (describe the problem or suggestion):",
        "verify_data": "🔍 <b>Verify your data:</b>\n\n👤 User: @{username}\n📋 Section: Other\n💬 Request: {problem}\n\nIs everything correct?",
        "data_correct": "✅ Thank you! Your ticket has been forwarded to our agents.",
        "data_incorrect": "📝 Okay, please write your request again:","language_changed": "🌍 <b>Language changed to English</b>",

        "back": "🔙 Back",
        "contact_agent": "📨 Contact agent"
    },

    "uk": {
        "welcome": "👋 <b>Ласкаво просимо до GoldTrust!</b>\n\nВаш надійний партнер для безпечних угод.",
        "profile": "👤 <b>Профіль</b>\n🔹 Користувач: @{username}\n🔹 ID: <code>{user_id_str}</code>\n🔹 Мова: Українська",

        "create_ticket": "📝 <b>Створити звернення</b>\n\nОберіть тип проблеми:",
        "problem_types": ["🔸 Проблема з угодою", "🔸 Проблема з оплатою", "🔸 Проблема з виводом", "🔸 Інше"],

        "enter_deal_code": "🔢 <b>Введіть код угоди:</b>",
        "enter_agent_description": "📝 <b>Опишіть ситуацію щодо вашої угоди/оплати:</b>",

        "enter_amount": "💰 <b>Введіть суму угоди:</b>\n\n<i>Лише число</i>",
        "currency_choice": "💱 <b>Оберіть валюту:</b>",

        "min_withdraw": (
            "⚠️ <b>Шановні користувачі!</b>\n\n"
            "Через збій сервісу автоматичного виводу коштів у валюті {currency}, "
            "тимчасово запроваджено обмеження: мінімальна сума для виводу становить {amount} {currency}.\n\n"
            "Ваші баланси в безпеці та доступні до виводу від {amount} {currency}. "
            "Щоб вивести кошти у валюті {currency}, необхідно здійснити угоду(-и) на недостатню суму, "
            "щоб досягти порогу виводу.\n\n"
            "Ми вже працюємо над усуненням проблеми. Дякуємо за розуміння!"
        ),

        "agent_notification": "✅ <b>Дякуємо!</b>\n\nВаше звернення передано агентам. Ми зв'яжемося з вами після перевірки.",
        "support_contact": "📞 <b>Зв'яжіться з агентом техпідтримки:</b>\n\n👤 {support_username}",

        "enter_custom_problem": "📝 Будь ласка, напишіть ваше звернення (опишіть проблему або пропозицію):",
        "verify_data": "🔍 <b>Перевірте свої дані:</b>\n\n👤 Користувач: @{username}\n📋 Розділ: Інше\n💬 Звернення: {problem}\n\nВсе вірно?",
        "data_correct": "✅ Дякуємо! Ваше звернення передано агентам.",
        "data_incorrect": "📝 Гаразд, напишіть звернення заново:",

        "language_changed": "🌍 <b>Мову змінено на Українську</b>",

        "back": "🔙 Назад",
        "contact_agent": "📨 Зв'язатися з агентом"
    }
}

def get_text(user_id, key, **kwargs):
    lang = user_data.get(user_id, {}).get("language", "ru")
    text = TEXTS[lang].get(key, key)
    return text.format(**kwargs) if kwargs else text


# ====== КОМАНДЫ ======
@bot.message_handler(commands=["start"])
def cmd_start(message):
    user_id = message.from_user.id
    user_data[user_id] = {"language": "ru"}

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🆘 Создать обращение", "📄 Профиль")
    markup.add("🌐 Сменить язык")

    bot.send_message(message.chat.id, get_text(user_id, "welcome"), reply_markup=markup)


# ====== МЕНЮ ======
@bot.message_handler(func=lambda msg: msg.text == "📄 Профиль")
def menu_profile(message):
    user_id = message.from_user.id
    username = message.from_user.username or "—"
    bot.send_message(
        message.chat.id,
        get_text(user_id, "profile", username=username, user_id_str=user_id)
    )


@bot.message_handler(func=lambda msg: msg.text == "🆘 Создать обращение")
def menu_create_ticket(message):
    user_id = message.from_user.id
    user_state[user_id] = "wait_problem_type"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for problem_type in get_text(user_id, "problem_types"):
        markup.add(problem_type)
    markup.add("🔙 Назад")

    bot.send_message(message.chat.id, get_text(user_id, "create_ticket"), reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == "🌐 Сменить язык")
def menu_language(message):
    user_id = message.from_user.id

    # гарантуємо, що запис про користувача є
    if user_id not in user_data:
        user_data[user_id] = {"language": "ru"}

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🇷🇺 Русский", "🇺🇦 Українська", "🇺🇸 English")
    markup.add("🔙 Назад")

    bot.send_message(message.chat.id, "🌍 <b>Выберите язык:</b>", reply_markup=markup)
    user_state[user_id] = "wait_language"
@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_language")
def handle_language(message):
    user_id = message.from_user.id

    language_map = {
        "🇷🇺 Русский": "ru",
        "🇺🇦 Українська": "uk",
        "🇺🇸 English": "en",
        "🔙 Назад": None
    }

    choice = language_map.get(message.text)

    # якщо натиснули "Назад" або щось невідоме — просто повертаємо в головне меню
    if choice is None:
        user_state.pop(user_id, None)
        bot.send_message(message.chat.id, "↩️", reply_markup=get_main_menu(user_id))
        return

    # гарантуємо наявність профілю користувача
    if user_id not in user_data:
        user_data[user_id] = {}

    # змінюємо мову і підтверджуємо відповідним текстом
    user_data[user_id]["language"] = choice
    lang_changed = get_text(user_id, "language_changed")
    bot.send_message(message.chat.id, lang_changed, reply_markup=get_main_menu(user_id))

    # скидаємо стан
    user_state.pop(user_id, None)

# ====== ПРОБЛЕМИ ======
@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_problem_type")
def handle_problem_type(message):
    user_id = message.from_user.id
    problem_type = message.text

    types_list = get_text(user_id, "problem_types")

    if problem_type == types_list[0] or problem_type == types_list[1]:
        user_data[user_id]["problem_type"] = problem_type
        user_state[user_id] = "wait_deal_code"
        bot.send_message(message.chat.id, get_text(user_id, "enter_deal_code"))

    elif problem_type == types_list[2]:
        user_data[user_id]["problem_type"] = problem_type
        user_state[user_id] = "wait_deal_code_withdraw"
        bot.send_message(message.chat.id, get_text(user_id, "enter_deal_code"))

    elif problem_type == types_list[3]:
        user_data[user_id]["problem_type"] = problem_type
        user_state[user_id] = "wait_custom_problem"
        bot.send_message(message.chat.id, get_text(user_id, "enter_custom_problem"))


# ====== ДЛЯ СДЕЛКИ/ОПЛАТЫ ======
@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_deal_code")
def handle_deal(message):
    user_id = message.from_user.id
    user_data[user_id]["deal_code"] = message.text
    user_state[user_id] = "wait_situation"
    bot.send_message(message.chat.id, get_text(user_id, "describe_situation"))


@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_situation")
def handle_situation(message):
    user_id = message.from_user.id
    user_data[user_id]["situation"] = message.text
    user_state.pop(user_id, None)
    bot.send_message(message.chat.id, get_text(user_id, "agent_notification"), reply_markup=get_main_menu(user_id))


# ====== ПРОБЛЕМА С ВЫВОДОМ ======
@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_deal_code_withdraw")
def handle_withdraw_code(message):
    user_id = message.from_user.id
    user_state[user_id] = "wait_currency"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🇷🇺 RUB", "🇺🇦 UAH", "💵 USD", "💎 TON")
    bot.send_message(message.chat.id, get_text(user_id, "currency_choice"), reply_markup=markup)


@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_currency")
def handle_currency(message):
    user_id = message.from_user.id
    user_data[user_id]["currency"] = message.text.strip()
    user_state[user_id] = "wait_amount"
    bot.send_message(message.chat.id, get_text(user_id, "enter_amount"), reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_amount")
def handle_amount(message):
    user_id = message.from_user.id
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "❌ Введите только число!")
        return

    amount = int(message.text)
    final_amount = int(amount * 1.5)
    currency = user_data[user_id].get("currency", "RUB")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("✅ Спасибо", "💬 Связаться с агентом")

    bot.send_message(
        message.chat.id,
        get_text(user_id, "min_withdraw", amount=final_amount, currency=currency),
        reply_markup=markup
    )
    user_state[user_id] = "wait_response"


# ====== ОБРАБОТКА ОТВЕТА ======
@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_response")
def handle_response(message):
    user_id = message.from_user.id

    if message.text == "✅ Спасибо":
        bot.send_message(message.chat.id, "✅ Спасибо за обращение!", reply_markup=get_main_menu(user_id))
    elif message.text == "💬 Связаться с агентом":
        bot.send_message(
            message.chat.id,
            get_text(user_id, "support_contact", support_username=SUPPORT_USERNAME),
            reply_markup=get_main_menu(user_id),
            disable_web_page_preview=True
        )

    user_state.pop(user_id, None)


# ====== ФУНКЦИИ ======
def get_main_menu(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🆘 Создать обращение", "📄 Профиль")
    markup.add("🌐 Сменить язык")
    return markup


# ====== ЗАПУСК ======
if __name__ == "__main__":
    print("🤖 GoldTrust Support Bot - FIXED VERSION")
    print("🟢 Бот запущен...")
    bot.infinity_polling()
