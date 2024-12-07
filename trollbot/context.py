
class MessageContext:
    def __init__(self, raw):
        self.date = raw["date"]
        self.color = raw["color"]
        self.home = raw["home"]
        self.style = raw["style"]
        self.author = raw["nick"]