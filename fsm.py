import random

from transitions.extensions import GraphMachine

from utils import send_text_message, is_mami, compare, is_kazuya, is_command, send_image_message


love_name = "mami"


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    # love_consultant
    def is_going_to_love_consultant(self, event):
        text = event.message.text
        return text == "戀愛相談"

    def on_enter_love_consultant(self, event):
        print("I'm entering love_consultant")
        reply_token = event.reply_token
        send_text_message(reply_token,
                          "こんにちわ~マミちゃんですっヾ(〃^∇^)ﾉ\n好きな人の名前を入力してください。\n您好！我是Mami！\n請輸入心儀對象的姓名：")

    # idle
    def is_going_to_idle(self, event):
        text = event.message.text
        if is_command(text):
            return False
        return True

    def on_enter_idle(self, event):
        print("I'm entering idle")

        reply_token = event.reply_token
        num = random.randint(2, 4)
        if num == 2:
            send_image_message(reply_token, "https://i.imgur.com/GctntXv.jpg")
        elif num == 3:
            send_image_message(reply_token, "https://i.imgur.com/hHJHXDI.jpg")
        elif num == 4:
            send_image_message(reply_token, "https://i.imgur.com/uAQQ1ab.jpg")
        self.go_back()

    # mad
    def is_going_to_mad(self, event):
        text = event.message.text
        return is_kazuya(text)

    def on_enter_mad(self, event):
        print("I'm entering mad")
        url1 = 'https://i.imgur.com/23fugco.jpg'
        url2 = 'https://i.imgur.com/qgVR9fM.jpg'
        reply_token = event.reply_token
        num = random.randint(1, 3)
        if num == 1:
            send_text_message(reply_token, "幹X娘和也這個廢物的怎麼才剛被我甩掉就有新歡我肏他X的咧")
        elif num == 2:
            send_image_message(reply_token, url1)
        elif num == 3:
            send_image_message(reply_token, url2)

        self.go_back()

    # acquire_name
    def is_going_to_acquire_name(self, event):
        text = event.message.text
        global love_name
        love_name = '' + text
        if is_mami(text) or is_kazuya(text):
            return False
        return True

    def on_enter_acquire_name(self, event):
        print("I'm entering acquire_name")

        reply_token = event.reply_token
        num1 = compare(event.source.user_id, love_name)
        if num1 == 0:
            mess = "您與心上人的匹配度是：" + str(
                num1) + "%，強烈建議您趕緊轉換目標，免得受到太大的打擊喲^_^\nhttps://dict.revised.moe.edu.tw/dictView.jsp?ID=59617&la=0&powerMode=0"
        elif 0 < num1 <= 20:
            mess = "您與心上人的匹配度是：" + str(num1) + "%，建議您趕緊下船，免得迷失在茫茫大海中喲^_^！"
        elif 20 < num1 <= 40:
            mess = "您與心上人的匹配度是：" + str(num1) + "%，處於不高的數值，建議您試探一下對方的喜好，抓住對方的好感喲！"
        elif 40 < num1 <= 60:
            mess = "您與心上人的匹配度是：" + str(num1) + "%，可喜可賀！"
        elif 60 < num1 <= 80:
            mess = "您與心上人的匹配度是：" + str(num1) + "%，說不定稍微注意一下自身的形象，就能夠勾住對方的心囉！"
        elif 80 < num1 < 100:
            mess = "您與心上人的匹配度是：" + str(num1) + "%，看來您需要鼓起勇氣，踏出最勇敢的那一步囉*\\^0^/*！"
        else:
            mess = "您與心上人的匹配度是：" + str(num1) + "%，給我原地結婚！！！"

        send_text_message(reply_token, mess)
        self.go_back()

    def is_going_to_pride(self, event):
        text = event.message.text
        return is_mami(text)

    def on_enter_pride(self, event):
        print("I'm entering pride")
        reply_token = event.reply_token
        send_text_message(reply_token, "啊咧？可是我現在不想交男朋友耶 凸^_^凸")
        self.go_back()

    def is_going_to_help(self, event):
        text = event.message.text
        return text.lower() == "help"

    def on_enter_help(self, event):
        print("I'm entering idle")
        reply_token = event.reply_token
        send_text_message(reply_token,
                      "こんにちわ~マミちゃんですっヾ(〃^∇^)ﾉ\n您好！我是Mami！\n輸入「戀愛相談」，我會為您做戀愛匹配度分析喲～")
        self.go_back()