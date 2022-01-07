# FCM 서버에 -> 파이썬 프로그램으로 -> API 호출 (기기 푸시알림 전송 요청)
import requests
import json

from pyfcm import FCMNotification


# 함수 제작 : 보내줄 문구 / 본문 내용을 받아서 전송.

def send_fcm_notificaion(title, body):
    
    # FCM 서버에 요청
    # 1. 호스트 주소 / 기능 주소 => 실제 기능 URL
    fcm_url = 'https://fcm.googleapis.com/fcm/send'
    
    # 2. 첨부해야할 파라미터 (보내줄 데이터)
    
    # 헤더에, 인증키 (token) 를 담아서 전달.
    fcm_headers = {
        'Authorization':'key=AAAAcyMDrYk:APA91bFfMLRhrFsm8gE0i07RAbnM7_JsD4CmrMoY-Uswh70tQFpPrPm9KHEvG_tNUJ44sgy0SRq0yRcfk_yhyIvsGEGPP5GRW2b6JjfXNyrrXRz1u9SEtxXXtDejjtdaXo4Eay1UnPO5',
        'Content-Type': 'application/json; UTF-8',
    }
    
    content = {
        'registration_ids':  'fkZ6zZkCRSuD9con9BNVmY:APA91bEIzvGvcp24XPm6PKA4V9WioJYbeVylj4FHUiWXlvfHZYJJ3pJd1jAXpEslhKvvqmxUI25Gdiny1NjLNvrmYilihhG5gIJpW0rYfPrS8FZ-X-FkzGbEsO5KgiSj5mQsNnp2LMDt',  # 어느 기기에 보낼건지, 디바이스 토큰 cf) 리스트로 넣으면, 여러 기기에 동시전송.
        'notification':{
            
            'title': title,
            'body': body,
            
        }, # 기본양식의 알림.  data-message 로 보내면 : 커스터마이징 지원 알림.
    }
    
    # 3. 어떤 방식  + 실제 API 호출.
    
    result = requests.post(fcm_url, data=json.dumps(content), headers=fcm_headers)
    print(f'FCM 발송 결과 : {result}')
    
    
# send_fcm_notificaion('안녕하세요', '파이썬을 통해서 보내봅니다.')


def send_fcm_by_library(title, body):
    push_service = FCMNotification(api_key='AAAAcyMDrYk:APA91bFfMLRhrFsm8gE0i07RAbnM7_JsD4CmrMoY-Uswh70tQFpPrPm9KHEvG_tNUJ44sgy0SRq0yRcfk_yhyIvsGEGPP5GRW2b6JjfXNyrrXRz1u9SEtxXXtDejjtdaXo4Eay1UnPO5')
    
    device_token = 'fkZ6zZkCRSuD9con9BNVmY:APA91bEIzvGvcp24XPm6PKA4V9WioJYbeVylj4FHUiWXlvfHZYJJ3pJd1jAXpEslhKvvqmxUI25Gdiny1NjLNvrmYilihhG5gIJpW0rYfPrS8FZ-X-FkzGbEsO5KgiSj5mQsNnp2LMDt'
    
    result = push_service.notify_single_device(registration_id=device_token, message_title=title, message_body=body)
    print(result)
    
# send_fcm_by_library('안녕하세요', '파이썬 pyfcm 라이브러리로 전송합니다.')

def send_sms_message(phone, message):
    aligo_url = 'https://apis.aligo.in/send/'
    aligo_api_key = 'i5m8plmyxhcpwfvty29hbzko2zzgi0nq'
    
    data = {
        'key' : aligo_api_key,
        'user_id' : 'cho881020',
        'sender' : '01051123237',
        'receiver': phone,
        'msg': message,
        'testmode_yn': 'y'
    }
    
    requests.post(url=aligo_url, data=data)
    
send_sms_message('01051123237', '파이썬으로 문자보내기')