"""
Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.
If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]

where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. 
Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
"""

def check_winner(p1, p2):
    if p1 == 3:
        return 1
    elif p2 == 6:
        return 2
    else:
        return 0


def check_board(arr):
    if not isinstance(arr[0], list):
        print("Please call function with 2D list")
        return

    scores_p1, scores_p2, diag_p1, diag_p2 = [], [], 0, 0

    # Check rows
    for i in range(len(arr)):
        row_p1, col_p1, row_p2, col_p2 = 0, 0, 0, 0
        for j in range(len(arr[i])):
            # Check rows
            if arr[i][j] == 1:
                row_p1 += 1
            elif arr[i][j] == 2:
                row_p2 += 2
            else:
                pass

            #Check cols
            if arr[j][i] == 1:
                col_p1 += 1
            elif arr[j][i] == 2:
                col_p2 += 2
            else:
                pass

            #Check left diag
            if i == j:
                if arr[i][j] == 1:
                    diag_p1 += 1
                elif arr[i][j] == 2:
                    diag_p2 += 2
                else:
                    pass                

        scores_p1.append(row_p1)
        scores_p1.append(col_p1)

        scores_p2.append(row_p2)
        scores_p2.append(col_p2)

    scores_p1.append(diag_p1)
    scores_p2.append(diag_p2)

    # Check right diag
    rdiag_p1, rdiag_p2 = 0, 0
    for i in range(len(arr)):
        for j in range(len(arr[i]), -1, -1):
            if i == j:
                if arr[i][j] == 1:
                    rdiag_p1 += 1
                elif arr[i][j] == 2:
                    rdiag_p2 += 2
                else:
                    pass   
    scores_p1.append(rdiag_p1)
    scores_p2.append(rdiag_p2)

    # Debug: checking scores
    # print(scores_p1, scores_p2)

    # Check for winner
    if 3 in scores_p1:
        return 1
    elif 6 in scores_p2:
        return 2
    else:
        return 0

    # Check cols
    # for i in len(arr):
    # win_p1, win_p2 = 0, 0
    # for j in len(arr[i]):
    #     if arr[j][i] == 1:
    #         win_p1 += 1
    #     elif arr[j][i] == 2:
    #         win_p2 += 2
    #     else:
    #         pass
    # scores_p1.append(win_p1)
    # scores_p2.append(win_p2)


if __name__ == "__main__":

    winner_is_2 = [
        [2, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

    winner_is_1 = [
        [1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

    winner_is_also_1 = [
        [0, 1, 0],
        [2, 1, 0],
        [2, 1, 1]]

    no_winner = [
        [1, 2, 0],
        [2, 1, 0],
        [2, 1, 2]]

    also_no_winner = [
        [1, 2, 0],
        [2, 1, 0],
        [2, 1, 0]]

    print(check_board(winner_is_1))
    print(check_board(winner_is_2))
    print(check_board(winner_is_also_1))
    print(check_board(no_winner))
    print(check_board(also_no_winner))


