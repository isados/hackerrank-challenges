# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
def print_rangoli(size):
    pattern = []
    indices = [x for x in range(size)] + [x for x in range(size-2,-1, -1)]
    letters  = [chr(_+97) for _ in range(size)]
    letters.reverse()
    for index in indices:
        row_pattern = ""
        row_pattern += "-"*(size-1-index)*2
        first_half = letters[:index+1]
        second_half = letters[:index][::-1]
        new_letters = first_half + second_half
        row_pattern += "-".join(new_letters)
        row_pattern += "-"*(size-1-index)*2
        pattern.append(row_pattern)
    print("\n".join(pattern))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
