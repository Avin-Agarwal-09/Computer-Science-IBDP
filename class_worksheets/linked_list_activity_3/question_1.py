def cancel_reservation(self, seat_number):
    current = self.head
    while current is not None:
        if current.seat_number == seat_number:
            current.prev.next = current.next 
            current.next.prev = current.prev  
            current.next = None            
            current.prev = None
            print("Seat " + str(seat_number) + " cancelled")
            return
        current = current.next
    print("Seat " + str(seat_number) + " not found")


def print_manifest_reverse(self):
    current = self.tail
    while current is not None:
        print(current.passenger_name, current.seat_number)
        current = current.prev


def terminate_process(self, pid):
    previous = self.head
    current = self.head.next
    while current is not self.head: 
        if current.pid == pid:
            previous.next = current.next 
            current.next = None
            print("Process " + str(pid) + " terminated")
            return
        previous = current
        current = current.next
    print("Process " + str(pid) + " not found")


def execute_cycle(self):
    if self.head is None:
        return
    current = self.head
    while True:
        current.burst_time -= 1
        print("PID " + str(current.pid) + " executed: " + str(current.burst_time) + " remaining")
        current = current.next
        if current is self.head:
            break