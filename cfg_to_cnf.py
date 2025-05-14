
def convert_to_cnf(cfg):
    variables, terminals, productions, start = cfg
    cnf_productions = []
    for head, bodies in productions.items():
        for body in bodies:
            if len(body) == 1 and body[0] in terminals:
                cnf_productions.append((head, body))
            elif len(body) > 2:
                while len(body) > 2:
                    new_var = "X" + str(len(cnf_productions))
                    cnf_productions.append((new_var, [body[0], body[1]]))
                    body = [new_var] + body[2:]
                cnf_productions.append((head, body))
            else:
                cnf_productions.append((head, body))
    return cnf_productions

# Example CFG
cfg = (
    {"S", "A", "B"},
    {"a", "b"},
    {
        "S": [["A", "B"], ["B"]],
        "A": [["a"]],
        "B": [["b"]]
    },
    "S"
)

print("CNF Productions:", convert_to_cnf(cfg))
