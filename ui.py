import tkinter as tk
import re
from math_func import add, subtract, multiply, divide

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("500x500")
        self.root.maxsize(500,500)
        self.history = []        


        

        ## Input field
        self.input = tk.Entry(root, bg="lightblue")
        self.input.pack(side="top", fill="x", padx=10, pady=10)

        topFrame = tk.Frame(root)
        topFrame.pack(side="top", fill="both")
        topFrame.rowconfigure(0, weight=1)

        ## History
        histBtn = tk.Button(topFrame, text="History", bg="Orange", width=20, command=self.show_history)
        histBtn.grid(column=0, row=0, padx=10, pady=10)

        ## Close
        closeBtn = tk.Button(topFrame, text="Exit", bg="Red", width=10, command=root.destroy)
        closeBtn.grid(column=1, row=0, padx=10, pady=10)
        
        ## Numbers
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
       
        ## Signs
        signFrame = tk.Frame(root, bg="purple")
        signFrame.pack(side="right", fill="both", expand="true", padx=10, pady=10)

        signs = [" / ", " x ", " - ", " + ", "<", "C", "="]
        for r in range(len(signs)):
            signFrame.rowconfigure(r, weight=1)

        for i, text in enumerate(signs):
            
            if text == "=":
                cmd = self.shunting_Yard
            elif text == "<":
                cmd = lambda t=text: self.deleteText(t)
            elif text == "C":
                cmd = lambda t=text: self.deleteText(t)
            else:
                cmd = lambda t=text: self.createText(t)
            btn = tk.Button(signFrame, text=text, command=cmd)
            btn.grid(row=i, column=0, sticky="nsew", padx=2, pady=2)

        

    ## Translates button clicks into text in the input field
    def createText(self, text):            
            self.input.insert(tk.END,text)
    
    ## Deletes last character or whole text
    def deleteText(self, text):
        if text == "C":
            self.input.delete(0, tk.END)
        elif text == "<":
            current_input = self.input.get()
            if current_input:
                self.input.delete(len(current_input)-1, tk.END)

    ## Records last five calculations
    def show_history(self):
        
        # Create a new window on top of the main one
        history_window = tk.Toplevel()
        history_window.title("History")
        history_window.geometry("500x400")
        history_window.maxsize(500,400) # Adjust size as needed
        
        # Title label for the new window
        tk.Label(history_window, text="Last 5 Calculations", font=("Helvetica", 10, "bold")).pack(pady=10)

        # Button to close window
        tk.Button(history_window, text="Close", font=("Helvetica", 10, "bold", ), command=history_window.destroy, bg="red").pack(padx=5,pady=5)
        
        # Check if there is history to show
        if not self.history:
            tk.Label(history_window, text="No history yet.").pack(pady=5)
        else:
            # Loop through the list and create a label for each calculation
            for item in self.history:
                tk.Label(history_window, text=item, font=("Helvetica", 12)).pack(pady=2)

                
    ## Using python's built-in eval function 
    def evaluate_input(self):
        text = self.input.get()
        
        cleaned_text = text.replace("x", "*")

        result = eval(cleaned_text)
        #self.calculate_expression(cleaned_text)

        self.input.delete(0,tk.END)
        self.input.insert(tk.END,result)
        
    ## Using custom function - works if there are spaces between numbers and spaces
    def calculate_expression(self):
        
        text = self.input.get()
        cleaned_text = text.replace("x ", "* ")
        tokens = list(cleaned_text) # with no spaces
        expr_tok = cleaned_text.split() # with spaces
        i = 0
        if not expr_tok:
            return
        
        while i < len(expr_tok):
            if expr_tok[i] in ["*", "/"]:
                num1 = float(expr_tok[i-1])
                operator = expr_tok[i]
                num2 = float(expr_tok[i+1])
                if operator == "/":
                    subresult = num1 / num2
                elif operator == "*":
                    subresult = num1 * num2
                expr_tok[i-1 : i+2] = [str(subresult)]
                i-=1            
            i+=1
        result = float(expr_tok[0])
        i = 1
        try:
            while i < len(expr_tok):
                operator = expr_tok[i]
                next_num = float(expr_tok[i+1])
                if operator == "+":
                    result += next_num
                elif operator == "-":
                    result -= next_num
                i+=2
        except Exception as e:
            print("Error: ", e)
        
        self.input.delete(0,tk.END)
        self.input.insert(tk.END, str(result))

    ## Modified function to use regex
    def calculate_expression_mod(self):
        try:
            text = self.input.get()
            cleaned_text = text.replace("x", "*")
            tokens = re.findall(r"\d+\.\d+|\d+|[+\-*/]", cleaned_text)
            i = 0
            if not tokens:
                return
            
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
        
            while i < len(tokens):
                operator = tokens[i]
                next_num = float(tokens[i+1])
                if operator == "+":
                    result += next_num
                elif operator == "-":
                    result -= next_num
                i+=2

            self.input.delete(0,tk.END)
            self.input.insert(tk.END, str(result))

            history_entry = f"{text} = {result}"
            self.history.append(history_entry)
        except Exception as e:
            self.input.delete(0, tk.END)
            self.input.insert(tk.END, "Error")

        

    ## Shunting-Yard algorithm
    def infix_to_postfix(self, tokens):
        precedence = {"+":1, "-":1, "*":2, "/":2}
        output = []
        operators = []
        if not tokens:
            return

        for token in tokens:
            if token in precedence:                    
                while (operators and operators[-1] in precedence and precedence[operators[-1]] >= precedence[token]):
                    output.append(operators.pop())
                operators.append(token)
            else:
                output.append(token)
        
        while operators:
            output.append(operators.pop())

        return output

    def evaluate_postfix(self, postfix):
        stack = []

        for token in postfix:
            if token in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()

                if token == "+": stack.append(a + b)
                elif token == "-": stack.append(a - b)
                elif token == "*": stack.append(a * b)
                elif token == "/":
                    if b == 0:
                        raise ValueError("Division by zero")
                    stack.append(a / b)
            else:
                stack.append(float(token))
        
        result = stack[0]

        return int(result) if result.is_integer() else result

    def shunting_Yard(self):
        try:
            text = self.input.get()
            cleaned_text = text.replace("x", "*")
            tokens = re.findall(r"\d+\.\d+|\d+|[+\-*/]", cleaned_text)
            i = 0
            if not tokens:
                return
            
            postfix = self.infix_to_postfix(tokens)
            result = self.evaluate_postfix(postfix)

            self.input.delete(0,tk.END)
            self.input.insert(tk.END, str(result))

            history_entry = f"{text} = {result}"
            self.history.append(history_entry)
            if len(self.history) > 5:
                self.history.pop(0)
        except ValueError as ve:
            self.input.delete(0, tk.END)
            self.input.insert(tk.END, "Math Error")
        except Exception as e:
            self.input.delete(0, tk.END)
            self.input.insert(tk.END, "Syntax Error")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

""" print(tk.TkVersion)
print(tk.Tcl().eval("info patchlevel")) """
