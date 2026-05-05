class Ticket:
    def __init__(self,ticket_id,holder_name):
        self.ticket_id = ticket_id
        self.holder_name = holder_name
    



class Event:
    def __init__(self,event_name,capacity):
        self.event_name = event_name
        self.capacity = capacity
        self.tickets = []
        self.next_ticket_id = 1
        
    def book_ticket(self,name):
        if len(self.tickets) >= self.capacity:
            return None
        
        ticket = Ticket(self.next_ticket_id, name)
        self.tickets.append(ticket)
        self.next_ticket_id += 1
        return ticket
    

    def cancel_ticket(self,ticket_id):
        for ticket in self.tickets:
            if ticket_id == ticket.ticket_id:
                self.tickets.remove(ticket)
                return

    def remaining_seats(self):
        return self.capacity - len(self.tickets)

    def list_attendees(self):
        arr = []
        for ticket in self.tickets:
            arr.append(ticket.holder_name)
        return arr



e = Event("Concert",3)

t1 = e.book_ticket("Alice")
t2 = e.book_ticket("Bob")
t3 = e.book_ticket("Charlie")

print(e.remaining_seats())   # 0

t4 = e.book_ticket("David")
print(t4)  # None (event full)

print(e.list_attendees())
# ['Alice','Bob','Charlie']

e.cancel_ticket(t2.ticket_id)

print(e.remaining_seats())   # 1

t5 = e.book_ticket("David")

print(e.list_attendees())
# ['Alice','Charlie','David']

e.cancel_ticket(100)  # non-existent
print(e.remaining_seats())   # 0