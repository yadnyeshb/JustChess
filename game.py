import chessmain
import os
import sys
import time


def game_start():
    print("Format : <piece><x><position> e.g." + "\n" + "C Pawn to C4 -> c4" + "\n" + "Knight to B4 -> Nb4" + "\n"
          + "Queen take F5 -> Qxf5")
    print("White Moves First")
    make_move()


def make_move():
    move_valid = False

    while not move_valid:
        move = input("Enter your move White")
        if not validate_move(move):
            print("Invalid")
            continue

        move_valid = True
        move = {"Color": "White", "Move": move}


def validate_move(move):
    check_for_syntax(move)
    exp_pos = chessmain.Pos()
    return check_for_syntax(move)


def check_for_syntax(move):
    if len(move) not in [2, 4]:
        return False
    if len(move) == 2:
        if move[0] in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            if move[1] in (str(x) for x in range(1, 9)):
                return chessmain.Pos()
    if len(move) == 3:
        if move[0] in ["K", "B", "N", "R", "Q"]:
            if move[1] in ["a", "b", "c", "d", "e", "f", "g", "h"]:
                if move[1] in (str(x) for x in range(1, 9)):
                    return True
    if len(move) == 4:
        if move[0] in ["K", "B", "N", "R", "Q"]:
            if move[1] in ["x", "X"]:
                if move[2] in ["a", "b", "c", "d", "e", "f", "g", "h"]:
                    if move[3] in (str(x) for x in range(1, 9)):
                        return True

    return False
