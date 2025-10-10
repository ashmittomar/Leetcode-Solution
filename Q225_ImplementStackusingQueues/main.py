from collections import deque

class MyStack(object):

    def __init__(self):
        # Initialize two queues
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        Push element x onto stack.
        """
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        print(f"Pushed {x}")

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.q1:
            print("Stack is empty! Cannot pop.")
            return None
        val = self.q1.popleft()
        print(f"Popped: {val}")
        return val

    def top(self):
        """
        Get the top element.
        """
        if not self.q1:
            print("Stack is empty!")
            return None
        print(f"Top element: {self.q1[0]}")
        return self.q1[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        print("Stack is empty." if not self.q1 else "Stack is not empty.")
        return len(self.q1) == 0


if __name__ == "__main__":
    myStack = MyStack()

    print("Stack Operations Menu:")
    print("1. push <value>")
    print("2. pop")
    print("3. top")
    print("4. empty")
    print("5. exit")

    while True:
        cmd = input("\nEnter command: ").strip().lower()

        if cmd.startswith("push"):
            try:
                val = int(cmd.split()[1])
                myStack.push(val)
            except (IndexError, ValueError):
                print("Usage: push <integer>")
        
        elif cmd == "pop":
            myStack.pop()

        elif cmd == "top":
            myStack.top()

        elif cmd == "empty":
            myStack.empty()

        elif cmd == "exit":
            print("Exiting...")
            break

        else:
            print("Invalid command. Try again.")
