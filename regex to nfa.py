def regex_to_nfa(regex):
    # Simple implementation for a|b
    if '|' in regex:
        parts = regex.split('|')
        if len(parts) == 2:
            a, b = parts
            # States: 0 (start), 1 (for a), 2 (end a), 3 (for b), 4 (end b), 5 (end)
            trans = {
                0: {'e': [1, 3]},
                1: {a: [2]},
                2: {'e': [5]},
                3: {b: [4]},
                4: {'e': [5]}
            }
            return trans, 0, [5]
    # For single
    trans = {0: {regex: [1]}}
    return trans, 0, [1]

if __name__ == "__main__":
    with open("inputs/input_regex.txt", "r") as f:
        regex = f.read().strip()
    trans, start, accept = regex_to_nfa(regex)
    with open("outputs/output_nfa.txt", "w") as f:
        states = max(trans.keys()) + 1
        f.write(f"States: {states}\n")
        f.write(f"Start: {start}\n")
        f.write(f"Accept: {' '.join(map(str, accept))}\n")
        f.write("Transitions:\n")
        for s, d in trans.items():
            for sym, ns in d.items():
                for n in ns:
                    f.write(f"{s} --{sym}--> {n}\n")
    print("Regex to NFA conversion complete. Check outputs/output_nfa.txt")
