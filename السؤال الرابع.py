
def increment_binary(binary_str):
    tape = list(binary_str)
    i = len(tape) - 1
    carry = 1
    while i >= 0 and carry:
        if tape[i] == '0':
            tape[i] = '1'
            carry = 0
        else:
            tape[i] = '0'
            i -= 1
    if carry:
        tape = ['1'] + tape
    return ''.join(tape)

# Example
binary_number = "1111"
result = increment_binary(binary_number)
print("Result:", result)
