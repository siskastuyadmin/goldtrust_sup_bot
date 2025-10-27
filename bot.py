# -*- coding: utf-8 -*-
# ------------------------------
# GoldTrust Support Bot — FINAL STABLE VERSION
# ------------------------------

import telebot
from telebot import types

# === CONFIG ===
TOKEN = "8499056222:AAG2p_tSmvOZIhCILvgeA_wD3khiAF6rebc"  # встав свій токен сюди
BOT_USERNAME = "GoldTrustSupport_bot"
SUPPORT_USERNAME = "@GoldTrustSupport"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")
user_state = {}
user_data = {}

# === TEXTS ===
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
            "В связи со сбоем автоматического вывода средств в валюте {currency}, "
            "временно введено ограничение: минимальная сумма для вывода составляет {amount} {currency}.\n\n"
            "Чтобы вывести средства, необходимо совершить сделки на недостающую сумму.\n\n"
            "Спасибо за понимание!"
        ),
        "agent_notification": "✅ <b>Спасибо за обращение!</b>\n\nВаша заявка передана агентам. Мы свяжемся с вами после проверки.",
        "support_contact": "📞 <b>Свяжитесь с агентом техподдержки:</b>\n\n👤 {support_username}\n\nОпишите ситуацию — специалисты помогут вам.",
        "enter_custom_problem": "📝 Пожалуйста, опишите вашу проблему:",
        "verify_data": "🔍 <b>Проверьте свои данные:</b>\n👤 Пользователь: @{username}\n📋 Раздел: Другое\n💬 Обращение: {problem}\n\nВсё верно?",
        "data_correct": "✅ Спасибо! Ваша заявка передана агентам.",
        "data_incorrect": "📝 Хорошо, напишите обращение заново:",
        "language_changed": "🌍 <b>Язык изменён на Русский</b>",
        "back": "🔙 Назад",
        "contact_agent": "💬 Связаться с агентом"
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
            "тимчасово встановлено обмеження: мінімальна сума для виводу становить {amount} {currency}.\n\n"
            "Щоб здійснити вивід, необхідно досягти мінімального порогу угод.\n\n"
            "Дякуємо за розуміння!"
        ),
        "agent_notification": "✅ <b>Дякуємо!</b>\n\nВаше звернення передано агентам. Ми зв’яжемось із вами після перевірки.",
        "support_contact": "📞 <b>Зв’яжіться з агентом техпідтримки:</b>\n\n👤 {support_username}",
        "enter_custom_problem": "📝 Будь ласка, опишіть вашу проблему:",
        "verify_data": "🔍 <b>Перевірте ваші дані:</b>\n👤 Користувач: @{username}\n📋 Розділ: Інше\n💬 Звернення: {problem}\n\nВсе вірно?",
        "data_correct": "✅ Дякуємо! Ваше звернення передано агентам.",
        "data_incorrect": "📝 Гаразд, напишіть звернення заново:",
        "language_changed": "🌍 <b>Мову змінено на Українську</b>",
        "back": "🔙 Назад",
        "contact_agent": "💬 Зв’язатися з агентом"
    },
    "en": {
        "welcome": "👋 <b>Welcome to GoldTrust!</b>\n\nYour reliable partner for secure deals.",
        "profile": "👤 <b>Profile</b>\n🔹 User: @{username}\n🔹 ID: <code>{user_id_str}</code>\n🔹 Language: English",
        "create_ticket": "📝 <b>Create Ticket</b>\n\nSelect problem type:",
        "problem_types": ["🔸 Deal problem", "🔸 Payment problem", "🔸 Withdrawal problem", "🔸 Other"],
        "enter_deal_code": "🔢 <b>Enter deal code:</b>",
        "enter_agent_description": "📝 <b>Describe your deal/payment situation:</b>",
        "enter_amount": "💰 <b>Enter deal amount:</b>\n\n<i>Numbers only</i>",
        "currency_choice": "💱 <b>Select currency:</b>",
        "min_withdraw": (
            "⚠️ <b>Dear users!</b>\n\n"
            "Due to a failure in the automatic withdrawal service in {currency}, "
            "a temporary restriction has been introduced: minimum withdrawal amount is {amount} {currency}.\n\n"
            "Please complete deals to reach the required threshold.\n\n"
            "Thank you for understanding!"
        ),
        "agent_notification": "✅ <b>Thank you!</b>\n\nYour request has been sent to our agents. We'll contact you soon.",
        "support_contact": "📞 <b>Contact a support agent:</b>\n\n👤 {support_username}",
        "enter_custom_problem": "📝 Please describe your problem:",
        "verify_data": "🔍 <b>Verify your data:</b>\n👤 User: @{username}\n📋 Section: Other\n💬 Request: {problem}\n\nIs everything correct?",
        "data_correct": "✅ Thank you! Your ticket has been sent to our agents.",
        "data_incorrect": "📝 Okay, please write your request again:",
        "language_changed": "🌍 <b>Language changed to English</b>",
        "back": "🔙 Back",
        "contact_agent": "💬 Contact agent"
    }
}


def get_text(user_id, key, **kwargs):
    lang = user_data.get(user_id, {}).get("language", "ru")
    text = TEXTS[lang].get(key, key)
    return text.format(**kwargs) if kwargs else text


# === START ===
@bot.message_handler(commands=["start"])
def cmd_start(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {"language": "ru"}
    bot.send_message(message.chat.id, get_text(user_id, "welcome"), reply_markup=get_main_menu(user_id))


# === PROFILE ===
@bot.message_handler(func=lambda msg: msg.text == "📄 Профиль")
def menu_profile(message):
    user_id = message.from_user.id
    username = message.from_user.username or "—"
    bot.send_message(message.chat.id, get_text(user_id, "profile", username=username, user_id_str=str(user_id)))


# === CREATE TICKET ===
@bot.message_handler(func=lambda msg: msg.text == "🆘 Создать обращение")
def menu_create_ticket(message):
    user_id = message.from_user.id
    user_state[user_id] = "wait_problem_type"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for problem_type in get_text(user_id, "problem_types"):
        markup.add(problem_type)
    markup.add(get_text(user_id, "back"))
    bot.send_message(message.chat.id, get_text(user_id, "create_ticket"), reply_markup=markup)


# === BACK BUTTON ===
@bot.message_handler(func=lambda msg: msg.text in ["🔙 Назад", "🔙 Back"])
def go_back(message):
    user_id = message.from_user.id
    user_state.pop(user_id, None)
    bot.send_message(message.chat.id, get_text(user_id, "welcome"), reply_markup=get_main_menu(user_id))


# === LANGUAGE SWITCH ===
@bot.message_handler(func=lambda msg: msg.text == "🌐 Сменить язык")
def choose_lang(message):
    user_id = message.from_user.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🇷🇺 Русский", "🇺🇦 Українська", "🇬🇧 English")
    markup.add(get_text(user_id, "back"))
    user_state[user_id] = "wait_lang"
    bot.send_message(message.chat.id, "🌍 <b>Выберите язык / Choose language / Оберіть мову:</b>", reply_markup=markup)


@bot.message_handler(func=lambda msg: user_state.get(msg.from_user.id) == "wait_lang")
def set_language(message):
    user_id = message.from_user.id
    lang_map = {"🇷🇺 Русский": "ru", "🇺🇦 Українська": "uk", "🇬🇧 English": "en"}
    if message.text in lang_map:
        user_data[user_id]["language"] = lang_map[message.text]
        bot.send_message(message.chat.id, get_text(user_id, "language_changed"), reply_markup=get_main_menu(user_id))
        user_state.pop(user_id, None)
    else:
        go_back(message)


# === FUNCTIONS ===
def get_main_menu(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🆘 Создать обращение", "📄 Профиль")
    markup.add("🌐 Сменить язык")
    return markup


# === START BOT ===
if __name__ == "__main__":
    print("🤖 GoldTrust Support Bot — STABLE VERSION")
    print("🟢 Бот запущен и готов к работе...")
    bot.infinity_polling()
