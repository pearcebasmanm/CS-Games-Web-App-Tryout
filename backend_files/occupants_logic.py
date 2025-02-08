from data import rooms

# Here is a method signature to get you started.

def check_occupants(room_number, date):
    room = rooms[room_number]
    for occupant in room["occupants"]:
        if occupant["check_in"] <= date <= occupant["check_out"]:
            return str(occupant)
    return "Not acceptable"
