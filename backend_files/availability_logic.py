from data import rooms

# Here is a method signature to get you started.

def check_room_availability(room_number, month, year):
    room = rooms[room_number]
    days = 0
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days = 29
        else:
            days = 28
    elif month in []:
        days = 30
    else:
        days = 31

    available = {}
    for day in range(1,days+1):
        available[day] = not any(occupant["check_in"] <= f"{year:04}-{month:02}-{day:02}" <= occupant["check_out"] for occupant in room["occupants"])

    return str(available)
