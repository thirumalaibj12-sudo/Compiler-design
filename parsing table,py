def compute_first(productions):
    first = {nt: set() for nt in productions}
    changed = True
    while changed:
        changed = False
        for nt, rhs_list in productions.items():
            for rhs in rhs_list:
                i = 0
                while i < len(rhs):
                    if rhs[i] not in productions:  # terminal
                        first[nt].add(rhs[i])
                        break
                    else:  # non-terminal
                        first[nt].update(first[rhs[i]] - {'e'})
                        if 'e' not in first[rhs[i]]:
                            break
                    i += 1
                else:
                    first[nt].add('e')
    return first

def compute_follow(productions, first, start):
    follow = {nt: set() for nt in productions}
    follow[start].add('$')
    changed = True
    while changed:
        changed = False
        for nt, rhs_list in productions.items():
            for rhs in rhs_list:
                for i in range(len(rhs)):
                    if rhs[i] in productions:
                        j = i + 1
                        while j < len(rhs):
                            if rhs[j] not in productions:
                                follow[rhs[i]].add(rhs[j])
                                break
                            else:
                                follow[rhs[i]].update(first[rhs[j]] - {'e'})
                                if 'e' not in first[rhs[j]]:
                                    break
                            j += 1
                        else:
                            follow[rhs[i]].update(follow[nt])
    return follow

def build_table(productions, first, follow):
    table = {}
    for nt, rhs_list in productions.items():
        for rhs in rhs_list:
            first_rhs = set()
            i = 0
            while i < len(rhs):
                if rhs[i] not in productions:
                    first_rhs.add(rhs[i])
                    break
                else:
                    first_rhs.update(first[rhs[i]] - {'e'})
                    if 'e' not in first[rhs[i]]:
                        break
                i += 1
            else:
                first_rhs.update(follow[nt])
            for term in first_rhs:
                table[(nt, term)] = rhs
    return table

if __name__ == "__main__":
    productions = {}
    with open("inputs/input_table.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            nt, rest = line.split(' -> ')
            rhs_list = [rhs.strip().split() for rhs in rest.split('|')]
            productions[nt] = rhs_list
    first = compute_first(productions)
    follow = compute_follow(productions, first, list(productions.keys())[0])
    table = build_table(productions, first, follow)
    with open("outputs/output_table.txt", "w") as f:
        for (nt, term), rhs in table.items():
            f.write(f"M[{nt}, {term}] = {nt} -> {' '.join(rhs)}\n")
    print("Parsing table construction complete. Check outputs/output_table.txt")
