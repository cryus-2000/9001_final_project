from Task import Task
from TaskManager import TaskManager


def main():
    manager = TaskManager("data.json")

    while True:
        print("""
Photographer Task Manager
-----------------------------
1. Add Task
2. View All Tasks (Sorted by Date)
3. Delete Task
4. Update Task
5. View Statistics (Total Tasks(completed and uncompleted) / Total Price)
6. Exit
-----------------------------
""")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            try:
                try:
                    num_people = int(input("Number of people (>=1): "))
                    if num_people < 1:
                        raise ValueError("Number of people must be >= 1.")
                except ValueError as ve:
                    print(f"Invalid number of people: {ve}")
                    continue

                try:
                    time_period = input("Time of shoot (day/night): ").strip().lower()
                    if time_period not in ['day', 'night']:
                        raise ValueError("Time period must be 'day' or 'night'.")
                except ValueError as ve:
                    print(f"Invalid time period: {ve}")
                    continue

                try:
                    location_type = input("Location type (indoor/outdoor): ").strip().lower()
                    if location_type not in ['indoor', 'outdoor']:
                        raise ValueError("Location type must be 'indoor' or 'outdoor'.")
                except ValueError as ve:
                    print(f"Invalid location type: {ve}")
                    continue

                location_detail = input("Specific location: ").strip()
                cosplay_role = input("Cosplay role: ").strip()

                try:
                    shoot_date_input = input("Shoot date (YYYY-MM-DD): ").strip()
                    datetime.strptime(shoot_date_input, '%Y-%m-%d')
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    continue

                task = Task(num_people, time_period, location_type, location_detail, cosplay_role, shoot_date_input)
                manager.add_task(task)
                print("Task added successfully!")
            except Exception as e:
                print(f"Failed to add task: {e}")

        elif choice == '2':
            tasks = manager.get_all_tasks()
            if not tasks:
                print("No tasks available.")
            for task in tasks:
                print(task)

        elif choice == '3':
            task_id = input("Enter the task ID to delete (e.g., T1): ").strip()
            if manager.delete_task(task_id):
                print("Task deleted successfully!")
            else:
                print("Task not found.")

        elif choice == '4':
            try:
                task_id = int(input("Enter the task ID to update (just the number): "))
                field = input("Which field would you like to update? ").strip()
                value = input("New value: ").strip()
                if field == 'num_people':
                    value = int(value)
                elif field == 'shoot_date':
                    datetime.strptime(value, '%Y-%m-%d')  # validate date format
                manager.update_task(task_id, **{field: value})
                print("Task updated successfully.")
            except Exception as e:
                print(f"Failed to update task: {e}")
                
        elif choice == '5':
            print(f"""
Total active tasks: {manager.count_tasks()[0]}
Total finished tasks: {manager.count_tasks()[1]} 
Total price earned: ${manager.get_total_price()}""")

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid input, please try again.")

if __name__ == '__main__':
    main()