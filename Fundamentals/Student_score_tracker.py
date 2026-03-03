def show_menu():
    print("\n1) Add Student")
    print("2)Show all student records:")
    print("3)Show the top scorer")
    print("4)Show Average score")
    print("5)Exit")
    return int(input("Choose:"))

def add_student(records):
    name = input("Enter name: ") 
    score = int(input("Enter score: "))
    if 0<=score<=100:
        records.append((name,score))
    else:
        print("Invalid score")
    return records
def show_all(records):
    if not records:
        print("No records")
    else:
        for rec in records:
            print("Name:",rec[0],"Score:",rec[1])
def top_scorer(records):
    if not records:
        print("No records")
    else:
        top = records[0]
        for rec in records:
            if rec[1]>top[1]:
                top = rec
        print("Top scorer",top[0],"-",top[1])
def avg_score(records):
    if not records:
        print("No records")
    else:
        total = 0
        for rec in records:
            total += rec[1]
        avg = total / len(records)
        print("Average score:",avg)

records = []

while True:
    choice = show_menu()

    if choice == 1:
        records = add_student(records)

    elif choice == 2:
        show_all(records)
    elif choice == 3:
        top_scorer(records)
    elif choice == 4:
        avg_score(records)
    elif choice == 5:
        print("Bye!!")
        break
    else:
        print("Invaild choice")