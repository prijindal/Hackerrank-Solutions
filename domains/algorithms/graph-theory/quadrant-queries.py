def convertToInt(char):
    try:
        return int(char)
    except ValueError:
        return char

N = input();

P = [[int(i) for i in raw_input().split(' ')] for x in xrange(N)]

Q = input();

queries = [[convertToInt(i) for i in raw_input().split(' ')] for x in xrange(Q)]

quadrants = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
}

def calculateQuadrants():
    global quadrants
    quadrants = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
    };

    print(P)

    for point in P:
        x = point[0]
        y = point[1]
        if x > 0:
            # Right Cordinate
            if y > 0:
                quadrants[1] += 1
                # First Cordinate
            else :
                quadrants[4] += 1
                # Fourth Cordinate
        else:
            # Left cordinate
            if y > 0:
                quadrants[2] += 1
                # Second Cordinate
            else :
                quadrants[3] += 1
                # Third Cordinate

calculateQuadrants()

# query = ['C', 1, 4]
def execute_query(query):
    task = query[0]
    point1 = query[1]
    point2 = query[2]
    points = []
    if task == 'C':
        print('{0[1]} {0[2]} {0[3]} {0[4]}'.format(quadrants))
        # Calculate how many points from point1 to point2 are in each quadrant
    elif task == 'X':
        # Flip Points point1 to point2 on Y axis
        for i in range(point1 - 1, point2):
            point = P[i]
            point[1] = -point[1]
        calculateQuadrants()
    elif task == 'Y':
        # Flip Points point1 to point2 on Y axis
        for i in range(point1 - 1, point2):
            point = P[i]
            point[0] = -point[0]
        calculateQuadrants()


for i in queries:
    execute_query(i)
