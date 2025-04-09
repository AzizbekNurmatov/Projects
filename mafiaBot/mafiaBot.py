import os
import telebot
from dotenv import load_dotenv
import math
import re

# Load environment variables
load_dotenv()

TOKEN = os.environ.get('BOT_TOKEN')
if not TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables. Please set it in your .env file.")

bot = telebot.TeleBot(TOKEN)

# Dictionary to store user-specific numbers and state
user_data = {}

# Define available operations
operations = {
    '/add': 'addition',
    '/subtract': 'subtraction',
    '/multiply': 'multiplication',
    '/divide': 'division',
    '/power': 'exponentiation',
    '/sqrt': 'square root',
    '/mod': 'modulo'
}

# Function to handle operations
def perform_operation(operation, num1, num2, message):
    try:
        if operation == '/add':
            total = num1 + num2
            bot.reply_to(message, f"The sum of {num1} and {num2} is: {total}")
        
        elif operation == '/subtract':
            total = num1 - num2
            bot.reply_to(message, f"The difference between {num1} and {num2} is: {total}")
        
        elif operation == '/multiply':
            total = num1 * num2
            bot.reply_to(message, f"The product of {num1} and {num2} is: {total}")
        
        elif operation == '/divide':
            if num2 == 0:
                bot.reply_to(message, "Error: Cannot divide by zero!")
                return
            total = num1 / num2
            bot.reply_to(message, f"The result of {num1} divided by {num2} is: {total}")
        
        elif operation == '/power':
            total = num1 ** num2
            bot.reply_to(message, f"{num1} raised to the power of {num2} is: {total}")
        
        elif operation == '/mod':
            if num2 == 0:
                bot.reply_to(message, "Error: Cannot perform modulo with zero!")
                return
            total = num1 % num2
            bot.reply_to(message, f"The remainder of {num1} divided by {num2} is: {total}")
        
        elif operation == '/sqrt':
            # For sqrt, we'll use the first number as the radicand and the second as the index
            if num2 == 0:
                bot.reply_to(message, "Error: Cannot have zero as root index!")
                return
            if num1 < 0 and num2 % 2 == 0:
                bot.reply_to(message, "Error: Cannot compute even root of negative number!")
                return
            total = num1 ** (1/num2)
            bot.reply_to(message, f"The {num2}th root of {num1} is: {total}")
        
        else:
            bot.reply_to(message, "Unknown operation. Please use one of the available commands.")
    
    except Exception as e:
        bot.reply_to(message, f"Error performing calculation: {str(e)}")

# Command to start interaction with the bot
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    instructions = (
        "Welcome to Calculator Bot! 🧮\n\n"
        "To use this bot:\n"
        "1. Enter two numbers separated by a space (e.g., '5.2 3')\n"
        "2. Then use one of these commands to perform operations:\n"
        "   • /add - Add the numbers\n"
        "   • /subtract - Subtract second from first\n"
        "   • /multiply - Multiply the numbers\n"
        "   • /divide - Divide first by second\n"
        "   • /power - Raise first to power of second\n"
        "   • /mod - Modulo (remainder)\n"
        "   • /sqrt - Calculate nth root (first number is the value, second is the root index)\n\n"
        "You can also use /clear to reset your numbers or /swap to swap the order of your numbers."
    )
    bot.reply_to(message, instructions)

# Command to clear stored numbers
@bot.message_handler(commands=['clear'])
def clear_numbers(message):
    chat_id = message.chat.id
    if chat_id in user_data:
        del user_data[chat_id]
        bot.reply_to(message, "Your stored numbers have been cleared. Enter two new numbers separated by a space.")
    else:
        bot.reply_to(message, "You don't have any stored numbers yet.")

# Command to swap the order of stored numbers
@bot.message_handler(commands=['swap'])
def swap_numbers(message):
    chat_id = message.chat.id
    if chat_id in user_data:
        num1, num2 = user_data[chat_id]
        user_data[chat_id] = (num2, num1)
        bot.reply_to(message, f"Numbers swapped! Now using: {num2} and {num1}")
    else:
        bot.reply_to(message, "You don't have any stored numbers yet. Enter two numbers separated by a space.")

# Handle operation commands
@bot.message_handler(commands=['add', 'subtract', 'multiply', 'divide', 'power', 'mod', 'sqrt'])
def handle_operations(message):
    chat_id = message.chat.id
    
    # Check if user has provided numbers
    if chat_id not in user_data:
        bot.reply_to(message, "Please provide two numbers first (example: '5 10').")
        return
    
    num1, num2 = user_data[chat_id]
    operation = message.text.split()[0]  # Get the command
    
    perform_operation(operation, num1, num2, message)

# Function to handle numeric input
@bot.message_handler(func=lambda message: re.match(r'^-?\d*\.?\d+\s+-?\d*\.?\d+$', message.text.strip()))
def handle_numbers(message):
    chat_id = message.chat.id
    text = message.text.strip()
    
    try:
        # Split and convert to float
        num1, num2 = map(float, text.split())
        
        # Store the numbers
        user_data[chat_id] = (num1, num2)
        
        reply = f"Numbers stored: {num1} and {num2}\n\nNow use one of these commands:\n"
        for cmd, desc in operations.items():
            reply += f"• {cmd} - for {desc}\n"
        reply += "\nOr use /swap to change the order, or /clear to reset."
        
        bot.reply_to(message, reply)
    
    except ValueError:
        bot.reply_to(message, "Invalid input. Please enter two numbers separated by a space (e.g., '5.2 3').")

# Catch-all for other messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Please enter two numbers separated by a space (e.g., '5.2 3') or use /help for instructions.")

# Start the bot
if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Bot polling error: {e}")