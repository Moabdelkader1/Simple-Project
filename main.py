print("Hello sic community")

def calc(n1,n2,op):
    if op == "+":
        print(f"{n1} + {n2} = {n1+n2}")
    elif op == "-":
        print(f"{n1} - {n2} = {n1-n2}")
    elif op == "*":
        print(f"{n1} * {n2} = {n1*n2}")
    elif op == "/":
        print(f"{n1} / {n2} = {n1/n2}")
    else:
        print("Invalid operation")
    