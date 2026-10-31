
from linked_list import LinkedList


if __name__ == "__main__":

    # 1. Create a LinkedList instance
    employees = LinkedList()

    # 2. Insert sample employee IDs
    employees.insert_at_front(303)
    employees.insert_at_front(202)
    employees.insert_at_front(101)

    # 3. Display the original list
    print("Original Employee Roster:")
    employees.display()

    # 4. Calculate and display the recursive sum
    total = employees.recursive_sum()
    print("\nSum of Employee IDs:", total)

    # 5. Search for an employee ID
    target = 202
    result = employees.recursive_search(target)

    print("\nSearching for Employee ID:", target)

    if result:
        print("Employee ID found!")
    else:
        print("Employee ID not found!")

    # 6. Reverse the linked list
    employees.recursive_reverse()

    print("\nReversed Employee Roster:")
    employees.display()
