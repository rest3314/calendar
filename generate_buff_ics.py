from ics import Calendar, Event
from datetime import datetime, timedelta

# === 설정 ===
first_start = datetime(2026, 2, 22, 10, 14)  # 첫 버프 시작 시점
end_of_day = datetime(2026, 2, 22, 23, 59)  # 오늘 하루 종료
buff_interval = 90  # 버프 간격(분)
buff_duration = 10  # 버프 제공 시간(분)

# === 캘린더 생성 ===
c = Calendar()
count = 0

while first_start < end_of_day:
    e = Event()
    e.name = "버프 시작"
    e.begin = first_start
    e.end = first_start + timedelta(minutes=buff_duration)
    c.events.add(e)

    first_start += timedelta(minutes=buff_interval)
    count += 1

print(f"오늘 하루 최대 버프 횟수: {count}")

# ICS 파일 저장
with open("buff.ics", "w", encoding="utf-8") as f:
    f.writelines(c)
