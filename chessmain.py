''''''
import random


class Pos:
    def __init__(self, contains_piece, _pos):
        self.cp = contains_piece
        self.row = _pos[0]
        self.col = _pos[1]
        self.pos = _pos
        self.piece = 0

    def put_piece(self, _piece):
        self.piece = _piece


class Board:
    def __init__(self):

        chess_positions = []
        for y in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            chess_positions += [y + str(x) for x in range(1, 9)]
        positions = [Pos("False", x) for x in chess_positions]
        pos_dict = {}
        for ni, i in enumerate(["a", "b", "c", "d", "e", "f", "g", "h"]):
            for nj, j in enumerate(range(1, 9)):
                pos_dict[i + str(j)] = positions[(ni * 8) + nj]

        Pieces = [Piece("Pawn", "White", "A2")]

        Pieces.append(Piece("Pawn", "White", "A2"))
        pos_dict["a2"].put_piece(Pieces[0])
        Pieces.append(Piece("Pawn", "White", "B2"))
        pos_dict["b2"].put_piece(Pieces[1])
        Pieces.append(Piece("Pawn", "White", "C2"))
        pos_dict["c2"].put_piece(Pieces[2])
        Pieces.append(Piece("Pawn", "White", "D2"))
        pos_dict["d2"].put_piece(Pieces[3])
        Pieces.append(Piece("Pawn", "White", "E2"))
        pos_dict["e2"].put_piece(Pieces[4])
        Pieces.append(Piece("Pawn", "White", "F2"))
        pos_dict["f2"].put_piece(Pieces[5])
        Pieces.append(Piece("Pawn", "White", "G2"))
        pos_dict["g2"].put_piece(Pieces[6])
        Pieces.append(Piece("Pawn", "White", "H2"))
        pos_dict["h2"].put_piece(Pieces[7])
        Pieces.append(Piece("Pawn", "Black", "A7"))
        pos_dict["a2"].put_piece(Pieces[8])
        Pieces.append(Piece("Pawn", "Black", "B7"))
        pos_dict["b2"].put_piece(Pieces[9])
        Pieces.append(Piece("Pawn", "Black", "C7"))
        pos_dict["c2"].put_piece(Pieces[10])
        Pieces.append(Piece("Pawn", "Black", "D7"))
        pos_dict["d2"].put_piece(Pieces[11])
        Pieces.append(Piece("Pawn", "Black", "E7"))
        pos_dict["e2"].put_piece(Pieces[12])
        Pieces.append(Piece("Pawn", "Black", "F7"))
        pos_dict["f2"].put_piece(Pieces[13])
        Pieces.append(Piece("Pawn", "Black", "G7"))
        pos_dict["g2"].put_piece(Pieces[14])
        Pieces.append(Piece("Pawn", "Black", "H7"))
        pos_dict["h2"].put_piece(Pieces[15])

        Pieces.append(Piece("Rook", "White", "A1"))
        pos_dict["a1"].put_piece(Pieces[16])
        Pieces.append(Piece("Rook", "White", "H1"))
        pos_dict["h2"].put_piece(Pieces[17])
        Pieces.append(Piece("Rook", "Black", "A8"))
        pos_dict["a8"].put_piece(Pieces[18])
        Pieces.append(Piece("Rook", "Black", "H8"))
        pos_dict["h8"].put_piece(Pieces[19])

        Pieces.append(Piece("Knight", "White", "B1"))
        pos_dict["b1"].put_piece(Pieces[20])
        Pieces.append(Piece("Knight", "White", "G1"))
        pos_dict["g1"].put_piece(Pieces[21])
        Pieces.append(Piece("Knight", "Black", "B8"))
        pos_dict["b8"].put_piece(Pieces[22])
        Pieces.append(Piece("Knight", "Black", "G8"))
        pos_dict["g8"].put_piece(Pieces[23])

        Pieces.append(Piece("Bishop", "White", "C1"))
        pos_dict["c1"].put_piece(Pieces[24])
        Pieces.append(Piece("Bishop", "White", "F1"))
        pos_dict["f1"].put_piece(Pieces[25])
        Pieces.append(Piece("Bishop", "Black", "C8"))
        pos_dict["c8"].put_piece(Pieces[26])
        Pieces.append(Piece("Bishop", "Black", "F8"))
        pos_dict["f8"].put_piece(Pieces[27])

        if random.randint(0, 1):
            Pieces.append(Piece("Queen", "White", "D1"))
            pos_dict["d1"].put_piece(Pieces[28])
            Pieces.append(Piece("King", "White", "E1"))
            pos_dict["e1"].put_piece(Pieces[29])
            Pieces.append(Piece("Queen", "White", "D8"))
            pos_dict["d8"].put_piece(Pieces[30])
            Pieces.append(Piece("King", "White", "E8"))
            pos_dict["e8"].put_piece(Pieces[31])
        else:
            Pieces.append(Piece("Queen", "White", "E1"))
            pos_dict["e1"].put_piece(Pieces[28])
            Pieces.append(Piece("King", "White", "D1"))
            pos_dict["d1"].put_piece(Pieces[29])
            Pieces.append(Piece("Queen", "White", "E8"))
            pos_dict["e8"].put_piece(Pieces[30])
            Pieces.append(Piece("King", "White", "D8"))
            pos_dict["d8"].put_piece(Pieces[31])


class Piece:
    def __init__(self, _type, _color, _position):
        self.type = _type
        self.color = _color
        self.col = _position[0]
        self.row = _position[1]
        self.jump_over = False
        self.upgradee = False
        self.upgrader = True
        self.move_to_being_attacked_pos = False
        self.has_been_moved = False

        if self.type == "Pawn":
            self.be_pawn()
        elif self.type == "Queen":
            self.be_queen()
        elif self.type == "King":
            self.be_king()

    def be_pawn(self):
        self.N = 1
        self.S = 0
        self.E = 0
        self.W = 0
        self.NW = 0
        self.NE = 0
        self.SW = 0
        self.SE = 0

    def be_queen(self):
        self.N = -1
        self.S = -1
        self.E = -1
        self.W = -1
        self.NW = -1
        self.NE = -1
        self.SW = -1
        self.SE = -1

    def be_king(self):
        self.N = 1
        self.S = 1
        self.E = 1
        self.W = 1
        self.NW = 1
        self.NE = 1
        self.SW = 1
        self.SE = 1
        self.move_to_being_attacked_pos = True
