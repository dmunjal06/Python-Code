def generate_permutations(s):
    if len(s) == 1:
        return [s]
    permutations = []
    for i, char in enumerate(s):
        remaining_chars = s[:i] + s[i+1:]
        for p in generate_permutations(remaining_chars):
            permutations.append(char + p)
    return permutations


original_string = input("Original String:")
all_permutations = generate_permutations(original_string)
print("All permutations:")
for p in all_permutations:
    print(p)
