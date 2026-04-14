def run_intermediate():
    print("\n--- PHASE 4: INTERMEDIATE CODE GENERATION ---\n")
    print("Enter statements (type 'exit' to stop)\n")

    temp = 1  

    while True:
        line = input(">> ").strip()
        if line.lower() == "exit":
            break
        if not line:
            continue
        if line.endswith(";"):
            line = line[:-1]
        if "=" in line and "+" in line:
            lhs, rhs = line.split("=", 1)
            lhs = lhs.strip()

            a, b = rhs.split("+", 1)
            a = a.strip()
            b = b.strip()

            print(f"t{temp} = {a} + {b}")
            print(f"{lhs} = t{temp}")
            temp += 1
        elif "=" in line:
            print(line)
        else:
            print("Invalid statement")

    print("\nIntermediate Code Generation Finished.")
if __name__ == "__main__":
    run_intermediate()
