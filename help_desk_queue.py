# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, action):
        new_node = Node(action)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_node.action

    def peek(self):
        if self.front and self.front.next:
            return self.front.next
        else:
            return None

    def print_queue(self):
        current = self.front
        if not current:
            print("Queue is empty")
            return
        while current:
            print(f"- {current.action}")
            current = current.next



def run_help_desk():
    myQue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            myQue.enqueue(name)

            print(f"{name} added to the queue.")
        elif choice == "2":
            helped = myQue.dequeue()
            if helped:
                print(f"Customer {helped} helped")
            else:
                print('No customers to help')
            # Help the next customer in the queue and return message that they were helped



        elif choice == "3":
            next_customer = myQue.peek()
            if next_customer:
                print(f"the next Customer is {next_customer.action}")
            else:
                print('Queue is too short')


        elif choice == "4":
            print("\nWaiting customers:")
            print(myQue.print_queue())

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    run_help_desk()
