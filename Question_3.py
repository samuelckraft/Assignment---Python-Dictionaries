service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(tickets, ticket_num, customer, issue, status):
    if ticket_num not in tickets:
        tickets[ticket_num] = {"Customer": customer, "Issue": issue, "Status": status}
        print(f"{ticket_num} added to tickets")
    else:
        print(f"Ticket '{ticket_num}' already exists")

def update_ticket(tickets, ticket_num, status):
    if ticket_num in tickets:
        tickets[ticket_num]["Status"] = status
        print(f"Status of {ticket_num} updated to {status}")
    else:
        print("Invalid ticket")

def display_tickets(tickets):
    for ticket_num, details in tickets.items():
        print(f"Ticket Number: {ticket_num} \nCustomer Name: {details['Customer']} \nIssue: {details["Issue"]} \nStatus: {details["Status"]}\n")

open_ticket(service_tickets, "Ticket003", "Sam", "Network issue", "closed")
update_ticket(service_tickets, "Ticket001", "closed")
display_tickets(service_tickets)