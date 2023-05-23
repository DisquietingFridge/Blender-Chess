import bpy
from bpy.props import PointerProperty
import os
from os.path import dirname as up
import chess.pgn
import math

gameFileName = "game.pgn" #filename located in same directory as blend file.
moveFrames = 12 #number of frames it takes for a piece to complete its move
restFrames = 4 #number of frames between moves

squareContents = [0] * 64 #initialize list to 64 positions
pieces = bpy.data.collections.get("Pieces")

for i in range(63): #initialize list to be PointerProperties (like a pseudo-pointer)
    squareContents[i] = bpy.props.PointerProperty(type=bpy.types.Object)
    
curFrame = 0

for obj in pieces.all_objects: #initialize first positions
    squareContents[int(obj["initSquare"])] = obj
    
    #delete and re-initialize animation data
    obj.animation_data_clear() 
    obj.location[0] = chess.square_file(int(obj["initSquare"]))
    obj.location[1] = chess.square_rank(int(obj["initSquare"]))
    
    #print(squareContents[int(obj["initSquare"])])

#navigate/open pgn file
two_up = up(up(__file__))
other_file_path = os.path.join(two_up, gameFileName)
pgn = open(other_file_path)


game = chess.pgn.read_game(pgn) #read pgn file as a game
board = game.board() #initialize board



for move in game.mainline_moves():
    board.push(move)
    
    newSquare = move.to_square # get square that piece moves to
    oldSquare = move.from_square
    newX = chess.square_file(newSquare) # get rank (x-coordinate) of target square
    newY = chess.square_rank(newSquare) # get file (y-coordinate) of target square
    
    squareContents[newSquare] = squareContents[oldSquare] #put old square piece into new square
    piece = squareContents[oldSquare] #get moving piece object by reference
    
    piece.keyframe_insert(data_path="location", frame = curFrame) #add keyframe pre-move
    curFrame = curFrame + moveFrames #increment frame by move time
    
    squareContents[oldSquare].location[0] = newX #update X coordinate location
    squareContents[oldSquare].location[1] = newY #update Y coordinate location
    squareContents[oldSquare].keyframe_insert(data_path="location",frame = curFrame) #set new keyframe
    curFrame = curFrame + restFrames #increment frame by resting time
    
    
bpy.data.scenes["Scene"].frame_end = curFrame #set end of animation to end of game
