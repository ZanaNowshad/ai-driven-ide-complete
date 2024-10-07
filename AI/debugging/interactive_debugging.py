
def interactive_debugging():
    code = input("Enter the code snippet to debug: ")
    # Simulate debugging analysis
    if "divide by zero" in code:
        result = "Debugging Result: Potential divide-by-zero error detected. Please handle zero division cases."
    else:
        result = "Debugging Result: No issues found in the code snippet."
    print(result)

if __name__ == "__main__":
    interactive_debugging()
