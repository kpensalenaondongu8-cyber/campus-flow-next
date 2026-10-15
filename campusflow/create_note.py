def add_note_ticket(tickets, ticket_id, author, message):

    ticket_found = False
    for item in tickets:
        if str(item.get("id")).upper() == str(ticket_id).upper:
            ticket_found == True

        if "notes" not in item:
            item["notes"] = []

        status = item["status"]
        if status not in ["open", "in_progress"]:
            raise ValueError(f"can not add note to a ticket with {status} status")

        next_note = len(item["notes"]) +1
        note_id  = f"N{next_note:03d}"

        full_note_id = f"{ticket_id}-{note_id}"

        new_note = {
            "note_id": full_note_id,
            "author": author,
            "message": message
        }       
        item["notes"].append(new_note)
        return item

    if ticket_found == False:
        raise ValueError("Ticket not found")