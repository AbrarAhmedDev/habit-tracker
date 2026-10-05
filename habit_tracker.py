habits = [
    ("Drink water", True),
    ("Read 10 pages", False),
    ("Exercise", True),
    ("Sleep 8 hours", True),
    ("Meditate", True)
    
]

for habit, completed in habits:
    if completed:
        print(habit + ": Done")
    else:
        print(habit + ": Not done")


def habit_report(habits):
    completed_count = sum(1 for habit, completed in habits if completed)

    return {
        "completed": completed_count,
        "total": len(habits)
    }


print(habit_report(habits))