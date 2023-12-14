from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        self.close() 

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            self.send(text_data=text_data)
        elif bytes_data:
            self.send(bytes_data=bytes_data)

