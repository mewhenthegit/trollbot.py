import trollbot

# Initialize our bot
bot = trollbot.Bot("TestBot [test!]", "#FF0000", "test!")

# Whenever the bot joins the atrium, print this
@bot.event("ready")
def funny():
    print("Holy shit it worked")

@bot.event("user join")
def userjoin(user):
    bot.send(f"Hello {user.nick}!")

@bot.event("user left")
def userbye(user):
    bot.send(f"Goodbye {user.nick}")

# let your bot connect to trollbox
bot.connect()

def ignore(): pass # ignore this, do not put this in your code as it does absolutely nothing