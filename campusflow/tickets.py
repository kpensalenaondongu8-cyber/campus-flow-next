from campusflow.calcualate_prio import calculate_priority
from campusflow.generate_id import generate_next_id
from campusflow.validate import validate_affected_users, validate_category, validate_title, validate_urgency


def create_ticket(tickets, title, category, urgency, affected_users):
    title = validate_title(title)
    category = validate_category(category)
    urgency = validate_urgency(urgency)
    affected_users = validate_affected_users(affected_users)

    ticket = {
        "id": generate_next_id(tickets),
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": calculate_priority(urgency, affected_users),
        "status": "open",
        "assigned_to": None,
    }
    tickets.append(ticket)
    return ticket