import ast

class PythonLearningTool:
    def __init__(self):
        self.examples = {
            'variables': self.variable_example,
            'control structures': self.control_structure_example,
            'functions': self.function_example,
            'lists': self.list_example,
            'loops': self.loop_example,
            'dictionaries': self.dictionary_example,
            'exception handling': self.exception_handling_example,
        }

    def show_examples(self):
        print("Available topics:")
        for topic in self.examples.keys():
            print(f"- {topic}")
        print("\nWhich topic would you like to see?")

    def variable_example(self):
        return """
# Variable Assignment
x = 5
y = "Hello"
print(x)
print(y)
"""

    def control_structure_example(self):
        return """
# Control Structures
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
"""

    def function_example(self):
        return """
# Function Definition
def add(a, b):
    return a + b

result = add(3, 4)
print(result)
"""

    def list_example(self):
        return """
# List Usage
fruits = ["apple", "banana", "strawberry"]
for fruit in fruits:
    print(fruit)
"""

    def loop_example(self):
        return """
# Loops
for i in range(5):
    print(i)
"""

    def dictionary_example(self):
        return """
# Dictionary Usage
person = {"name": "Alice", "age": 30}
print(person["name"])
"""

    def exception_handling_example(self):
        return """
# Exception Handling
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
"""

    def get_example(self, topic):
        return self.examples.get(topic.lower(), lambda: "Topic not found.")()

    def compare_code(self, user_code, example_code):
        user_lines = user_code.strip().splitlines()
        example_lines = example_code.strip().splitlines()
        has_error = False

        for i, line in enumerate(example_lines):
            if i < len(user_lines):
                if line.strip() != user_lines[i].strip():
                    print(f"Error on line {i + 1}: expected: '{line.strip()}', but you wrote: '{user_lines[i].strip()}'")
                    has_error = True
            else:
                print(f"Error: line {i + 1} is missing.")
                has_error = True

        if len(user_lines) > len(example_lines):
            extra = len(user_lines) - len(example_lines)
            print(f"Error: You have {extra} extra line(s).")
            has_error = True

        if not has_error:
            print("✅ Your code matches the example!")

# ---- User Interaction ----

if __name__ == "__main__":
    tool = PythonLearningTool()
    tool.show_examples()

    topic = input("Enter your topic choice: ").strip().lower()
    example_code = tool.get_example(topic)

    if example_code == "Topic not found.":
        print("❌ Invalid topic. Please restart and choose a valid one.")
    else:
        print("\nExample code for the selected topic:\n")
        print(example_code)

        print("\nNow write your own code for comparison.")
        print("Finish your input with 'CTRL+D' (Unix/Linux/Mac) or 'CTRL+Z' (Windows) and press Enter.\n")

        try:
            user_input = ""
            while True:
                line = input()
                user_input += line + "\n"
        except EOFError:
            pass

        tool.compare_code(user_input, example_code)
