# FCM 서버에 -> 파이썬 프로그램으로 -> API 호출 (기기 푸시알림 전송 요청)
import requests

# 함수 제작 : 보내줄 문구 / 본문 내용을 받아서 전송.

def send_fcm_notificaion(title, body):
    
    # FCM 서버에 요청
    # 1. 호스트 주소 / 기능 주소 => 실제 기능 URL
    url = 'https://fcm.googleapis.com/fcm/send'
    
    # 2. 첨부해야할 파라미터 (보내줄 데이터)
    
    # 헤더에, 인증키 (token) 를 담아서 전달.
    headers = {
        'Authorization':'key=AAAAcyMDrYk:APA91bFfMLRhrFsm8gE0i07RAbnM7_JsD4CmrMoY-Uswh70tQFpPrPm9KHEvG_tNUJ44sgy0SRq0yRcfk_yhyIvsGEGPP5GRW2b6JjfXNyrrXRz1u9SEtxXXtDejjtdaXo4Eay1UnPO5',
        'Content-Type': 'application/json; UTF-8',
    }
    
    # 3. 어떤 방식 
    