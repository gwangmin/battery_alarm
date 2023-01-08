# Macbook battery alarm
2021.2.25 ~  
tested on MacOS Mojave, python3.7
배터리 알람 기능이 필요한데 앱스토어는 고장이고 고객센터 답변은 맘에 들지 않아서 내가 만들어본거

if battery percent (percent <= 20) or (80 <= percent), alert via alarm app.
and write battery percent log.

- python battery_alarm.py check: battery check and alarm, battery percent log
- python battery_alarm.py state: print current state

* * * * * python /battery_alarm/battery_alarm.py check
