import time
from datetime import datetime
from zoneinfo import ZoneInfo

# timezone
tz_tokyo = ZoneInfo("Asia/Tokyo")

now = datetime.now(tz_tokyo)
print(f"ジョブ開始時間:{now.strftime('%x %X')}")

# 5秒待機
time.sleep(5)

now = datetime.now(tz_tokyo)
print(f"ジョブ終了時間:{now.strftime('%x %X')}")

