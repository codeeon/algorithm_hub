import sys, math

Data = list(sys.stdin.readline().rstrip().split())

N = int(Data[0])
game = Data[1]

player = set([])

for i in range(N):
    user = sys.stdin.readline().rstrip()
    
    player.add(user)

if game == 'Y':
    play = len(player) / 1
if game == 'F':
    play = math.floor(len(player) / 2)
if game == 'O':
    play = math.floor(len(player) / 3)

print(int(play))