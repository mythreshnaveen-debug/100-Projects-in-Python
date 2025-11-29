# Day 6 Project -- Focus Buddy
# In the Udemy course, they wanted us to write code in something called: 'Reeborg's World' which I thought didn't show a good understanding of what I know in Python,
# So I asked ChatGPT to generate a project that I can write in basic Python.
# This Project probably took the most time.
import warnings

# I actually never learned Dictionaries yet, so new stuff, but useful stuff!

# -------------------------------------
# FocusBuddy - Study & Break Planner
# -------------------------------------

# This list will store the tasks
tasks = []
session_plan = []
session_planned = False

def add_task(tasks_list):
    print("\n--- Add a Task ---")
    taskName = input("What is the name of the task? \n")
    taskMin = int(input("How much minutes will it take? \n"))
    taskPriority = int(input("How much priority will the task take? (1-5)\n"))

    newTask = {
        "Name": taskName,
        "Minutes": taskMin,
        "Priority": taskPriority
    }

    tasks_list.append(newTask)
    pass

def view_tasks(tasks):
    print("\n--- Your Tasks ---")
    if not tasks:
        print("You have not created any tasks.")
    else:
        iteration = 1
        for task in tasks:
            print(f"TASK #{iteration}")
            print(f"Task Name: {task.get("Name")}")
            print(f"Task will take {task.get("Minutes")} Minutes.")
            print(f"Task priority out of 5: {task.get("Priority")}")
            iteration += 1
    pass

def plan_session(tasks_list):
    print("\n--- Plan a Study Session ---")
    plan = []
    if not tasks_list:
        warnings.warn("There are no tasks.")
    else:
        minutes = int(input("How many minutes do you have?\n"))
        breakMin = int(input("How much minutes should each break be?\n"))
        sortedTasks = sorted(tasks_list, key=lambda x: x.get("Priority", 0)) #Learned this from Microsoft Copilot, super useful in coding.
        i = 0
        while minutes > 0 and i < len(sortedTasks):
            task = sortedTasks[i]
            requiredMinutes = task.get("Minutes")
            if requiredMinutes + breakMin <=minutes:
                minutes -= requiredMinutes
                minutes = minutes - breakMin
                task["BreakMinutes"] = breakMin
                plan.append(task)
            i += 1
            for task in plan:
                tasks_list.remove(task)
        print("STUDY PLAN:")
        it = 0
        for task in plan:
            print("Complete Task: " + task.get("Name"))
            print(f"This will take {task.get("Minutes")} minutes.")
            print(f"Then, take a break for {breakMin} Minutes.")
            if len(plan) - 1 != it:
                print("Next,")
            else:
                it += 1
        print("------")
    return plan

def run_session(plan):
    print("\n--- Start Session ---")
    if not plan:
        warnings.warn("No PLAN!")
        return
    else:
        for task in plan:
            print("Now, complete Task: " + task["Name"])
            input(f"Set a timer, for {task["Minutes"]} minutes, and press Enter once this timer has completed.")
            print("Now, take a break.")
            input(f"Set a timer for {task["BreakMinutes"]} minutes, and press Enter once this timer has completed.")
    print("Session Complete!")
    print("When you have more time, remember to create a new plan.")
    pass

# ---------------- Main Loop ----------------
# The code past this line is AI-Generated
def main():
    global session_plan, session_planned

    while True:
        print("\n===== FocusBuddy =====")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Plan a study session")
        print("4. Start study simulation")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            session_plan = plan_session(tasks)
            if len(session_plan) > 0:
                session_planned = True
        elif choice == "4":
            if session_planned:
                run_session(session_plan)
            else:
                print("You need to plan a session first!")
        elif choice == "5":
            print("Goodbye! Stay focused :)")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
