class Notification:
    def send(self):
        return None


class EmailNotification(Notification):
    def __init__(self, receiver):
        self.receiver = receiver
    
    def send(self):
        return (f"Email sent to {self.receiver}:")
        

class SMSNotification(Notification):
    def __init__(self, receiver):
        self.receiver = receiver
    
    def send(self):
        return (f"SMS sent to {self.receiver}:")

def broadcast(notifications_list ,message):
    for i in range(len(notifications_list)):
        print(f"{notifications_list[i].send()} {message}")




email = EmailNotification("user@email.com")
sms = SMSNotification("+6588888888")

broadcast([email, sms], "Exam Tomorrow")

