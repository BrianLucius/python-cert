class Time:
    def __init__(self, hh, mm, ss):
        if (type(hh) != int) or (type(mm) != int) or (type(ss) != int):
            raise TypeError
        self.hh = hh
        self.mm = mm
        self.ss = ss
        
    def __add__(self, other):
        ss_added = (self.ss + other.ss) % 60
        mm_added = (self.mm + other.mm + ((self.ss + other.ss) // 60)) % 60
        hh_added = (self.hh + other.hh + ((self.mm + other.mm) // 60)) % 24
        return f"{hh_added:02d}" + ":" + f"{mm_added:02d}" + ":" + f"{ss_added:02d}"

    def __sub__(self, other):
        ss_subbed = (self.ss - other.ss) if (self.ss - other.ss) >= 0 else 60 + (self.ss - other.ss)
        mm_subbed = (self.mm - other.mm) if (self.mm - other.mm - ((self.ss - other.ss) < 0)) >= 0 else 60 + (self.mm - other.mm - ((self.ss - other.ss) < 0))
        hh_subbed = (self.hh - other.hh) if (self.hh - other.hh - ((self.mm - other.mm) < 0)) >= 0 else 24 + (self.hh - other.hh - ((self.mm - other.mm) < 0))
        return f"{hh_subbed:02d}" + ":" + f"{mm_subbed:02d}" + ":" + f"{ss_subbed:02d}"
    
    def __mul__(self, multiplier):
        ss_mult = (self.ss * multiplier) % 60
        mm_mult = (self.mm * multiplier + ((self.ss * multiplier) // 60)) % 60
        hh_mult = (self.hh * multiplier + ((self.mm * multiplier) // 60))
        return f"{hh_mult:02d}" + ":" + f"{mm_mult:02d}" + ":" + f"{ss_mult:02d}"
    
    def __str__(self):
        return f"{self.hh:02d}" + ":" + f"{self.mm:02d}" + ":" + f"{self.ss:02d}"

time1 = Time(12, 23, 42)
time2 = Time(13, 45, 29)
print(time1)
print("Added:", time1 + time2)  

time3 = Time(00, 00, 00)
time4 = Time(23, 59, 59)
print("Subtracted:", time3 - time4)

time5 = Time(6, 30, 30)
print("Multiplied:", time5 * 3)

fti = Time(21, 58, 50)
sti = Time(1, 45, 22)
print("Added:", fti + sti) 
print("Subtracted:", fti - sti)
print("Multiplied:", fti * 2)
