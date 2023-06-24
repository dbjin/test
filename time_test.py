import requests
import my_util

url = "http://api.coolsms.co.kr/messages/v4/send"
headers = my_util.get_headers(
    "NCSGRLWL3ZGZV1LC", "KRASXRLVWMZYNRCCIJV6EO5AYIHMQ0II")
data = '{"message":{"to":"01050931826","from":"01050931826","text":"hello world"}}'

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
print(response.text)

if response.status_code == 200:
    print("메시지가 발송되었습니다.")
else:
    print("메시지가 발송되지 않았습니다.")
