def run_optimization():
    print("\n--- PHASE 5: CODE OPTIMIZATION ---\n")
    print("Enter statements (type 'exit' to stop)\n")

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
            rhs = rhs.strip()

            parts = rhs.split("+")
            if len(parts) == 2:
                a = parts[0].strip()
                b = parts[1].strip()
                if a.isdigit() and b.isdigit():
                    result = int(a) + int(b)
                    print(f"{lhs} = {result}")
                    continue
        if "=" in line:
            lhs, rhs = line.split("=", 1)
            if lhs.strip() == rhs.strip():
                print("Removed redundant assignment:", line)
                continue
        print(line)

    print("\nOptimization Finished.")
if __name__ == "__main__":
    run_optimization()
