import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

# timezone
tz_tokyo = ZoneInfo("Asia/Tokyo")

# 引数参照
args = sys.argv

now = datetime.now(tz_tokyo)
print(f"ジョブ開始時間:{now.strftime('%x %X')}")
if 1 < len(args):
    print(f"引数:{args[1]}")

# 5秒待機
time.sleep(5)

now = datetime.now(tz_tokyo)
print(f"ジョブ終了時間:{now.strftime('%x %X')}")

