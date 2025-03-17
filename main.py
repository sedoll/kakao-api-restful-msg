import requests
import json

# 🔹 저장된 토큰 불러오기
with open("kakao_code_exam.json", "r") as fp:
    tokens = json.load(fp)

# 🔹 API URL
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 🔹 요청 헤더
headers = {
    "Authorization": "Bearer " + tokens["access_token"],
    "Content-Type": "application/x-www-form-urlencoded"
}

# 🔹 리스트 템플릿 데이터
data = {
    "template_object": json.dumps({
        "object_type": "list",
        "header_title": "리스트 템플릿 제목",
        "header_link": {
            "web_url": "https://media.naver.com/press/055/ranking?type=popular",
            "mobile_web_url": "https://media.naver.com/press/055/ranking?type=popular"
        },
        "contents": [
            {
                "title": "네이버",
                "image_url": "",
                "description": "네이버",
                "link": {
                    "web_url": "https://naver.com",
                    "mobile_web_url": "https://naver.com"
                }
            },
            {
                "title": "카카오",
                "image_url": "",
                "description": "카카오",
                "link": {
                    "web_url": "https://kakao.com",
                    "mobile_web_url": "https://kakao.com"
                }
            }
        ],
        "buttons": [
            {
                "title": "뉴스 전체 보기",
                "link": {
                    "web_url": "https://media.naver.com/press/055/ranking?type=popular",
                    "mobile_web_url": "https://media.naver.com/press/055/ranking?type=popular"
                }
            }
        ]
    })
}

# 🔹 API 요청
response = requests.post(url, headers=headers, data=data)

# 🔹 응답 확인
print("응답 코드:", response.status_code)
print("응답 내용:", response.text)
