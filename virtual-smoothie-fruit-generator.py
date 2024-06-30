import tkinter as tk
import random

class SmoothieGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Fruit Smoothie Generator")
        
        self.root.configure(bg='lightblue')
        
        self.fruits = ["Banana", "Strawberry", "Mango", "Blueberry", "Kiwi", "Pineapple", "Avocado", "Dragon Fruit","Apple","Lychee"]
        self.bizarre_ingredients = ["Spinach", "Beetroot", "Cucumber", "Ginger", "Cayenne Pepper", "Broccoli", "Garlic", "Turmeric","carrot"]
        
        self.title_label = tk.Label(root, text="Welcome to the Smoothie Generator!", font=("Helvetica", 16), bg='lightgreen')
        self.title_label.pack(pady=20)
        
        self.generate_button = tk.Button(root, text="Generate Smoothie", command=self.generate_smoothie, font=("Helvetica", 14))
        self.generate_button.pack(pady=20)
        
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14), bg='orange')
        self.result_label.pack(pady=20)
        
    def generate_smoothie(self):
        fruit_combination = random.sample(self.fruits, 3)
        bizarre_ingredient = random.choice(self.bizarre_ingredients)
        
        smoothie = f"Try this smoothie: {', '.join(fruit_combination)} with a touch of {bizarre_ingredient}!"
        self.result_label.config(text=smoothie)

if __name__ == "__main__":
    root = tk.Tk()
    app = SmoothieGeneratorApp(root)
    root.mainloop()