import httpx
import threading
import redis
from datetime import timedelta


def thread(name):
    con = redis.Redis(host="localhost", port=6379, decode_responses=True)
    response = httpx.get(f"https://{name}")
    data = response.content
    con.set(name=name, value=data, ex=timedelta(seconds=60))


oqim1 = threading.Thread(target=thread, args=('daryo.uz',))
oqim2 = threading.Thread(target=thread, args=("xabar.uz",))
oqim3 = threading.Thread(target=thread, args=("leetcode.com",))
oqim4 = threading.Thread(target=thread, args=("kun.uz",))
oqim5 = threading.Thread(target=thread, args=("wikipedia.org",))

oqim1.start()
oqim2.start()
oqim3.start()
oqim4.start()
oqim5.start()

oqim1.join()
oqim2.join()
oqim3.join()
oqim4.join()
oqim5.join()
#cheking
# connection = redis.Redis(host="localhost", port=6379, decode_responses=True)
# print(connection.get('kun.uz'))