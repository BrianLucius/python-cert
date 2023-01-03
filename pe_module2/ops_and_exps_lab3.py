hour = int(input("Starting time (hours): "))
minutes = int(input("Starting time (minutes): "))
dur = int(input("Event duration (minutes: "))

end_hour = (hour + ((minutes+dur)//60)) % 24
end_minutes = (minutes + dur) % 60 

print("End time: ", str(end_hour)+":"+str(end_minutes))