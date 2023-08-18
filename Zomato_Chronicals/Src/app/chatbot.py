# src/app/chatbot.py
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('ZomatoBot')
trainer = ChatterBotCorpusTrainer(bot)

# Train the bot on English language data
trainer.train('chatterbot.corpus.english')

while True:
    user_input = input('You: ')
    response = bot.get_response(user_input)
    print('ZomatoBot:', response)
