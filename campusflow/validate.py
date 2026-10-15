CATEGORIES = ["Network", "Hardware", "Software", "Other"]
URGENCIES = ["low", "medium", "high"]


def validate_title(title):
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Title cannot be blank.")
    return title.strip()


def validate_category(category):
    cleaned = str(category).strip().lower()
    for allowed in CATEGORIES:
        if allowed.lower() == cleaned:
            return allowed
    raise ValueError(f"Invalid category. Choose one of: {', '.join(CATEGORIES)}.")


def validate_urgency(urgency):
    cleaned = str(urgency).strip().lower()
    if cleaned in URGENCIES:
        return cleaned
    raise ValueError(f"Invalid urgency. Choose one of: {', '.join(URGENCIES)}.")


def validate_affected_users(value):
    message = "Affected users must be a whole number greater than 0."
    if isinstance(value, bool):
        raise ValueError(message)
    if isinstance(value, str):
        text = value.strip()
        if not text.isdigit():
            raise ValueError(message)
        value = int(text)
    if not isinstance(value, int) or value <= 0:
        raise ValueError(message)
    return value
