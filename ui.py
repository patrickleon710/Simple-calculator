import tkinter as tk
from math_func import add, subtract, multiply, divide

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("500x500")
        self.root.maxsize(500,500)
        self.inputText = []        


        
        
        self.input = tk.Entry(root, bg="lightblue")
        self.input.pack(side="top", fill="x", padx=10, pady=10)
        

        btnFrame = tk.Frame(root, bg="lightblue")
        btnFrame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        num_buttons = [
            ("9",0,0), ("8", 0, 1), ("7", 0 , 2),
            ("6",1,0), ("5", 1, 1), ("4", 1 , 2),
            ("3",2,0), ("2", 2, 1), ("1", 2 , 2),
            ("0",3,1)
        ]

        for c in range(3):
            btnFrame.columnconfigure(c, weight=1)
        for r in range(4):
            btnFrame.rowconfigure(r, weight=1)

        for text, row,col in num_buttons:
            btn = tk.Button(btnFrame, text=text, command=lambda t=text: self.createText(t))
            btn.grid(row=row, column=col, sticky="nsew", padx=2,pady=2)
       

        signFrame = tk.Frame(root, bg="purple")
        signFrame.pack(side="right", fill="both", expand="true", padx=10, pady=10)

        signs = ["/", "x", "-", "+", "="]
        for r in range(4):
            signFrame.rowconfigure(r, weight=1)

        for i, text in enumerate(signs):
            btn = tk.Button(signFrame, text=text, command=self.evaluate_input if text == "="  else lambda t=text: self.createText(t))
            btn.grid(row=i, column=0, sticky="nsew", padx=2, pady=2)
        
    def createText(self, text):            
            self.input.insert(tk.END,text)
  
## Using python's built-in eval function 
    def evaluate_input(self):
        text = self.input.get()
        self.inputText.append(text)
        print(text)
        print(self.inputText)
        cleaned_text = text.replace("x", "*")

        result = eval(cleaned_text)
        #self.calculate_expression(cleaned_text)

        self.input.delete(0,tk.END)
        self.input.insert(tk.END,result)
        
    def calculate_expression(self, text):
        i = 0
        while i < len(text):
            pass
        pass

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

print(tk.TkVersion)
print(tk.Tcl().eval("info patchlevel"))
