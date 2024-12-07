import trollbot

bot = trollbot.Bot("TestBot", "#FF0000", "test!")

@bot.event("ready")
def funny():
    print("Holy shit it worked")

@bot.command()
def epico(ctx, argument):
    bot.send(f"You said: {argument}")

@bot.error("epico")
def epico_error(ctx, error):
    bot.send(f"The epico command returned an error! {error}")

@bot.unknown_command
def unknown_command(ctx, cmd):
    bot.send(f"Unknown command {cmd}")

def sample():
    bot.connect()