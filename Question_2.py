#Task 1

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_room(hotel, room_number, customer):
    if room_number in hotel:
        hotel[room_number]['status'] = 'booked'
        hotel[room_number]['customer'] = customer
        print(f"Room number {room_number} is booked by {customer}")
    else:
        print(f"{room_number} is not a valid room number")

def check_out_room(hotel, room_number):
    if room_number in hotel:
        if hotel[room_number]['status'] == 'booked':
            hotel[room_number]['status'] = 'available'
            print(f"{hotel[room_number]['customer']} has been checked out of {room_number}")
            hotel[room_number]['customer'] = ''
        else:
            print("Room already empty")
    else:
        print("Invalid room number please try again")

def display_rooms(hotel):
    for room, available in hotel.items():
        available = hotel_rooms[room]['status'].capitalize()
        print(f"Room: {room}, Status: {available}")


book_room(hotel_rooms, '101', 'John')
check_out_room(hotel_rooms, '102')
display_rooms(hotel_rooms)
print(hotel_rooms)