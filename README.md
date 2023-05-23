# Blender-Chess
This is a python script I made in 2021 for an experiment in procedurally animating basic chess game moves in Blender. It was largely an experiment in working with Blender's API, and seeing what scripted animation generation would entail.

The Blender file is set up with a board and text objects representing the pieces. Upon running the script, the animation keyframes will automatically be generated, and the result can be rendered.

The script is dependent on the [python-chess](https://python-chess.readthedocs.io/en/latest/index.html) library, which is used here to interpret chess games encoded in the .PGN format. The file "game.pgn" is included as an example but can be replaced with any game of one's choosing. The script makes use of an array of "PointerProperties" sized to the 64 tiles on a chess board, so that a piece can be acted upon by looking up its board position. This is important because the chess library doesn't make a distinction about *which* unique piece is being used in a move- only the type of piece it is.

Once the chess library has interpreted the game file as a series of moves, each move is queried for information about the origin and destination cells. The positions of the pieces are updated accordingly in the file's animation timeline. The script only performs basic piece movement, and doesn't handle more sophisticated chess behavior like captures or promotion- just like regular moves, that behavior could be accommodated by querying the move for those details and applying specific kinds of animation to the timeline.
