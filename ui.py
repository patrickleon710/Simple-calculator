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
            btn = tk.Button(signFrame, text=text, command=self.calculate_expression if text == "="  else lambda t=text: self.createText(t))
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
        
## Using custom function
    def calculate_expression(self):
        
        text = self.input.get()
        cleaned_text = text.replace("x", "*")
        tokens = list(cleaned_text)
        i = 0
        if not tokens:
            return
        print(tokens)
        while i < len(tokens):
            if tokens[i] in ["*", "/"]:
                num1 = float(tokens[i-1])
                operator = tokens[i]
                num2 = float(tokens[i+1])
                if operator == "/":
                    subresult = num1 / num2
                elif operator == "*":
                    subresult = num1 * num2
                tokens[i-1 : i+2] = [str(subresult)]
                i-=1            
            i+=1
        result = float(tokens[0])
        i = 1
        try:
            while i < len(tokens):
                operator = tokens[i]
                next_num = float(tokens[i+1])
                if operator == "+":
                    result += next_num
                elif operator == "-":
                    result -= next_num
                i+=2
        except Exception as e:
            print("Error: ", e)
        print(tokens)
        print(result)
        self.input.delete(0,tk.END)
        self.input.insert(tk.END, str(result))
        

            
        pass

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

print(tk.TkVersion)
print(tk.Tcl().eval("info patchlevel"))
