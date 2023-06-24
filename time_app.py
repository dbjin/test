import time
import requests
import datetime
import my_util


def is_6pm():
    # 현재 시간이 6시인지 확인
    current_time = time.localtime()
    return current_time.tm_hour == 18


def is_holiday():
    # 오늘이 휴일인지 확인
    today = datetime.date.today()
    holidays = ["2023-01-01", "2023-02-12", "2023-03-09", "2023-05-05",
                "2023-05-15", "2023-09-06", "2023-10-03", "2023-10-09", "2023-12-25"]
    return today in holidays


def is_weekend():
    # 오늘이 주말인지 확인
    day = datetime.date.today().weekday()
    return day == 5 or day == 6


while True:
    # 1분에 한번씩 현재 시간을 검사
    if is_6pm() and not is_holiday() and not is_weekend():
        # 쿨에스엠에스에 메시지를 발송
        url = "http://api.coolsms.co.kr/messages/v4/send-many"
        headers = my_util.get_headers(
            "NCSGRLWL3ZGZV1LC", "KRASXRLVWMZYNRCCIJV6EO5AYIHMQ0II")
        data = '{"message":{"to":"01050931826","from":"01050931826","text":"저녁 6시입니다."}}'

        response = requests.post(url, headers=headers, data=data)
        print(response.status_code)
        print(response.text)

    time.sleep(60)
