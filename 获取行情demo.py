from sdk.gaoapi2 import GaoApi
from tqsdk.tafunc import time_to_str
api=GaoApi("086515","123456")

行情=api.获取_K线("SHFE.rb2101",10)
print(行情)
行情2=api.获取_tick("SHFE.rb2101")
print(行情2.last_price)
while True:
    api.wait_update()
    print(行情)
    print(time_to_str(行情.datetime.iloc[-1]))