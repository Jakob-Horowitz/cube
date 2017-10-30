#edges only, dictionairy of edge pieces, layer by layer
#starts from front, counter clockwise around cube
#looking top down aka top piece comes first
#yellow top green front
TL = {"front" : ["yellow", "green"],
      "right" : ["yellow", "orange"],
      "back" : ["yellow","blue"],
      "left" : ["yellow", "red"]}

#middle layer has no front, starts from the right side, CCW around cube
#
ML = {"frontRight" : ["green",  "orange"],
      "backRight" : ["orange", "blue"],
      "backLeft" : ["blue", "red"],
      "frontLeft" : ["red", "green"]}

#bottom layer organized same way as top layer
#still looking top down, so sticker on bottom of cube comes second
BL = {"front" : ["green", "white"],
      "right" : ["orange", "white"],
      "back" : ["blue","white"],
      "left" : ["red", "white"]}

cubeEdges = [TL, ML, BL]

#Defining move functions here
#when going from middle layer to top or bottom layer, sticker order must be swapped
def flipEdge(edge):
    flippedEdge = [edge[1], edge[0]]
    return flippedEdge

#R turn function cycles as follows:
    #TL[right] to ML[backRight]
    #ML[backRight] to BL[right]
    #BL[right] to ML[frontRight]
    #ML[frontRight] to TL[right]

#must call flipEdge on pieces going to middle layer (cube[1])
#right face clockwise 90 degrees
def rTurn(cube):
    TLr = cube[0]["right"]
    MLbr = cube[1]["backRight"]
    BLr = cube[2]["right"]
    MLfr = cube[1]["frontRight"]

    cube[0]["right"] = MLfr
    cube[1]["backRight"] = flipEdge(TLr)
    cube[2]["right"] = MLbr
    cube[1]["frontRight"] = flipEdge(BLr)
    return cube

#front face clockwise 90 degrees
def fTurn(cube):
    TLf = cube[0]["front"]
    MLfr = cube[1]["frontRight"]
    BLf = cube[2]["front"]
    MLfl = cube[1]["frontLeft"]

    cube[0]["front"] = MLfl
    cube[1]["frontRight"] = flipEdge(TLf)
    cube[2]["front"] = MLfr
    cube[1]["frontLeft"] = flipEdge(BLf)
    return cube

#left face clockwise 90 degrees
def lTurn(cube):
    TLl = cube[0]["left"]
    MLf = cube[1]["frontLeft"]
    BLl = cube[2]["left"]
    MLb = cube[1]["backLeft"]

    cube[0]["left"] = MLb
    cube[1]["frontLeft"] = flipEdge(TLl)
    cube[2]["left"] = MLf
    cube[1]["backLeft"] = flipEdge(BLl)
    return cube

#back face clockwise 90 degrees
def bTurn(cube):
    TLb = cube[0]["back"]
    MLbr = cube[1]["backRight"]
    BLb = cube[2]["back"]
    MLbl = cube[1]["backLeft"]

    cube[0]["back"] = MLbr
    cube[1]["backLeft"] = flipEdge(TLb)
    cube[2]["back"] = MLbl
    cube[1]["backRight"] = flipEdge(BLb)
    return cube

def uTurn(cube):
    TLf = cube[0]["front"]
    TLl = cube[0]["left"]
    TLb = cube[0]["back"]
    TLr = cube[0]["right"]

    cube[0]["front"] = TLr
    cube[0]["left"] = TLf
    cube[0]["back"] = TLl
    cube[0]["right"] = TLb
    return cube

def dTurn(cube):
    BLf = cube[2]["front"]
    BLr = cube[2]["right"]
    BLb = cube[2]["back"]
    BLl = cube[2]["left"]

    cube[2]["front"] = BLl
    cube[2]["right"] = BLf
    cube[2]["back"] = BLr
    cube[2]["left"] = BLb
    return cube

#R2 U F2 R2 B2 U F R L F
cube2 = cubeEdges
cube2 = rTurn(cube2)
cube2 = rTurn(cube2)
cube2 = uTurn(cube2)
cube2 = fTurn(cube2)
cube2 = fTurn(cube2)
cube2 = rTurn(cube2)
cube2 = rTurn(cube2)
cube2 = bTurn(cube2)
cube2 = bTurn(cube2)
cube2 = uTurn(cube2)
cube2 = fTurn(cube2)
cube2 = rTurn(cube2)
cube2 = lTurn(cube2)
cube2 = fTurn(cube2)
#

colors = ["green", "red", "blue", "orange"]
movesDone = []
def uMulti(x, cube):
    for i in range(0, x):
        cube = uTurn(cube)
    return cube

def cross(cube): #insanely inefficient but it works

    for piece in cube[0]:
        
        if cube[0][piece][0] == "white":
            
            #checks for white sticker in top player
            #moves piece with white sticker over to correct slot
            #moves down to bottom later into correct cross position
            if (cube[0][piece][1] == "green") & (piece == "front"):
                cube = uMulti(0, cube)
                cube = fTurn(cube)
                cube = fTurn(cube)
                movesDone.append("F2, ")
                cross(cube)
            if (cube[0][piece][1] == "green") & (piece == "right"):
                cube = uMulti(1, cube)
                cube = fTurn(cube)
                cube = fTurn(cube)
                movesDone.append("U, F2, ")
                cross(cube)
            if (cube[0][piece][1] == "green") & (piece == "back"):
                cube = uMulti(2, cube)
                cube = fTurn(cube)
                cube = fTurn(cube)
                movesDone.append("U2, F2, ")
                cross(cube)
            if (cube[0][piece][1] == "green") & (piece == "left"):
                cube = uMulti(3, cube)
                cube = fTurn(cube)
                cube = fTurn(cube)
                movesDone.append("U', F2, ")
                cross(cube)
        if cube[0][piece][0] == "white":    
            if (cube[0][piece][1] == "orange") & (piece == "front"):
                cube = uMulti(3, cube)
                cube = rTurn(cube)
                cube = rTurn(cube)
                movesDone.append("U', R2, ")
                cross(cube)
            if (cube[0][piece][1] == "orange") & (piece == "right"):
                cube = uMulti(0, cube)
                cube = rTurn(cube)
                cube = rTurn(cube)
                movesDone.append("R2, ")
                cross(cube)
            if (cube[0][piece][1] == "orange") & (piece == "back"):
                cube = uMulti(1, cube)
                cube = rTurn(cube)
                cube = rTurn(cube)
                movesDone.append("U, R2, ")
                cross(cube)
            if (cube[0][piece][1] == "orange") & (piece == "left"):
                cube = uMulti(2, cube)
                cube = rTurn(cube)
                cube = rTurn(cube)
                movesDone.append("U2, R2, ")
                cross(cube)
            
        if cube[0][piece][0] == "white":
            if (cube[0][piece][1] == "blue") & (piece == "front"):
                cube = uMulti(2, cube)
                cube = bTurn(cube)
                cube = bTurn(cube)
                movesDone.append("U2, B2, ")
                cross(cube)
            if (cube[0][piece][1] == "blue") & (piece == "right"):
                cube = uMulti(3, cube)
                cube = bTurn(cube)
                cube = bTurn(cube)
                movesDone.append("U', B2, ")
                cross(cube)
            if (cube[0][piece][1] == "blue") & (piece == "back"):
                cube = uMulti(0, cube)
                cube = bTurn(cube)
                cube = bTurn(cube)
                movesDone.append("B2, ")
                cross(cube)
            if (cube[0][piece][1] == "blue") & (piece == "left"):
                cube = uMulti(1, cube)
                cube = bTurn(cube)
                cube = bTurn(cube)
                movesDone.append("U, B2, ")
                cross(cube)
                
        if cube[0][piece][0] == "white":    
            if (cube[0][piece][1] == "red") & (piece == "front"):
                cube = uMulti(1, cube)
                cube = lTurn(cube)
                cube = lTurn(cube)
                movesDone.append("U, L2, ")
                cross(cube)
            if (cube[0][piece][1] == "red") & (piece == "right"):
                cube = uMulti(2, cube)
                cube = lTurn(cube)
                cube = lTurn(cube)
                movesDone.append("U2, L2, ")
                cross(cube)
            if (cube[0][piece][1] == "red") & (piece == "back"):
                cube = uMulti(3, cube)
                cube = lTurn(cube)
                cube = lTurn(cube)
                movesDone.append("U', L2, ")
                cross(cube)
            if (cube[0][piece][1] == "red") & (piece == "left"):
                cube = uMulti(0, cube)
                cube = lTurn(cube)
                cube = lTurn(cube)
                movesDone.append("L2, ")
                cross(cube)
            #end white top sticker case if statements
            
            #check for white stickers in middle layer, and move them to 
            #top layer, preserves any cross pieces in place
    for edge in cube[1]:
        if edge == "frontRight":
            if cube[1][edge][1] == "white":
                cube = fTurn(cube)
                cube = fTurn(cube)
                cube = fTurn(cube)
                cube = uTurn(cube)
                cube = fTurn(cube)
                movesDone.append("F', U, F")
                cross(cube)
            if cube[1][edge][0] == "white":
                cube = rTurn(cube)
                cube = uTurn(cube)
                cube = rTurn(cube)
                cube = rTurn(cube)
                cube = rTurn(cube)
                movesDone.append("R, U, R'")
                cross(cube)
            
        if edge == "backRight":
            if cube[1][edge][1] == "white": #R' U R
                cube = rTurn(cube)
                cube = rTurn(cube)
                cube = rTurn(cube)
                cube = uTurn(cube)
                cube = rTurn(cube)
                movesDone.append("R', U, R")
                cross(cube)
            if cube[1][edge][0] == "white": #B U B'
                cube = bTurn(cube)
                cube = uTurn(cube)
                cube = bTurn(cube)
                cube = bTurn(cube)
                cube = bTurn(cube)
                movesDone.append("B, U, B'")
                cross(cube)
        
        if edge == "backLeft":
            if cube[1][edge][1] == "white": #B', U, B
                cube = bTurn(cube)
                cube = bTurn(cube)
                cube = bTurn(cube)
                cube = uTurn(cube)
                cube = bTurn(cube)
                movesDone.append("B', U, B")
                cross(cube)
            if cube[1][edge][0] == "white": #L, U, L'
                cube = lTurn(edge)
                cube = uTurn(edge)
                cube = lTurn(edge)
                cube = lTurn(edge)
                cube = lTurn(edge)
                movesDone.append("L, U, L'")
                cross(cube)
                
        if edge == "frontLeft":
            if cube[1][edge][1] == "white": #L', U, L
                cube = lTurn(edge)
                cube = lTurn(edge)
                cube = lTurn(edge)
                cube = uTurn(edge)
                cube = lTurn(edge)
                movesDone.append("L', U, L")
                cross(cube)
            if cube[1][edge][0] == "white": #F U F'
                cube = fTurn(cube)
                cube = uTurn(cube)
                cube = fTurn(cube)
                cube = fTurn(cube)
                cube = fTurn(cube)
                movesDone.append("F, U, F'")
                cross(cube)
                
    #end middle layer cases
    #begin top layer, white sticker not facing up cases
    #only 4 cases, one per position
    for edge in cube[0]:
        if cube[0][edge][1] == "white":
            if edge == "front": 
                cube = uTurn(cube)
                cube = uTurn(cube)
                cube = uTurn(cube)
                movesDone.append("U'")
                cross(cube)
        if cube[0][edge][1] == "white":
            if edge == "right": 
                cube = rTurn(cube)
                cube = rTurn(cube)
                cube = rTurn(cube)
                cube = fTurn(cube)
                cube = fTurn(cube)
                cube = fTurn(cube)
                cube = rTurn(cube)
                cube = uTurn(cube)
                cube = fTurn(cube)
                movesDone.append("R', F', R, U, F")
                cross(cube)
        if cube[0][edge][1] == "white":
            if edge == "back": 
                cube = uTurn(cube)
                movesDone.append("U")
                cross(cube)
        if cube[0][edge][1] == "white":
            if edge == "left": 
                cube = uTurn(cube)
                cube = uTurn(cube)
                movesDone.append("U2")
                cross(cube)
                


                
    return cube #end cross solution

#each of the 4 positions in the top player has 2 cases, moving to the front
#and moving to the back.

#pieces in the middle layer will be moved to the top layer to be reduced to
#one of those 8 cases

#total of 12 cases


for item in cube2:
    print(item)
    
#R2 U F2 R2 B2 U F R  L F
print()
print()
print()
for item in cross(cube2):
    print(item)
print(movesDone)
