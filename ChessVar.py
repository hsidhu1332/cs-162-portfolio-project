# Author: Harpaul Sidhu
# GitHub username: hsidhu1332
# Date: 12/8/2023
# Description: # Creating a chess match using chess piece objects and a class
#                to keep score. The board is initialized using a dictionary and
#                is then filled with objects based on each chess piece. Each
#                piece inherits a base chess piece class that has basic properties
#                such as name and color. Each class has a valid move method that
#                determines if the move is valid for the piece and returns true or
#                false which allows the ChessVar class to either make the move or not.
#                The game state is checked based on if any chess piece of a type is
#                present and if not changes the game state variable.

class ChessVar:
    """
    Class is going to initialize the game, keep track of moves and location of pieces
    It will also track who has won the game or if it is ongoing.
    """

    def __init__(self):
        self._final_yInt = None
        self._final_xInt = None
        self._initial_yInt = None
        self._initial_xInt = None
        self._board = None
        self._game_state = 'UNFINISHED'
        self._turn = 'white'
        self.initialize_board()

    def initialize_board(self):
        """
        Initializes the board to a dictionary and fills out the 8x8
        grid with None before creating the default positions for
        every piece
        """
        self._board = {}
        x_axis = 'abcdefgh'
        y_axis = '12345678'

        # fill the board with coordinate keys and None values
        for x in x_axis:
            for y in y_axis:
                self._board[x + y] = None

        # fill the 2 and 7th row with pawns
        for x in x_axis:
            self._board[x + '2'] = Pawn('white')
            self._board[x + '7'] = Pawn('black')

        # initialize the rest of the pieces
        self._board['a1'] = self._board['h1'] = Rook('white')
        self._board['a8'] = self._board['h8'] = Rook('black')
        self._board['b1'] = self._board['g1'] = Knight('white')
        self._board['b8'] = self._board['g8'] = Knight('black')
        self._board['c1'] = self._board['f1'] = Bishop('white')
        self._board['c8'] = self._board['f8'] = Bishop('black')
        self._board['d1'] = Queen('white')
        self._board['d8'] = Queen('black')
        self._board['e1'] = King('white')
        self._board['e8'] = King('black')

    def get_game_state(self):
        """
        Return the game state
        """
        return self._game_state

    def update_game_state(self):
        """
        Check if the game is completed by constantly checking if each of the
        piece's quantity is removed based on their color. Updates game_state
        depending on the color missing
        """
        # check if there is any instance of a piece and its color, sets the
        # game state to the opposite color if it returns false
        white_pawn_check = any(isinstance(piece, Pawn) and piece.get_color() == 'white'
                               for piece in self._board.values())
        if white_pawn_check is False:
            self._game_state = 'BLACK_WON'

        black_pawn_check = any(isinstance(piece, Pawn) and piece.get_color() == 'black'
                               for piece in self._board.values())
        if black_pawn_check is False:
            self._game_state = 'WHITE_WON'

        white_rook_check = any(isinstance(piece, Rook) and piece.get_color() == 'white'
                               for piece in self._board.values())
        if white_rook_check is False:
            self._game_state = 'BLACK_WON'

        black_rook_check = any(isinstance(piece, Rook) and piece.get_color() == 'black'
                               for piece in self._board.values())
        if black_rook_check is False:
            self._game_state = 'WHITE_WON'

        white_knight_check = any(isinstance(piece, Knight) and piece.get_color() == 'white'
                               for piece in self._board.values())
        if white_knight_check is False:
            self._game_state = 'BLACK_WON'

        black_knight_check = any(isinstance(piece, Knight) and piece.get_color() == 'black'
                               for piece in self._board.values())
        if black_knight_check is False:
            self._game_state = 'WHITE_WON'

        white_bishop_check = any(isinstance(piece, Bishop) and piece.get_color() == 'white'
                               for piece in self._board.values())
        if white_bishop_check is False:
            self._game_state = 'BLACK_WON'

        black_bishop_check = any(isinstance(piece, Bishop) and piece.get_color() == 'black'
                               for piece in self._board.values())
        if black_bishop_check is False:
            self._game_state = 'WHITE_WON'

        white_queen_check = any(isinstance(piece, Queen) and piece.get_color() == 'white'
                               for piece in self._board.values())
        if white_queen_check is False:
            self._game_state = 'BLACK_WON'

        black_queen_check = any(isinstance(piece, Queen) and piece.get_color() == 'black'
                               for piece in self._board.values())
        if black_queen_check is False:
            self._game_state = 'WHITE_WON'

        white_king_check = any(isinstance(piece, King) and piece.get_color() == 'white'
                               for piece in self._board.values())
        if white_king_check is False:
            self._game_state = 'BLACK_WON'

        black_king_check = any(isinstance(piece, King) and piece.get_color() == 'black'
                               for piece in self._board.values())
        if black_king_check is False:
            self._game_state = 'WHITE_WON'

    def make_move(self, initial_spot, final_spot):
        """
        Take the spots and get the dictionary object associated with the initial spot.
        Use the object properties to check if it would be valid move
        by comparing the turn counter to the color property of the object
        being moved. Also checks if the final spot contains an object
        of the same color, if the game is over, or if the move
        would take the piece "out of bounds". Then checks if the move
        is valid based on the object. If the move is valid,
        move the object from its current spot to the final spot.
        """

        if self._game_state != 'UNFINISHED':
            return False

        bounds = self.check_bounds(initial_spot, final_spot)

        if bounds:
            return False

        # if there is a piece at the final spot check if it's the same color
        if self._board[final_spot] is not None:
            if self._board[final_spot].get_color() == self._board[initial_spot].get_color():
                return False

        if self._board[initial_spot] is None:
            return False

        if self._turn == self._board[initial_spot].get_color():
            result = self._board[initial_spot].valid_move(initial_spot, final_spot, self._board)
            # if the move is valid, update the board and check if the game is over
            if result:
                if self._turn == 'white':
                    self._turn = 'black'
                else:
                    self._turn = 'white'
                self._board[final_spot] = self._board[initial_spot]
                self._board[initial_spot] = None
                self.update_game_state()
                return result
            else:
                return result
        else:
            return False

    def check_bounds(self, initial_spot, final_spot):
        """
        Checks if the move being made would take the piece off the
        board
        """
        self._initial_xInt = ord(initial_spot[0]) - ord('a') + 1
        self._initial_yInt = int(initial_spot[1])
        self._final_xInt = ord(final_spot[0]) - ord('a') + 1
        self._final_yInt = int(final_spot[1])
        # checks if the piece is on the 8x8 grid
        if (0 < self._initial_xInt < 9 and 0 < self._initial_yInt < 9 and
                0 < self._final_xInt < 9 and 0 < self._final_yInt < 9):
            return False
        else:
            return True


class ChessPiece():
    """
    A class representing a chess piece object. Will be
    inherited by each piece Sets the name and color as well as
    getting the integer coordinates of the piece.
    """

    def __init__(self, name, color):
        self._name = name
        self._color = color
        self._initial_xInt = None
        self._initial_yInt = None
        self._final_xInt = None
        self._final_yInt = None

    def get_name(self):
        """
        Returns the name of the chess piece
        """
        return self._name

    def get_color(self):
        """
        Returns the color of the piece
        """
        return self._color

    def valid_move(self, initial_spot, final_spot, board):
        """
        Converts the spot, ex a1, to two integers, ex 1 and 1.
        """
        # converts the letters to numbers 1-8 and splits the second number
        self._initial_xInt = ord(initial_spot[0]) - ord('a') + 1
        self._initial_yInt = int(initial_spot[1])
        self._final_xInt = ord(final_spot[0]) - ord('a') + 1
        self._final_yInt = int(final_spot[1])

    def num_to_letter(self, coord):
        """
        Converts the x integer back to a letter for
        any dictionary check
        """
        return chr(ord('a') + coord - 1)


class Pawn(ChessPiece):
    """
    A class representing a pawn. Will inherit the chess piece class.
    Will be unique in checking if this is the first move and if it can
    move two spots
    """

    def __init__(self, color):
        super().__init__(name='pawn', color=color)
        self._first_move = True

    def valid_move(self, initial_spot, final_spot, board):
        """
        First check if it's the first move for this pawn, if so
        allow for two moves up otherwise return false. Once,
        the first move is checked, change it to false.
        If the final_spot object is none, don't allow for
        diagonal movement for a pawn.
        """
        super().valid_move(initial_spot, final_spot, board)

        # moves up for white pieces
        if board[initial_spot].get_color() == 'white':
            # allows for two spot movement if the first move has not occurred
            if self._first_move:
                self._first_move = False
                if self._initial_xInt == self._final_xInt:
                    if (self._initial_yInt + 1 == self._final_yInt
                            and board[final_spot] is None):
                        return True
                    elif self._initial_yInt + 2 == self._final_yInt:
                        if (board[self.num_to_letter(self._initial_xInt) +
                                str(self._initial_yInt + 1)] is None):
                            if board[final_spot] is None:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                if self._initial_xInt == self._final_xInt:
                    if (self._initial_yInt + 1 == self._final_yInt
                            and board[final_spot] is None):
                        return True
                    else:
                        return False
                # check if a piece is to be captured and check for diagonal movement
                elif board[final_spot] is not None:
                    if (self._initial_xInt + 1 == self._final_xInt
                            and self._initial_yInt + 1 == self._final_yInt):
                        return True
                    elif (self._initial_xInt - 1 == self._final_xInt
                            and self._initial_yInt + 1 == self._final_yInt):
                        return True
                    else:
                        return False
                else:
                    return False
        # if the piece is black, it can only move down
        # same logic as white, just subtracting one/two now
        else:
            if self._first_move:
                self._first_move = False
                if self._initial_xInt == self._final_xInt:
                    if (self._initial_yInt - 1 == self._final_yInt
                            and board[final_spot] is None):
                        return True
                    elif self._initial_yInt - 2 == self._final_yInt:
                        if (board[self.num_to_letter(self._initial_xInt) +
                                str(self._initial_yInt - 1)] is None):
                            if board[final_spot] is None:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                if self._initial_xInt == self._final_xInt:
                    if (self._initial_yInt - 1 == self._final_yInt
                            and board[final_spot] is None):
                        return True
                    else:
                        return False
                elif board[final_spot] is not None:
                    if (self._initial_xInt - 1 == self._final_xInt
                            and self._initial_yInt - 1 == self._final_yInt):
                        return True
                    elif (self._initial_xInt + 1 == self._final_xInt
                            and self._initial_yInt - 1 == self._final_yInt):
                        return True
                    else:
                        return False
                else:
                    return False


class Rook(ChessPiece):
    """
    A class representing a rook. Will inherit the chess piece class.
    """

    def __init__(self, color):
        super().__init__(name='rook', color=color)

    def valid_move(self, initial_spot, final_spot, board):
        """
        Check if the rook is completing a valid move based on if either the
        x axis or y axis is not changing between the final and initial spot.
        Constantly checks if an object is in front of it as it moves to
        its final spot.
        """
        super().valid_move(initial_spot, final_spot, board)

        # check if the x axis stays the same
        if self._initial_xInt == self._final_xInt:
            # check if the object is moving right
            if self._final_yInt > self._initial_yInt:
                while self._initial_yInt != self._final_yInt:
                    # check if an object is present in the next spot
                    # if so, return true only if it's the final spot
                    if (board[self.num_to_letter(self._initial_xInt) + str(self._initial_yInt + 1)]
                            is not None):
                        if (final_spot ==
                                self.num_to_letter(self._initial_xInt) + str(self._initial_yInt + 1)):
                            return True
                        else:
                            return False
                    else:
                        self._initial_yInt += 1
                return True
            # check if the object is moving left
            if self._final_yInt < self._initial_yInt:
                while self._initial_yInt != self._final_yInt:
                    if (board[self.num_to_letter(self._initial_xInt) + str(self._initial_yInt - 1)]
                            is not None):
                        if (final_spot ==
                                self.num_to_letter(self._initial_xInt) + str(self._initial_yInt - 1)):
                            return True
                        else:
                            return False
                    else:
                        self._initial_yInt -= 1
                return True
        # check if the y axis stays the same
        # same logic as the x axis, just updating the y int now
        elif self._initial_yInt == self._final_yInt:
            if self._final_xInt > self._initial_xInt:
                while self._initial_xInt != self._final_xInt:
                    if (board[self.num_to_letter(self._initial_xInt + 1) + str(self._initial_yInt)]
                            is not None):
                        if (final_spot ==
                                self.num_to_letter(self._initial_xInt + 1) + str(self._initial_yInt)):
                            return True
                        else:
                            return False
                    else:
                        self._initial_xInt += 1
                return True
            if self._final_xInt < self._initial_xInt:
                while self._initial_xInt != self._final_xInt:
                    if (board[self.num_to_letter(self._initial_xInt - 1) + str(self._initial_yInt)]
                            is not None):
                        if (final_spot ==
                                self.num_to_letter(self._initial_xInt - 1) + str(self._initial_yInt)):
                            return True
                        else:
                            return False
                    else:
                        self._initial_xInt -= 1
                return True
        # if both the x and y are changing, then it is not a valid move for a rook
        else:
            return False


class Knight(ChessPiece):
    """
    A class representing a knight. Will inherit the chess piece class.
    """

    def __init__(self, color):
        super().__init__(name='knight', color=color)

    def valid_move(self, initial_spot, final_spot, board):
        """
        Check if the knight is doing a legal move by checking how much each
        grid value increases by. Ex. If letter increases by 2, num increases by
        1.
        """
        super().valid_move(initial_spot, final_spot, board)

        # checks every scenario a knight can move
        if (self._initial_xInt + 2 == self._final_xInt and
                self._initial_yInt + 1 == self._final_yInt):
            return True
        elif (self._initial_xInt + 2 == self._final_xInt and
                self._initial_yInt - 1 == self._final_yInt):
            return True
        elif (self._initial_xInt - 2 == self._final_xInt and
                self._initial_yInt + 1 == self._final_yInt):
            return True
        elif (self._initial_xInt - 2 == self._final_xInt and
                self._initial_yInt - 1 == self._final_yInt):
            return True
        elif (self._initial_xInt + 1 == self._final_xInt and
                self._initial_yInt + 2 == self._final_yInt):
            return True
        elif (self._initial_xInt + 1 == self._final_xInt and
                self._initial_yInt - 2 == self._final_yInt):
            return True
        elif (self._initial_xInt - 1 == self._final_xInt and
                self._initial_yInt + 2 == self._final_yInt):
            return True
        elif (self._initial_xInt - 1 == self._final_xInt and
                self._initial_yInt - 2 == self._final_yInt):
            return True
        else:
            return False


class Bishop(ChessPiece):
    """
    A class representing a bishop. Will inherit the chess piece class.
    """

    def __init__(self, color):
        super().__init__(name='bishop', color=color)

    def valid_move(self, initial_spot, final_spot, board):
        """
        Check if the bishop is doing a valid move by seeing if it
        is going diagonal in either direction by seeing if each
        increments by 1 or decreases by 1. Constantly checks if
        an object is in front of it as it moves to its final spot.
        """
        super().valid_move(initial_spot, final_spot, board)
        # checks for if the piece is going up and to the right
        # same logic for each other direction
        if (self._initial_xInt < self._final_xInt and
                self._initial_yInt < self._final_yInt):
            while (self._initial_xInt != self._final_xInt and
                    self._initial_yInt != self._final_yInt):
                # similar to rook, check if there is an object in front of it
                # as it moves, if not the final spot, return false
                if (board[self.num_to_letter(self._initial_xInt + 1) + str(self._initial_yInt + 1)]
                        is not None):
                    if (final_spot ==
                            self.num_to_letter(self._initial_xInt + 1) + str(self._initial_yInt + 1)):
                        return True
                    else:
                        return False
                # if the final spot is completely diagonal, return true
                elif (final_spot ==
                            self.num_to_letter(self._initial_xInt + 1) + str(self._initial_yInt + 1)):
                    return True
                else:
                    self._initial_xInt += 1
                    self._initial_yInt += 1
            # returns false if it gets past the final spot meaning it was not diagonal
            return False
        # checks if the piece is going up and to the left
        elif (self._initial_xInt > self._final_xInt and
                self._initial_yInt < self._final_yInt):
            while (self._initial_xInt != self._final_xInt and
                    self._initial_yInt != self._final_yInt):
                if (board[self.num_to_letter(self._initial_xInt - 1) + str(self._initial_yInt + 1)]
                        is not None):
                    if (final_spot ==
                            self.num_to_letter(self._initial_xInt - 1) + str(self._initial_yInt + 1)):
                        return True
                    else:
                        return False
                elif (final_spot ==
                            self.num_to_letter(self._initial_xInt - 1) + str(self._initial_yInt + 1)):
                    return True
                else:
                    self._initial_xInt -= 1
                    self._initial_yInt += 1
            return False
        # checks if the piece is going down and to the right
        elif (self._initial_xInt < self._final_xInt and
                self._initial_yInt > self._final_yInt):
            while (self._initial_xInt != self._final_xInt and
                    self._initial_yInt != self._final_yInt):
                if (board[self.num_to_letter(self._initial_xInt + 1) + str(self._initial_yInt - 1)]
                        is not None):
                    if (final_spot ==
                            self.num_to_letter(self._initial_xInt + 1) + str(self._initial_yInt - 1)):
                        return True
                    else:
                        return False
                elif (final_spot ==
                            self.num_to_letter(self._initial_xInt + 1) + str(self._initial_yInt - 1)):
                    return True
                else:
                    self._initial_xInt += 1
                    self._initial_yInt -= 1
            return False
        # checks if the piece is going down and to the left
        elif (self._initial_xInt > self._final_xInt and
                self._initial_yInt > self._final_yInt):
            while (self._initial_xInt != self._final_xInt and
                    self._initial_yInt != self._final_yInt):
                if (board[self.num_to_letter(self._initial_xInt - 1) + str(self._initial_yInt - 1)]
                        is not None):
                    if (final_spot ==
                            self.num_to_letter(self._initial_xInt - 1) + str(self._initial_yInt - 1)):
                        return True
                    else:
                        return False
                elif (final_spot ==
                            self.num_to_letter(self._initial_xInt - 1) + str(self._initial_yInt - 1)):
                    return True
                else:
                    self._initial_xInt -= 1
                    self._initial_yInt -= 1
            return False
        # if it is not doing any of these then it is not valid for a bishop
        else:
            return False


class Queen(ChessPiece):
    """
    A class representing a queen. Will inherit the chess piece class.
    """

    def __init__(self, color):
        super().__init__(name='queen', color=color)

    def valid_move(self, initial_spot, final_spot, board):
        """
        Check if the queen is doing a valid move by going diagonal
        or going forward by inheriting the move check methods of bishop
        and rook. If either return true, then the method returns true.
        """
        # creates two objects for a rook and bishop and uses their valid move checks
        check_rook = Rook(self._color)
        check_bishop = Bishop(self._color)

        if (check_rook.valid_move(initial_spot, final_spot, board) or
                check_bishop.valid_move(initial_spot, final_spot, board)):
            return True
        else:
            return False


class King(ChessPiece):
    """
    A class representing a king. Will inherit the chess piece class.
    """

    def __init__(self, color):
        super().__init__(name='king', color=color)

    def valid_move(self, initial_spot, final_spot, board):
        """
        Check if the king is doing valid move by checking if a king
        is moving within one spot of its initial spot.
        """
        super().valid_move(initial_spot, final_spot, board)

        # checks every valid move for a king, otherwise returns false
        if (self._initial_xInt - 1 == self._final_xInt and
                self._initial_yInt == self._final_yInt):
            return True
        elif (self._initial_xInt - 1 == self._final_xInt and
                self._initial_yInt + 1 == self._final_yInt):
            return True
        elif (self._initial_xInt == self._final_xInt and
                self._initial_yInt + 1 == self._final_yInt):
            return True
        elif (self._initial_xInt + 1 == self._final_xInt and
                self._initial_yInt + 1 == self._final_yInt):
            return True
        elif (self._initial_xInt + 1 == self._final_xInt and
                self._initial_yInt == self._final_yInt):
            return True
        elif (self._initial_xInt + 1 == self._final_xInt and
                self._initial_yInt - 1 == self._final_yInt):
            return True
        elif (self._initial_xInt == self._final_xInt and
                self._initial_yInt - 1 == self._final_yInt):
            return True
        elif (self._initial_xInt - 1 == self._final_xInt and
                self._initial_yInt - 1 == self._final_yInt):
            return True
        else:
            return False
