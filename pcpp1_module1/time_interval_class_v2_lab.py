class Time:
    def __init__(self, hh, mm, ss):
        if (type(hh) != int) or (type(mm) != int) or (type(ss) != int):
            raise TypeError
        self.hh = hh
        self.mm = mm
        self.ss = ss
        
    def __add__(self, other):
        t1_secs = self.hh * 3600 + self.mm * 60 + self.ss
        t2_secs = other.hh * 3600 + other.mm * 60 + other.ss
        
        hh_added = (t1_secs + t2_secs) // 3600
        mm_added = (t1_secs + t2_secs - hh_added * 3600) // 60
        ss_added = (t1_secs + t2_secs - hh_added * 3600 - mm_added * 60)
        return f"{hh_added:02d}" + ":" + f"{mm_added:02d}" + ":" + f"{ss_added:02d}"

    def __sub__(self, other):
        t1_secs = self.hh * 3600 + self.mm * 60 + self.ss
        t2_secs = other.hh * 3600 + other.mm * 60 + other.ss
        
        hh_subbed = (t1_secs - t2_secs) // 3600
        mm_subbed = (t1_secs - t2_secs - hh_subbed * 3600) // 60
        ss_subbed = (t1_secs - t2_secs - hh_subbed * 3600 - mm_subbed * 60)
        return f"{hh_subbed:02d}" + ":" + f"{mm_subbed:02d}" + ":" + f"{ss_subbed:02d}"
    
    def __mul__(self, multiplier):
        t1_secs = self.hh * 3600 + self.mm * 60 + self.ss
        
        hh_mult = (t1_secs * multiplier) // 3600
        mm_mult = (t1_secs * multiplier - hh_mult * 3600) // 60
        ss_mult = (t1_secs * multiplier - hh_mult * 3600 - mm_mult * 60)
        return f"{hh_mult:02d}" + ":" + f"{mm_mult:02d}" + ":" + f"{ss_mult:02d}"
    
    def __str__(self):
        return f"{self.hh:02d}" + ":" + f"{self.mm:02d}" + ":" + f"{self.ss:02d}"

time1 = Time(12, 23, 42)
time2 = Time(13, 45, 29)
print(time1)
print(time2)
print("Added:", time1 + time2)
print("Subtracted:", time1 - time2)
print("="*15)

time3 = Time(00, 00, 00)
time4 = Time(23, 59, 59)
print(time3)
print(time4)
print("Added:", time3 + time4)
print("Subtracted:", time3 - time4)
print("="*15)

time5 = Time(6, 30, 30)
print(time5)
print("Multiplied:", time5 * 3)
print("="*15)

fti = Time(21, 58, 50)
sti = Time(1, 45, 22)
print(fti)
print(sti)
print("Added:", fti + sti) 
print("Subtracted:", fti - sti)
print("Multiplied:", fti * 2)
