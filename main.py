
from campusflow.storage import load_tickets, save_tickets
from campusflow.reports import build_report, format_report
from campusflow.create_note import add_note_ticket
from campusflow.storage import StorageError, load_tickets, save_tickets
from campusflow.validate import (
    CATEGORIES,
    URGENCIES,
    validate_affected_users,
    validate_category,
    validate_title,
    validate_urgency,
    validate_author,
    validate_message
)
from campusflow.tickets import create_ticket
from campusflow.ticket_views import list_tickets, view_ticket
from campusflow.workflow import assign_ticket, update_status, get_work_queue
#from campusflow.reports import build_report, format_report, CATEGORIES
from campusflow.search import search_tickets
from campusflow.understanding_check import run_understanding_check
# from campusflow.create_note import add_note_ticket


def handle_create(tickets):
    title = input("Enter ticket title: ")
    category = input(f"Enter category ({', '.join(CATEGORIES)}): ")
    urgency = input("Enter urgency (critical, high, medium, low): ")
    try:
        affected_users = int(input("Enter affected users count: "))
        ticket = create_ticket(tickets, title, category, urgency, affected_users)
        save_tickets(tickets)
        print(f"Success! Created ticket {ticket['id']} with priority '{ticket['priority']}'.")
    except ValueError as e:
        print(f"Error creating ticket: {e}")

def handle_list(tickets):
    list_tickets(tickets)

def handle_view(tickets):
    ticket_id = input("Enter ticket ID to view: ")
    ticket = view_ticket(tickets, ticket_id)
    if ticket:
        print(f"\n--- Ticket {ticket['id']} ---")
        for k, v in ticket.items():
            print(f"  {k}: {v}")
    else:
        print("Ticket not found.")

def handle_assign(tickets):
    ticket_id = input("Enter ticket ID to assign: ")
    name = input("Enter assignee name: ")
    try:
        assign_ticket(tickets, ticket_id, name)
        save_tickets(tickets)
        print(f"Ticket {ticket_id} successfully assigned to {name.strip()}.")
    except ValueError as e:
        print(f"Assignment failed: {e}")

def handle_status(tickets):
    ticket_id = input("Enter ticket ID: ")
    new_status = input("Enter new status (in_progress / resolved / reopen): ")
    try:
        update_status(tickets, ticket_id, new_status)
        save_tickets(tickets)
        print(f"Ticket {ticket_id} status updated successfully.")
    except ValueError as e:
        print(f"Status update failed: {e}")
    ticket_id = read_ticket_id()
    new_status = input("Enter new status (open / in_progress / resolved): ")
    ticket = update_status(tickets, ticket_id, new_status.strip().lower())
    save_tickets(tickets)
    print(f"Ticket {ticket['id']} is now '{ticket['status']}'.")


def handle_add_note(tickets):
    ticket_id = read_ticket_id()
    
    ticket = find_ticket(tickets, ticket_id)
    if ticket is None:
        print(f"Error: Ticket '{ticket_id}' not found.")
        return
        
    author = ask("Enter your name (Author): ", validate_author).strip()
    message = ask("Enter note message: ", validate_message).strip()
    
    if not author or not message:
        print("Error: Author and message fields cannot be empty.")
        return

    ticket = add_note_ticket(tickets, ticket_id, author, message)
    save_tickets(tickets)
    print(f"Successfully added note to Ticket {ticket_id}!")


def handle_queue(tickets):
    queue = get_work_queue(tickets)
    if not queue:
        print("Work queue is empty.")
        return
    print("\n--- Active Work Queue ---")
    for t in queue:
        print(f"ID: {t['id']} | Priority: {t['priority']} | Status: {t['status']} | Title: {t['title']}")

def handle_report(tickets):
    report = build_report(tickets)
    print("\n" + format_report(report))

def handle_search(tickets):
    query = input("Enter title keyword (leave blank to skip): ").strip()
    cat_input = input(f"Enter category ({', '.join(CATEGORIES)} or blank): ").strip()
    stat_input = input("Enter status (open / in_progress / resolved or blank): ").strip()
    prio_input = input("Enter priority (critical / high / medium / low or blank): ").strip()

    category = cat_input if cat_input else None
    status = stat_input if stat_input else None
    priority = prio_input if prio_input else None

    results = search_tickets(tickets, query=query, category=category, status=status, priority=priority)
    
    if not results:
        print("No matching tickets found.")
        return

    print(f"\nFound {len(results)} matching ticket(s):")
    for ticket in results:
        print(
            f"ID: {ticket['id']} | Title: {ticket['title']} | "
            f"Cat: {ticket['category']} | Status: {ticket['status']} | "
            f"Priority: {ticket['priority']}"
        )

def handle_understanding_check(tickets):
    run_understanding_check()


MENU = """
------ CampusFlow ------
1. Create ticket
2. List all tickets
3. View one ticket
4. Assign ticket
5. Change status 
6. Work queue
7. Report
8. Search tickets
9. Engineering Understanding Check
0. Exit"""

ACTIONS = {
    "1": handle_create,
    "2": handle_list,
    "3": handle_view,
    "4": handle_assign,
    "5": handle_status,
    "6": handle_queue,
    "7": handle_report,
    "8": handle_search,
    "9": handle_understanding_check,
}

def main():
    tickets = load_tickets()
    while True:
        print(MENU)
        choice = input("Enter choice: ").strip()
        if choice == "0":
            print("Exiting CampusFlow. Goodbye!")
            break
        action = ACTIONS.get(choice)
        if action:
            action(tickets)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()