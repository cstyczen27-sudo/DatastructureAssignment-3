# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None

    def push(self, action):
        new_node = Node(action)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node.action

    def peek(self):
        if self.top:
            return self.top.action
        else:
            return None

def run_undo_redo():
    StackUndo = Stack()
    StackRedo = Stack()
    

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            StackUndo.push(action)


            print(f"Action performed: {action}")
        elif choice == "2":
            StackRedo.push(StackUndo.pop())
            

        elif choice == "3":
             StackUndo.push(StackRedo.pop())


        elif choice == "4":
            print("\nUndo Stack:")
            print(StackUndo.peek())
            

        elif choice == "5":
            print("\nRedo Stack:")
            print(StackRedo.peek())
            
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()