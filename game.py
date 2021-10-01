from player import HumanPlayer, RandomComputerPlayer
import time

# Creating a board
class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)] # Create a 3 x 3 board
        self.current_winner = None # keep track of winner.

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc(tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


    # 다음으로 이동 가능한 위치 확인
    def available_move(self):
        # return = [] # 인덱스들의 리스트 리턴.
        # return [i for i, spot in enumerate(self.board) if spot == ' ']
        moves = []
        for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)
        return moves
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')


    # when we make a move, 
    # we need information about 
    # 1. what square the user wants their move to be at
    # 2. what letter the player is
    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid, return false
        if self.board[square] == ' ': # if self.board[square] is empty,
            self.board[square] = letter # At that space on the board nothing's there yet.
            if self.winner(square, letter):
                self.current_winner = letter
            return True
            # then we assign that letter to that given square, and return true.
        return False 

    # checking the winner
    def winner(self, square, letter):
        # In TicTacToe, the winner if 3 in a row anywhere
        # we have to check all of these
        # 1. in the row
        # 2. column
        # 3. diagonal

        # first, let's check the row.
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in row]):
            return True

        # check diagonals it's only even number 02468
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        # if all of these fail
        return False

def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game(the letter)! or None for a tie
    


    # If print_game is true, it'll print out all the steps.
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # statring letter
    # iterate while the game still has empty squares
    
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # let's define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}') 
                game.print_board()
                print('') # just empty line

            if game.current_winner: # if the current winner var is not set to None anymore, then a letter has one.
                if print_game:
                    print(letter + ' wins!')
                return letter

            # after we made our move, we need to alternate letters(switches player)
            # letter = 'O' if letter == 'X' else 'X'
            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'
            
        # tiny break to make things a little easier to read
        time.sleep(0.8)

    if print_game: # after this while loop is over, we can just print, it's a tie
        print('It\'s a tie!')


x_player = HumanPlayer('X')
o_player = RandomComputerPlayer('O')
t = TicTacToe()
play(t, x_player, o_player, print_game=True)






# print([' ' for _ in range(9)])
# board = [' ' for _ in range(9)]
# for row in [board[i*3:(i+1)*3] for i in range(3)]:
#     # print(row)
#     # print('| ' + ' | '.join(row) + ' |')
#     print(' | f'.join(row))

# number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
# # print(number_board)
# for row in number_board:
#     print('| ' + ' | '.join(row) + ' |')
