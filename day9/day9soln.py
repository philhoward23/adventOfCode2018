#part 1
#play marble game where each player inserts one marble in turn and scores on multiples of 23

day9input=open("input.txt")
input = day9input.readlines()[0].strip().split()
#458 players with 72020 marbles
player_count = int(input[0])
marble_count = int(input[6]) + 1

class Circle(object):
    def __init__(self):
        self.circle = []
        self.current = None
        self.current_index = 0
     
    def insert(self, marble):
        #insert marble between next clockwise and two next clockwise from current
        #return score: 0 if not multiple of 23
        if marble > 0:
            if (marble % 23 == 0):
                self.current_index = (self.current_index - 7) % len(self.circle)
                #score removed marble
                score = self.circle.pop(self.current_index)
                self.current = self.circle[self.current_index]                
                #score
                return(score + marble) 
            else:
                #find correct index for insertion
                self.current_index = (self.current_index + 2) % len(self.circle)
                self.circle.insert(self.current_index,marble)
                self.current = marble
                return(0)
        else:
            #assume valid use: this only happens if marble == 0
            self.circle.append(0)
            self.current = 0
            self.current_index = 0
            return(0)
        

#store score for each player
player_scores = [0 for x in range(player_count)]
circle = Circle()
current_player = 0

for marble in range(marble_count):
    player_scores[current_player] += circle.insert(marble)
    current_player = (current_player + 1) % player_count

max(player_scores)
#404502

#part 2
#what happens if highest marble is 100 times bigger
marble_count = 1 + 100*(int(input[6]))

#better data structure keeps track of links not all list positions
class Marble(object):
    def __init__(self,id):
        self.id = str(id)
        self.next = None
        self.previous = None
        
    def place(self,circle):
        #find right place in circle and return score: 0 if not multiple of 23
        current = circle.current
        if self.id == '0':
            #first marble
            self.next = self.id
            self.previous = self.id
            circle.marbles[self.id] = self
            circle.current = self.id
            return(0)
        else:
            if (int(self.id) % 23 == 0):
                removed_marble = circle.marbles[circle.navigate(-7)]
                circle.current = removed_marble.next
                circle.marbles[current].previous = removed_marble.previous
                circle.marbles[removed_marble.previous].next = circle.current
                del(circle.marbles[removed_marble.id])
                return(int(self.id) + int(removed_marble.id))
            else:
                next_marble = circle.marbles[current].next
                two_next_marble = circle.marbles[next_marble].next
                #insert between
                self.previous = next_marble
                self.next = two_next_marble
                circle.marbles[self.id] = self
                circle.current = self.id
                #update circle links
                circle.marbles[next_marble].next = self.id
                circle.marbles[two_next_marble].previous = self.id
                return(0)
                 

                 
class Circle(object):
    def __init__(self):
        self.marbles = {}
        self.current = None
    
    def navigate(self,offset):
        #return id of marble offset places from current
        id = self.current
        if offset == 0:
            return(id)
        else:
            if offset > 0:
                for move in range(offset):
                    id = self.marbles[id].next
            else:
                for move in range(-offset):
                    id = self.marbles[id].previous
            return(id)
    

player_scores = [0 for x in range(player_count)]
circle = Circle()
current_player = 0

for marble_id in range(marble_count):
    marble = Marble(marble_id)
    player_scores[current_player] += marble.place(circle)
    current_player = (current_player + 1) % player_count
    if int(marble.id) % 100000 == 0:
        print marble.id


max(player_scores)
#3243916887



