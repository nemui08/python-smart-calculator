import math

history = []
last_result = 0

print("=== Python Smart Calculator ===")
print("Examples:")
print("2+3*5")
print("sqrt(16)+cos(0)")
print("sin(pi/2)")
print("(2+3)*(4+tan(1))")
print("log(100)")
print("ans*100")
print("Type 'history' to see history")
print("Type 'clear' to clear history")
print("Type 'exit' to quit\n")

while True:

    expr = input(">>>")
    
    if expr == "exit":
        print("Goodbye!")
        break

    elif expr == "history":
        print("\n--- History ---")
        
        if len(history) == 0:
            print("No history yet")

        for h in history:
            print(h)
        continue

    elif expr == "clear":
        history.clear()
        print("History cleared")
        continue

    try:
        env = {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "pi": math.pi,
            "ans": last_result
        }

        result = eval(expr,env)
        last_result = result
        
        text = f"{expr} = {result}"
        print(text)

        history.append(text)
    
    except Exception:
        print("Invalid expression")