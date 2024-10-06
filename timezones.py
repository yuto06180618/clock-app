from datetime import timezone, timedelta


TIMEZONE_DICT = {  # ※ 夏時間は考慮していません
    "Africa/Johannesburg": timezone(timedelta(hours=2)),
    "America/Guatemala": timezone(timedelta(hours=-6)),
    "America/Halifax": timezone(timedelta(hours=-4)),
    "America/Los_Angeles": timezone(timedelta(hours=-8)),
    "Asia/Jakarta": timezone(timedelta(hours=7)),
    "Asia/Kolkata": timezone(timedelta(hours=5, minutes=30)),
    "Asia/Shanghai": timezone(timedelta(hours=8)),
    "Asia/Tokyo": timezone(timedelta(hours=9)),
    "Australia/Sydney": timezone(timedelta(hours=10)),
    "Europe/Berlin": timezone(timedelta(hours=1)),
    "Europe/London": timezone.utc,
    "Europe/Moscow": timezone(timedelta(hours=3)),
    "Pacific/Honolulu": timezone(timedelta(hours=-10)),
    "UTC": timezone.utc,
}
