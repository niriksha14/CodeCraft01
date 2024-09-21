# Function to insert element at bottom of stack
def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        top = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(top)

# Function to reverse the stack
def reverse_stack(stack):
    if stack:
        top = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, top)

# Example usage:
stack = [10, 20, 30, 40, 50]
reverse_stack(stack)
print(stack)  # Output should be [5, 4, 3, 2, 1]
