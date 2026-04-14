def remove_left_recursion(productions):
    new_productions = {}
    for nt, rhs_list in productions.items():
        alpha = []
        beta = []
        for rhs in rhs_list:
            if rhs[0] == nt:
                alpha.append(rhs[1:])
            else:
                beta.append(rhs)
        if alpha:
            new_nt = nt + "'"
            new_productions[nt] = [b + [new_nt] for b in beta]
            new_productions[new_nt] = [a + [new_nt] for a in alpha] + [['e']]
        else:
            new_productions[nt] = rhs_list
    return new_productions

if __name__ == "__main__":
    productions = {}
    with open("inputs/input_left.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            nt, rest = line.split(' -> ')
            rhs_list = [rhs.strip().split() for rhs in rest.split('|')]
            productions[nt] = rhs_list
    new_prod = remove_left_recursion(productions)
    with open("outputs/output_left.txt", "w") as f:
        for nt, rhs_list in new_prod.items():
            rhs_str = ' | '.join(' '.join(rhs) for rhs in rhs_list)
            f.write(f"{nt} -> {rhs_str}\n")
    print("Left recursion removal complete. Check outputs/output_left.txt")
