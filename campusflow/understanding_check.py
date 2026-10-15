QUESTIONS = [
    {
        "id": "Q1",
        "prompt": "Ticket T001 is open and unassigned. A user tries to move it to in_progress.",
        "options": {
            "A": "Accept",
            "B": "Reject and preserve all data",
            "C": "Resolve it automatically",
            "D": "Remove ticket"
        },
        "answer": "B"
    },
    {
        "id": "Q2",
        "prompt": "The app has zero tickets. What should resolution percentage display?",
        "options": {
            "A": "Crash",
            "B": "100%",
            "C": "0%",
            "D": "Divide by one without explanation."
        },
        "answer": "C"
    },
    {
        "id": "Q3",
        "prompt": "Filter title='wifi', category='Network', status='open'. Which records should match?",
        "options": {
            "A": "Any record matching one filter",
            "B": "Only records matching all supplied filters",
            "C": "All network records",
            "D": "All open records."
        },
        "answer": "B"
    },
    {
        "id": "Q4",
        "prompt": "A resolved ticket receives 'Add note'. What should happen?",
        "options": {
            "A": "Append anyway",
            "B": "Delete old notes",
            "C": "Reject until reopened",
            "D": "Change status silently."
        },
        "answer": "C"
    },
    {
        "id": "Q5",
        "prompt": "The JSON file includes two tickets with the same ID. What should load do?",
        "options": {
            "A": "Keep both",
            "B": "Replace memory with duplicates",
            "C": "Reject the load without changing current memory",
            "D": "Rename IDs silently."
        },
        "answer": "C"
    },
    {
        "id": "Q6",
        "prompt": "A PR changes validation but has no negative-case tests. Best review action?",
        "options": {
            "A": "Approve because it runs",
            "B": "Request focused tests and reasoning",
            "C": "Merge immediately",
            "D": "Ask AI to approve it."
        },
        "answer": "B"
    }
]

def run_understanding_check():
    print("\n--- Engineering Understanding Check ---")
    score = 0
    responses = {}

    for q in QUESTIONS:
        print(f"\n{q['id']}: {q['prompt']}")
        for opt, text in q['options'].items():
            print(f"  {opt}. {text}")
        
        while True:
            choice = input("Your choice (A/B/C/D): ").strip().upper()
            if choice in q['options']:
                break
            print("Invalid choice. Please enter A, B, C, or D.")

        responses[q['id']] = choice
        if choice == q['answer']:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer was {q['answer']}.")

    print(f"\nYour Final Score: {score} / {len(QUESTIONS)}")
    return score, responses