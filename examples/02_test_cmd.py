import trollbot

bot = trollbot.Bot("TestBot [test!]", "#FF0000", "test!")

@bot.event("ready")
def funny():
    print("Holy shit it worked")

@bot.unknown_command
def unknown_command(ctx, cmd):
    bot.send(f"Unknown command {cmd}")

@bot.command()
def testcmd(ctx, *argument):
    bot.send(f"{ctx.user.nick} said {''.join(argument)}")

@bot.error("testcmd")
def testcmd(ctx, error):
    bot.send(f"The testcmd command returned an error! {error}")

bot.connect()

def ignore(): pass # ignore this, do not put this in your code as it does absolutely nothing