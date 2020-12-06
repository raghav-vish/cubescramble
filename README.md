#Cube Scramble
This is a project to generate scrambles for the Rubik's Cube and other related twisty puzzles.

##Usage
`pip install cubescramble`

Generate a scramble for the original 3x3 Rubik's cube
`scr=scramble3()`

Optional arguments are **length** to fix the length of the scramble, **number** to fix the number of scrambles, and **gen2** if you want 2-gen scrambles (only R and U)

Other functions include scramble2() for the 2x2 cube, scramble4() for 4x4 and scramble5() for 5x5. These functions have the same arguments except gen2

Examples of usage are:
`scramble2(length=7, number=10)`
`scramble3(gen2=True)`
`scramble4(number=5)`
`scramble5()`

