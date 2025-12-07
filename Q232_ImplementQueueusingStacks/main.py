class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self.move_in_to_out()
        return self.out_stack.pop()

    def peek(self):
        self.move_in_to_out()
        return self._stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

    def move_in_to_out(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


if __name__ == "__main__":
    q = MyQueue()
    n = int(input("Enter number of operations: "))
    print("Enter operations in format: push x / pop / peek / empty")

    for _ in range(n):
        op = input().strip().split()

        if op[0] == "push":
            x = int(op[1])
            q.push(x)
            print(f"Pushed {x}")

        elif op[0] == "pop":
            if not q.empty():
                print("Popped:", q.pop())
            else:
                print("Queue is empty!")

        elif op[0] == "peek":
            if not q.empty():
                print("Front element:", q.peek())
            else:
                print("Queue is empty!")

        elif op[0] == "empty":
            print("Is queue empty?", q.empty())

        else:
            print("Invalid operation!")
