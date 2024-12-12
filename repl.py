def repl():
    print("Arbitrary Precision Calculator")
    print("Enter expressions or commands. Type 'exit' to quit")
    while True:
        expr = input("calc> ").strip()
        if expr == 'exit':
            break
        elif expr.startswith("factorial"):
            _, num = expr.split()
            print(BigInt(num).factorial())
        elif expr.startswith("to_base"):
            _, num, base = expr.split()
            print(BigInt(num).to_base(int(base)))
        elif expr.startswith("from_base"):
            _, base, representation = expr.split()
            print(BigInt(0).from_base(int(base), representation))
        else:
            result = eval(expr, {"__builtins__": None}, {
                "BigInt": BigInt,
                "Fraction": Fraction
            })
            print(result)
    except Exception as e:
        print(f"Error:" {e})

