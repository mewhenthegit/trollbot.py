import trollbot

# Initialize our bot
bot = trollbot.Bot("TestBot [test!]", "#FF0000", "test!")

# Whenever the bot joins the atrium, print this
@bot.event("ready")
def funny():
    print("Holy shit it worked")

# let your bot connect to trollbox
bot.connect()

def ignore(): pass # ignore this, do not put this in your code as it does absolutely nothing