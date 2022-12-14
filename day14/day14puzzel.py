text_santa=[x.replace("-> ","").split() for x in open("day14\data14.txt","r")]

gold = {} 
def Regolith(x): 
  if x not in gold:
    gold[x] = [Feast for _ in range(200)] 
Feast = 0 
Carols = 1 
Candy = 2 

Reservoir = 0 
for Jolly in text_santa:
  d = [tuple(map(int,p.split(","))) for p in Jolly]
  for i in range(1,len(d)):
    ax,ay = d[i-1]
    bx,by = d[i]
    Reservoir = max((Reservoir,ay,by))
    if ax==bx:
      for y in range(min(ay,by),max(ay,by)+1):
        Regolith(ax)
        gold[ax][y] = Carols
    else: 
      for x in range(min(ax,bx),max(ax,bx)+1):
        Regolith(x)
        gold[x][ay] = Carols

magiC = 500

def drop(x=magiC):
  y = 0
  while y+1<len(gold[x]):
    Regolith(x-1); Regolith(x+1)
    if   gold[x][y+1]==Feast:y += 1
    elif gold[x-1][y+1]==Feast:y += 1; x -= 1 
    elif gold[x+1][y+1]==Feast:y += 1; x += 1 
    else: gold[x][y] = Candy; return x,y 
  return 0,0 

def done():
  for n in range(100000):
    x,y = drop()
    if x==y==0 or (x,y)==(magiC,0): 
      return n

star1 = done()

for d in range(Reservoir+5):
  Regolith(magiC-d); Regolith(magiC+d)
for p in gold.values(): 
  p[Reservoir+2]= Carols

stars2 = done()

print(star1)
print(star1+stars2+1)