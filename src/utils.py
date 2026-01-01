from datetime import date, datetime
import time


# 입력받은 data를 int type으로 바꿔 반환하는 함수 만약 불가능하면 None을 반환
def to_int(data: str | int) -> int | None:
    if isinstance(data, int):
        return data

    elif isinstance(data, str):
        try:
            return int(data)
        except ValueError:
            return None

    else:
        return None


# 오늘 날짜를 얻는 함수
def get_today():
    today: str = str(date.today())
    return today


# 제대로 된 날짜 형식인지 확인하는 함수
def check_date_format(d: str) -> bool:
    try:
        datetime.strptime(d, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# 오늘 날짜를 "YYYY-MM" 형식으로 반환
def get_today_ym() -> str:
    ym: str = datetime.now().strftime("%Y-%m")
    return ym
