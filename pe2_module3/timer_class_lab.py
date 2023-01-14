class Timer:
    def __init__(self, hh = 0, mm = 0, ss = 0):
        self.hh = hh
        self.mm = mm
        self.ss = ss
    
    def __str__(self):
        return str(f"{self.hh:02d}") + ':' + str(f"{self.mm:02d}") + ':' + str(f"{self.ss:02d}")
    
    def next_second(self):
        if self.ss == 59:
            self.ss = 0
            if self.mm == 59:
                self.mm = 0
                if self.hh == 23:
                    self.hh = 0
                else:
                    self.hh += 1
            else:
                self.mm += 1
        else:
            self.ss += 1
    
    def prev_second(self):
        if self.ss == 0:
            self.ss = 59
            if self.mm == 0:
                self.mm = 59
                if self.hh == 0:
                    self.hh = 23
                else:
                    self.hh -= 1
            else:
                self.mm -= 1
        else:
            self.ss -= 1
    
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)