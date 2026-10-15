def search_tickets(tickets, query="", category=None, status=None, priority=None):
    """
    Search tickets with case-insensitive substring matching on title 
    and optional filters for category, status, and priority (combined with AND).
    """
    results = []
    cleaned_query = str(query).strip().casefold()
    
    clean_cat = str(category).strip().lower() if category else None
    clean_stat = str(status).strip().lower() if status else None
    clean_prio = str(priority).strip().lower() if priority else None

    for ticket in tickets:
        title = str(ticket.get("title", "")).casefold()
        if cleaned_query and cleaned_query not in title:
            continue

        if clean_cat and str(ticket.get("category", "")).lower() != clean_cat:
            continue

        if clean_stat and str(ticket.get("status", "")).lower() != clean_stat:
            continue

        if clean_prio and str(ticket.get("priority", "")).lower() != clean_prio:
            continue

        results.append(ticket)

    return results