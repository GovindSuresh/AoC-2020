
from collections import deque

class Ship:
    
    def __init__(self, dir = 2, dir_list = [2,3,4,1], x=0, y=0):
        # North = 1, East = 2, South = 3, West = 4
        self.dir = dir
        self.dir_list = deque(dir_list)
        self.x = x
        self.y = y

    def rotation(self, direction, degrees):
        if direction == 'R':
            # Rotate the deque left, divide degrees by 90 to get number of 90
            # Degree turns
            self.dir_list.rotate(-(degrees//90))
            self.dir = self.dir_list[0] # first element is the new direction of ship

        elif direction == 'L':
            # Positive rotation here
            self.dir_list.rotate(degrees//90)
            self.dir = self.dir_list[0]

    def move(self, direction, steps):

        # North-South moves change the y
        if direction == 'N':
            self.y += steps
        elif direction == 'S':
            self.y += -steps

        # East-West moves change the x
        elif direction == 'E':
            self.x += steps
        elif direction == 'W':
            self.x += -steps

        # When moving forwards we depend upon the direction
        if direction == 'F':

            # Check N - positive change y
            if self.dir == 1:
                self.y += steps

            # Check S - negative change y    
            elif self.dir == 3:
                self.y += -steps

            # Check E - Positive change x
            elif self.dir == 2:
                self.x += steps

            # Check W - negative change x
            elif self.dir == 4:
                self.x += -steps

    def manhattan_distance(self):

        distance = abs(self.x) + abs(self.y)

        return distance

class WaypointShip():
    '''
    Class for Part 2, this incorporates a waypoint that the ship follows 
    '''
    def __init__(self, x=0, y=0, w_x = 10, w_y = 1):
        self.x = x
        self.y = y
        self.w_x = w_x
        self.w_y = w_y

    def rotation(self, direction, degrees):
        # Rotation now involves the way point rotating around the ship
        # We can use the trick of rotating by 90 degs
        # where you negate the x and the flip x and y for your vector (when going clockwise)
        
        if direction == 'R':
        
            num_rotations = degrees//90

            # Do this operation multiple times for >90 rotations
            for i in range(num_rotations):
                self.w_x = self.w_x*-1
                neg_x = self.w_x
                
                self.w_x = self.w_y
                self.w_y = neg_x
    
        # Opposite of the clockwise case
        elif direction == 'L':
            num_rotations = degrees//90

            for i in range(num_rotations):
                self.w_y = self.w_y*-1
                neg_y = self.w_y
                self.w_y = self.w_x
                self.w_x = neg_y

    def move(self, direction, steps):

        # North-South moves change the y of the waypoint
        if direction == 'N':
            self.w_y += steps
        elif direction == 'S':
            self.w_y += -steps

        # East-West moves change the x of the waypoint
        elif direction == 'E':
            self.w_x += steps
        elif direction == 'W':
            self.w_x += -steps

        # When moving forwards we depend upon the direction
        # This is the only move that moves the ship
        # We move the ship towards the waypoint coords
        if direction == 'F':

           self.x += steps*self.w_x
           self.y += steps*self.w_y

    def manhattan_distance(self):

        distance = abs(self.x) + abs(self.y)

        return distance


with open('day_8_data.txt') as f:

    # Create ship
    ship = Ship()
    waypoint_ship = WaypointShip()

    for line in f:
        line = line.rstrip()
        #print(line)

        direction = line[0]
        steps = int(line[1:])
        
        if (direction == 'R') or (direction == 'L'):
            ship.rotation(direction, steps)

            waypoint_ship.rotation(direction, steps)

        else:
            ship.move(direction, steps)

            waypoint_ship.move(direction, steps)

    distance = ship.manhattan_distance()
    w_distance = waypoint_ship.manhattan_distance()

    print(f'Ship distance {distance}')
    print(f'Waypoint ship distance {w_distance}')