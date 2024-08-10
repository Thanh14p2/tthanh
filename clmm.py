from zlapi import ZaloAPI
from zlapi.models import *
import time
class Clmm(ZaloAPI):  # Kế thừa từ ZaloAPI
    def __init__(self, phone, passzl, imei, session_cookies, money,mid, author_id, message, message_object, thread_id, thread_type):
        # Khởi tạo lớp cha ZaloAPI
        super().__init__(phone, passzl, imei=imei, session_cookies=session_cookies)
        
        # Khởi tạo các thuộc tính riêng của Clmm
        self.money=money
        self.mid = mid
        self.author_id = author_id
        self.message = message
        self.message_object = message_object
        self.thread_id = thread_id
        self.thread_type = thread_type
    def xuly(self,result,opt):
      if opt == 'T' or opt == 'X':
        if result > 5 :
          return "Tài"
        if result <= 5:
          return "Xỉu"
      if opt == 'C' or opt == 'L':
        if result % 2 == 0:
          return "Chẵn"
        else:
          return "Lẻ"
    def clmm(self):
      try:
        opt=self.message.split()[1]
        tien=int(self.message.split()[2])
        option=['T','X','C','L']
        if opt not in option:
          reply='Sai Lựa Chọn\nTài:T\nXỉu:X\nChẵn:C\nLẻ:L'
          self.replyMessage(Message(text=reply), self.message_object, thread_id=self.thread_id, thread_type=self.thread_type)
          return
        if tien < 10000:
          reply='Hết tiền à em min 10000 dell có thì next'
          self.replyMessage(Message(text=reply), self.message_object, thread_id=self.thread_id, thread_type=self.thread_type)
          return
        if self.money[self.author_id] < 10000 or tien > self.money[self.author_id]:
          reply='Tiền Thì Dell Có Mà Đòi Chơi À Mày😎'
          self.replyMessage(Message(text=reply), self.message_object, thread_id=self.thread_id, thread_type=self.thread_type)
          return
        else:
          magd=int(time.time())
          print(magd)
          total_dice = int(magd % 10)
          is_even = total_dice % 2 == 0 
          ketqua=self.xuly(total_dice,opt)
          if ( (opt == 'T' and total_dice > 5) or
     (opt == 'X' and total_dice <= 5) or
     (opt == 'C' and is_even) or
     (opt == 'L' and not is_even) ):
    # Thực hiện hành động nếu một trong các điều kiện trên đúng

            self.money[self.author_id] += int(tien * 1.5)
            reply=f'Thắng\nKết Quả:{ketqua}\nMã Giao Dịch:{magd}\nSố Tiền Hiện Tại Của Bạn Là: {self.money[self.author_id]}'
            self.replyMessage(Message(text=reply), self.message_object, thread_id=self.thread_id, thread_type=self.thread_type)
          else:
            self.money[self.author_id] -= tien
            reply=f'Thua\nKết Quả:{ketqua}\nMã Giao Dịch:{magd}\nSố Tiền Hiện Tại Của Bạn Là: {self.money[self.author_id]}'
            self.replyMessage(Message(text=reply), self.message_object, thread_id=self.thread_id, thread_type=self.thread_type)
      except:
        reply='Cách Chơi: Clmm T/X/C/L Tiền'
        self.replyMessage(Message(text=reply), self.message_object, thread_id=self.thread_id, thread_type=self.thread_type)