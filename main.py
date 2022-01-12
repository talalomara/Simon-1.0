# Importing chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Create object of ChatBot class
bot = ChatBot(
    name = 'Simon', read_only = True)


corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')

while True:
    try:
        bot_input = input("You: ")
        bot_response = bot.get_response(bot_input)
        print(f"{bot.name}: {bot_response}")
    except(KeyboardInterrupt,SystemExit, EOFError):
        break