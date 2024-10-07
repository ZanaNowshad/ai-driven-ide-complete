
import tkinter as tk
from ..ai_utils import send_request

class VisualProgrammingCanvas:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.blocks = []
        self.canvas.bind("<Button-1>", self.add_block)

    def add_block(self, event):
        block = self.canvas.create_rectangle(event.x, event.y, event.x + 100, event.y + 50, fill="lightblue")
        self.blocks.append(block)
        self.generate_code()

    def generate_code(self):
        messages = [
            {
                "role": "user",
                "content": "Generate Python code based on the current visual blocks."
            }
        ]
        response = send_request(model_key="coding", messages=messages)
        generated_code = response.get("choices", [{}])[0].get("message", {}).get("content", "")
        print("Generated Code:\n", generated_code)

if __name__ == "__main__":
    root = tk.Tk()
    app = VisualProgrammingCanvas(root)
    root.mainloop()
