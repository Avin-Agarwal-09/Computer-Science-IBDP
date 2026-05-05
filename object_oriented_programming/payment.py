class PaymentMethod:
    def pay(self,amount):
        return None
    
class CreditCard(PaymentMethod):
    def __init__(self,CardNo):
        self.CardNo = CardNo
 
    def pay(self,amount):
        return f"Paid {amount} using Credit Card ending {self.CardNo}"


class PayPal(PaymentMethod):
    def __init__(self,Email):
        self.Email = Email

    def pay(self,amount):
        return f"Paid {amount} using PayPal account{self.Email}"

def process_payment(method,amount):
    print(method.pay(amount))


card = CreditCard("1234")
paypal = PayPal("abc@email.com")

process_payment(card, 100) #Paid $100 using Credit Card ending 1234
process_payment(paypal, 200) # Paid $200 using PayPal account abc@email.com