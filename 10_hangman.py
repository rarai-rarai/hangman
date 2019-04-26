def hangman(word):
    stages=["",
            "__________          ",
            "|                   ",
            "|          |        ",
            "|          0        ",
            "|         |||       ",
            "|          |        ",
            "|         | |       "
            ]

    wrong = 0
    answer = list(word)
    board = ["_"] * len(word)
    win = False
    
    print("Welcome to hangman")
    while wrong < len(stages) - 1:
        char = input("imagine one word" +  format(board) + ":")
        if char in answer:
            board[answer.index(char)] = char
        else:
            wrong += 1

        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you are winner")
            print(" ".join(board))
            win = True
            break
        if not win:
            if e != len(stages):
                print("wrong!!")
            if e == len(stages):
                print("you are looser. answer is {}.".format(word))

hangman("cat")
