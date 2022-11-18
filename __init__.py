from mycroft import MycroftSkill, intent_file_handler


class StockTrading(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('trading.stock.intent')
    def handle_trading_stock(self, message):
        self.speak_dialog('trading.stock')


def create_skill():
    return StockTrading()

