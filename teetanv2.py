from zlapi import ZaloAPI
from zlapi.models import *
from clmm import Clmm

class TeeTan(ZaloAPI):
    def __init__(self, phone, passzl, imei, session_cookies):
        super().__init__(phone, passzl, imei=imei, session_cookies=session_cookies)
        self.phone=phone
        self.passzl=passzl
        self.imei=imei
        self.session_cookies=session_cookies
        self.money={}
        self.allow_group = []
        self.admin=['6949019840942160627']
    def onMessage(self, mid, author_id, message, message_object, thread_id, thread_type):
        try:
            if author_id != self.uid and thread_id in self.allow_group or author_id in self.admin:
                if author_id not in self.money:
                  self.money[author_id] = 100000
                self.markAsDelivered(mid, message_object.cliMsgId, author_id, thread_id, thread_type, message_object.msgType)
                self.markAsRead(mid, message_object.cliMsgId, author_id, thread_id, thread_type, message_object.msgType)
                
                print(f"Received message: {message} from {author_id} in thread {thread_id}, type {thread_type}, {message_object}")
                
                if not isinstance(message, str):
                    message = "[not a message]"
                if author_id in self.admin and message.startswith('Addgroup'):
                  id_group=message.split()[1]
                  self.allow_group.append(id_group)
                  print(self.allow_group)
                  reply=f'Đã thêm thành công bot vào nhóm có ID : {id_group}'
                  self.replyMessage(Message(text=reply), message_object, thread_id=thread_id, thread_type=thread_type)
                if message.startswith('Money'):
                  reply=f'Số Tiền Hiện Tại Của Bạn Là: {self.money[author_id]}'
                  self.replyMessage(Message(text=reply), message_object, thread_id=thread_id, thread_type=thread_type)
                  
                if message.startswith('Clmm'):
                    # Khởi tạo Clmm với đầy đủ các tham số cần thiết
                    clmm_instance = Clmm(self.phone, self.passzl, self.imei, self.session_cookies, self.money,mid, author_id, message, message_object, thread_id, thread_type)
                    clmm_instance.clmm()
        
        except Exception as e:
            print(e)
            reply = 'Bot đã xảy ra sự cố không xác định!'
            self.replyMessage(Message(text=reply), message_object, thread_id=thread_id, thread_type=thread_type)

client = TeeTan('</>', '</>', "a364337f-ace0-4285-8c97-a087533c4339-b78b4e2d6c0a362c418b145fe44ed73f", {"_ga":"GA1.2.854110349.1722652265","_gid":"GA1.2.1164327188.1722652265","_ga_VM4ZJE1265":"GS1.2.1722652265.1.0.1722652265.0.0.0","_ga_RYD7END4JE":"GS1.2.1722652267.1.1.1722652268.59.0.0","_zlang":"vn","zpsid":"Bjyp.362016986.0.fwOPea697CERUO_MJOaSmpJwRl1tkopoTx0azMl-a-PoPqHUG2oARYU97CC","zpw_sek":"gW9T.362016986.a0.B40yVIlaThBn5EMd2kHsib364za9tbJ7GRqZncNH8jSPhnkA6A0r-6YU6efSsKkGLiu1FGxNcEgsvT0aXe9siW","__zi":"3000.SSZzejyD6zOgdh2mtnLQWYQN_RAG01ICFjIXe9fEM8yuc-sYcaLGY7AJugRKGbA8SfFZfpCv.1","__zi-legacy":"3000.SSZzejyD6zOgdh2mtnLQWYQN_RAG01ICFjIXe9fEM8yuc-sYcaLGY7AJugRKGbA8SfFZfpCv.1","ozi":"2000.QOBlzDCV2uGerkFzm09LrMNTvFd62LVGBj_b_eWELT0kt-J_Cpa.1","app.event.zalo.me":"7370408023715644353"})
print('Bot ID:', client.uid)
client.listen()
