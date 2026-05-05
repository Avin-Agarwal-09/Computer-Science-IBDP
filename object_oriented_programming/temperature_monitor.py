class TemperatureMonitor:
    def __init__(self):
        self.readings = []
    
    def add_reading(self,temp):
        self.readings.append(temp)

    def highest(self):
        return max(self.readings)
    
    def lowest(self):
        return min(self.readings)
    
    def last_n_readings(self,n):
        return self.readings[-n:]
    
    def trend(self):
        if self.readings[-1] > self.readings[-2]:
            return "rising"
        if self.readings[-1] < self.readings[-2]:
            return "falling"
        else:
            return "stable"

t = TemperatureMonitor()

t.add_reading(25)
t.add_reading(27)
t.add_reading(29)
t.add_reading(28)

print(t.highest())    # 29
print(t.lowest())     # 25

print(t.last_n_readings(2))  # [29,28]

print(t.trend())      # falling
    