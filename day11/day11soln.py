#part 1
#find 3x3 grid with highest power

#input given in webpage is grid serial number
input = 9110 

def get_digit(number, n):
    return number // 10**n % 10

def power(x,y,serial):
    return(get_digit((y*(x + 10) + serial)*(x + 10), 2) - 5)

xmax, ymax, max_power = 0, 0, 0

for x in range(1,299):
    for y in range(1,299):
        current_power = sum(power(x_curr,y_curr,input) for x_curr in range(x,x+3) for y_curr in range(y,y+3))
        if current_power > max_power:
            max_power = current_power
            xmax = x
            ymax = y

print xmax, ymax, max_power
#21 13 28

#part 2
#allow squares of any dimension to find max total power


xmax, ymax, sizemax, max_power = 0, 0, 0

#naive soln too slow
for x in range(1,301):
    for y in range(1,301):
        for size in range(1,min(301-y,301-x)):
            current_power = sum(power(x_curr,y_curr,input) for x_curr in range(x,x+size) for y_curr in range(y,y+size))
            if current_power > max_power:
                max_power = current_power
                xmax = x
                ymax = y
                sizemax = size
            print x, y, size, max_power


print xmax, ymax, sizemax, max_power

#populate dictionary with list of powers for fast lookup
cells = {}

for x in range(1,301):
    for y in range(1,301):
        key = str(x)+'_'+str(y)
        cells[key] = [power(x,y,input)]

xmax, ymax, sizemax, max_power = 0, 0, 0, 0

#try calculating all squares of each size, using previous squares to avoid extra calculations
def power_square(x,y,size,cells):
    key = str(x)+'_'+str(y)
    #assume size>1 and valid inputs
    if size % 2 == 0:
        #even sides so use last even square and squares of size two to calculate extra
        if size == 2:
            power = sum(cells[str(x_curr)+'_'+str(y_curr)][0] for x_curr in range(x,x+2) for y_curr in range(y,y+2))
        else:
            power = cells[key][size-3] + sum(cells[str(x_curr)+'_'+str(y+size-2)][1] for x_curr in range(x,x+size-1,2)) + sum(cells[str(x+size-2)+'_'+str(y_curr)][1] for y_curr in range(y,y+size-3,2))
    else:
        #odd sides so use last even square and squares of size one to calculate extra
        power = cells[key][size-2] + sum(cells[str(x_curr)+'_'+str(y+size-1)][0] for x_curr in range(x,x+size)) + sum(cells[str(x+size-1)+'_'+str(y_curr)][0] for y_curr in range(y,y+size-1))
    return(power)

for size in range(2,301):
    for x in range(1,302-size):
        for y in range(1,302-size):
            key = str(x)+'_'+str(y)
            current_power = power_square(x,y,size,cells)
            cells[key].append(current_power)
            if current_power > max_power:
                max_power = current_power
                xmax = x
                ymax = y
                sizemax = size
            if x % 10 == 0 and y % 10 == 0:
                print x, y, size, max_power

print xmax, ymax, sizemax, max_power
#235 268 13 80

