import os
from telegram import Update, LabeledPrice
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace with your bot token
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Secure method (recommended)
# TOKEN = "YOUR_BOT_TOKEN"  # Hardcoded method (not recommended)

# Replace with your actual payment provider token
PAYMENT_PROVIDER_TOKEN = "YOUR_PAYMENT_PROVIDER_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send an invoice when the user starts the bot."""
    chat_id = update.message.chat_id

    await context.bot.send_invoice(
        chat_id=chat_id,
        title="Telegram Stars ⭐",
        description="Purchase 1⭐ using XTR currency.",
        payload="invoice_payload",  # Unique payload identifier
        provider_token=PAYMENT_PROVIDER_TOKEN,
        currency="XTR",  # Using XTR as currency
        prices=[LabeledPrice(label="1⭐", amount=100)],  # Amount in smallest unit
    )

async def precheckout(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Confirm checkout process."""
    query = update.pre_checkout_query
    await query.answer(ok=True)

async def successful_payment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle successful payment."""
    chat_id = update.message.chat_id
    await context.bot.send_message(chat_id, "Payment received! You have successfully purchased 1⭐.")

def main() -> None:
    """Start the bot."""
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("pre_checkout_query", precheckout))
    application.add_handler(CommandHandler("successful_payment", successful_payment))

    application.run_polling()

if __name__ == "__main__":
    main()
