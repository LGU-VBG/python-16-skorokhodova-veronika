class HourClock:
    def __init__(self, hours):
        if not isinstance(hours, int) or not (1 <= hours <= 12):
            raise ValueError("Некорректное время")
        self._hours = hours
    
    @property
    def hours(self):
        return self._hours
    
    @hours.setter
    def hours(self, value):
        if not isinstance(value, int) or not (1 <= value <= 12):
            raise ValueError("Некорректное время")
        self._hours = value


time = HourClock(7)
print(time.hours)
time.hours = 9
print(time.hours)

time = HourClock(7)
try:
    time.hours = 15
except ValueError as e:
    print(e)

try:
    HourClock('pizza time 🕷')
except ValueError as e:
    print(e)