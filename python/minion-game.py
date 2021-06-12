def minion_game(string):
    stuart_scores = 0
    kevin_scores = 0
    vowels = ["A", "E", "I", "O", "U"]
    consonants = ['J', 'P', 'V', 'X', 'G', 'Y', 'S', 'N', 'F', 'R', 'Q', 'L', 'M', 'W', 'C', 'Z', 'T', 'B', 'D', 'K', 'H']    
    length = len(string)
    for marker in range(length):
        score = 1*length
        length -= 1
        if string[marker] in consonants:
            stuart_scores += score
        else:
            kevin_scores += score
            
    if kevin_scores > stuart_scores:
        print("Kevin", kevin_scores)
    elif kevin_scores == stuart_scores:
        print("Draw")
    else:
        print("Stuart", stuart_scores)



if __name__ == '__main__':
    s = input()
    minion_game(s)
