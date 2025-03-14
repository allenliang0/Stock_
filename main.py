from ibapi.client import EClient
from ibapi.wrapper import EWrapper
import time, datetime
from ibapi.client import Contract

from threading import Thread

init_symbol = "TSLA"

default_host = '127.0.0.1'
default_client_id = 1
paper_trading_port = 7497
live_trading_port = 7496
live_trading = False
trading_port = paper_trading_port
if live_trading:
    trading_port = live_trading_port

class IBClient(EWrapper, EClient):

    def __init__(self, host, port, client_id):
        EClient.__init__(self,self)

        self.connect(host, port, client_id)
        thread = Thread(target=self.run)
        thread.start()

    def error(self, req_id, code, msg, misc):
        if code in [2104, 2106, 2158]:
            print(msg)
        else:
            print('Error{}:{}'.format(code, msg))

    def historicalData(self, req_id, bar):
        print(bar)

    def historicalDataEnd(self, reqId: int, start: str, end: str):
        print(f"end of data {start} {end}")



client = IBClient(default_host,trading_port,default_client_id)
time.sleep(1)
contract = Contract()
contract.symbol = 'GOOG'
contract.secType = 'STK'
contract.exchange = 'SMART'
contract.currency = 'USD'
what_to_show = 'TRADES'

client.reqHistoricalData(
    2, contract, '', '30 D', '5 mins', what_to_show, True, 2, False, []
)
time.sleep(1)
