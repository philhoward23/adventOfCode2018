#part 1
#find location of first crash of minecarts

day13input=open("input.txt")
input = day13input.readlines()

#have a look and read into grid
#substitute backslashes?
grid = []
for x in range(len(input)):
    print input[x]
    grid.append(input[x][:-1]) #remove newlines

def turn(direction, track, turn):
    #return direction and next turn for cart moving onto track in direction with next turn turn
    if track in ('|','-'):
        #keep going
        return(direction, turn)
    elif track == '+':
        #turn
        if turn == 'straight':
            #keep going
            return(direction, 'right')
        elif turn == 'right':
            if direction == '^':
                return('>','left')
            elif direction == 'v':
                return('<','left')
            elif direction == '<':
                return('^','left')
            else:
                #direction == '>'
                return('v','left')
        else:
            #turn == 'left'
            if direction == '^':
                return('<','straight')
            elif direction == 'v':
                return('>','straight')
            elif direction == '<':
                return('v','straight')
            else:
                #direction == '>'
                return('^','straight')            
    elif track == '/':
        #turn 
            if direction == '^':
                return('>',turn)
            elif direction == 'v':
                return('<',turn)
            elif direction == '<':
                return('v',turn)
            else:
                #direction == '>'
                return('^',turn)
    elif track == '\\':
        #turn
            if direction == '^':
                return('<',turn)
            elif direction == 'v':
                return('>',turn)
            elif direction == '<':
                return('^',turn)
            else:
                #direction == '>'
                return('v',turn)
    else:
        print 'error', 'track: ', track
        return(0)


class cart(object):
    #needs location, direction, which way to turn next
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction #^v<>
        self.turn = 'left' #left, straight, right
    #needs to move on a grid
    def move(self,grid):
        if self.direction == '^':
            self.y -= 1
        elif self.direction == 'v':
            self.y += 1
        elif self.direction == '<':
            self.x -= 1
        else:
            #self.direction == '>':
            self.x += 1
        next_track = grid[self.y][self.x]
        #print self.direction, next_track, self.turn
        self.direction, self.turn = turn(self.direction,next_track,self.turn)


#find carts
carts = []

for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == '^':
            carts.append(cart(x,y,'^'))
            grid[y] = grid[y][:x]+'|'+grid[y][x+1:]
        elif char == 'v':
            carts.append(cart(x,y,'v'))
            grid[y] = grid[y][:x]+'|'+grid[y][x+1:]
        elif char == '<':
            carts.append(cart(x,y,'<'))
            grid[y] = grid[y][:x]+'-'+grid[y][x+1:]
        elif char == '>':
            carts.append(cart(x,y,'>'))
            grid[y] = grid[y][:x]+'-'+grid[y][x+1:]
        else:
            pass


#move carts and alarm if a crash
def tick(carts, grid):
    carts.sort(key= lambda cart: (cart.y,cart.x))
    for index, cart in enumerate(carts):
        print index, cart.x, cart.y, cart.direction, cart.turn
        cart.move(grid)
        if (cart.x,cart.y) in [(other_cart.x, other_cart.y) for ii, other_cart in enumerate(carts) if ii != index]:
            print 'crash!', cart.x, cart.y 
            return(1)
    return(0)

def find_next_crash(carts,grid):
    crash = 0
    count = 0
    while crash == 0:
        crash = tick(carts,grid)
        count += 1
        print count

#111,13 after 264 ticks

#part 2
#remove carts if they crash and report location of remaining cart

def tick_and_remove(carts, grid):
    carts.sort(key= lambda cart: (cart.y,cart.x))
    crashes = []
    for index, cart in enumerate(carts):
        #print index, cart.x, cart.y, cart.direction, cart.turn
        if index not in crashes:
            cart.move(grid)
            if (cart.x,cart.y) in [(other_cart.x, other_cart.y) for ii, other_cart in enumerate(carts) if ii != index and ii not in crashes]:
                print 'crash!', cart.x, cart.y 
                crashes.append(index)
                crashes.append([ii for ii, other_cart in enumerate(carts) if other_cart.x==cart.x and other_cart.y==cart.y and ii != index and ii not in crashes][0])
                if len(crashes) == len(carts)-1:
                    print 'only one cart remains'
                    return(1, carts)
    #remove crashed carts
    print crashes, len(carts)
    carts = [cart for jj, cart in enumerate(carts) if jj not in crashes]
    print len(carts)
    return(0, carts)

def find_final_cart(carts,grid):
    final = 0
    while final == 0:
        final, carts = tick_and_remove(carts,grid)
        print len(carts)
    return(carts)
#16, 73 


def n_ticks(n):
    for x in range(n):
        tick_and_remove(carts,grid)




