import os
import json
import random
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, CallbackContext,
                          MessageHandler, Filters, ConversationHandler)
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("tokal number")
ADMIN_ID = int(os.getenv("@QuizSutraBot", "0"))

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# States for conversation
QUIZ, ASK_DOUBT = range(2)

# Load quiz data (daily.json as an example)
def load_quiz_data(subject="daily"):
    try:
        with open(f"quiz_data/{subject}.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Store user scores
user_scores = {}

# Start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "\U0001F44B Welcome to the Daily Quiz & Current Affairs Bot!\n\n"
        "Use /quiz to start today\'s quiz.\n"
        "Use /quiz_subject <subject> to start a subject-wise quiz.\n"
        "Use /currentaffairs to get today\'s news.\n"
        "Use /help to see all commands."
    )

# Help command
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        "/quiz - Daily quiz\n"
        "/quiz_subject <subject> - Subject-wise quiz (e.g. polity, history)\n"
        "/currentaffairs - Get today's current affairs\n"
        "/ca_pdf - Download today's CA PDF\n"
        "/score - View your quiz score\n"
        "/ask - Ask a doubt (admin will respond)\n"
        "/notes <subject> - Get study notes\n"
        "/jobs - Latest job alerts"
    )

# Quiz function (daily)
def quiz(update: Update, context: CallbackContext):
    return start_quiz(update, context, "daily")

# Subject-wise quiz function
def quiz_subject(update: Update, context: CallbackContext):
    args = context.args
    if not args:
        update.message.reply_text("Please specify a subject. Example: /quiz_subject polity")
        return ConversationHandler.END
    subject = args[0].lower()
    return start_quiz(update, context, subject)

def start_quiz(update: Update, context: CallbackContext, subject: str):
    user_id = update.message.from_user.id
    questions = load_quiz_data(subject)
    if not questions:
        update.message.reply_text(f"❌ No quiz found for subject: {subject}")
        return ConversationHandler.END
    context.user_data['score'] = 0
    context.user_data['questions'] = questions
    random.shuffle(context.user_data['questions'])
    context.user_data['index'] = 0
    return ask_question(update, context)

def ask_question(update: Update, context: CallbackContext):
    idx = context.user_data['index']
    questions = context.user_data['questions']

    if idx >= len(questions):
        score = context.user_data['score']
        update.message.reply_text(f"\n\U0001F389 Quiz finished! Your score: {score}/{len(questions)}")
        return ConversationHandler.END

    q = questions[idx]
    reply_markup = ReplyKeyboardMarkup([[q['options'][0], q['options'][1]], [q['options'][2], q['options'][3]]], one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(f"Q{idx+1}: {q['question']}", reply_markup=reply_markup)
    return QUIZ

def answer(update: Update, context: CallbackContext):
    user_ans = update.message.text.strip()
    idx = context.user_data['index']
    questions = context.user_data['questions']
    correct = questions[idx]['answer']

    if user_ans.lower() == correct.lower():
        context.user_data['score'] += 1
        update.message.reply_text("✅ Correct!")
    else:
        update.message.reply_text(f"❌ Incorrect! Correct answer: {correct}")

    context.user_data['index'] += 1
    return ask_question(update, context)

# Current Affairs command
def current_affairs(update: Update, context: CallbackContext):
    update.message.reply_text(
        "📰 Today's Current Affairs:\n"
        "1. PM launches new health scheme.\n"
        "2. RBI keeps repo rate unchanged.\n"
        "3. ISRO plans new moon mission."
    )

# CA PDF
def ca_pdf(update: Update, context: CallbackContext):
    try:
        with open("pdfs/current_affairs_today.pdf", "rb") as file:
            update.message.reply_document(file, filename="Current_Affairs_Today.pdf")
    except FileNotFoundError:
        update.message.reply_text("No PDF found for today.")

# Score command
def score(update: Update, context: CallbackContext):
    score = context.user_data.get('score', 0)
    update.message.reply_text(f"\U0001F4CA Your current quiz score: {score}")

# Ask doubt
def ask(update: Update, context: CallbackContext):
    update.message.reply_text("Please type your doubt:")
    return ASK_DOUBT

def receive_doubt(update: Update, context: CallbackContext):
    msg = update.message.text
    user = update.message.from_user
    context.bot.send_message(chat_id=ADMIN_ID, text=f"Doubt from @{user.username or user.id}:\n{msg}")
    update.message.reply_text("✅ Your doubt has been sent to the admin. Wait for reply.")
    return ConversationHandler.END

# Fallback/cancel
def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("Operation cancelled.")
    return ConversationHandler.END

# Main function to run bot
def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    quiz_conv = ConversationHandler(
        entry_points=[CommandHandler("quiz", quiz), CommandHandler("quiz_subject", quiz_subject)],
        states={QUIZ: [MessageHandler(Filters.text & ~Filters.command, answer)]},
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    doubt_conv = ConversationHandler(
        entry_points=[CommandHandler("ask", ask)],
        states={ASK_DOUBT: [MessageHandler(Filters.text & ~Filters.command, receive_doubt)]},
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("currentaffairs", current_affairs))
    dp.add_handler(CommandHandler("ca_pdf", ca_pdf))
    dp.add_handler(CommandHandler("score", score))
    dp.add_handler(quiz_conv)
    dp.add_handler(doubt_conv)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
