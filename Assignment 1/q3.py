while True:
    try:
        hour = int(input("Enter hour (0-23): "))
        minute = int(input("Enter minute (0-59): "))
        ampm = "AM"

        if(hour > 23 or hour < 0 or minute > 59 or minute < 0):
            print("Invalid time")
            break

        if(hour == 12):
            ampm = "PM"
        elif(hour == 0):
            hour = 12
        elif(hour > 12):
            hour -= 12
            ampm = "PM"

        if minute < 10:
            minute = f"0{minute}"
        
        print(f"The time is: {hour}:{minute} {ampm}")
    except:
        print("Invalid time")
        break