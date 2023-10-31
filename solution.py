import math

# G = 6.67408e-11

# Define the bodies
central_body = (1e12, (400.0, 400.0), (0.0, 0.0))  # Central body with large mass, positioned at the origin, stationary
planet1 = (1e4, (360.0, 400.1), (0.0001, 1.5))   # Planet 1 starting at (1000, 0) with a velocity vector giving it a circular orbit
planet2 = (1e3, (400.1, 280.0), (-0.5, 0.0001))  # Planet 2 starting at (0, -500) with a velocity vector giving it a circular orbit

# Define the system
system = [central_body, planet1, planet2]

def calculate_distance(body1, body2):
    """Returns the distance between two bodies"""
    position1x = body1[1][0]
    position1y = body1[1][1]
    position2x = body2[1][0]
    position2y = body2[1][1]
    distancex = position1x - position2x
    distancey = position1y - position2y
    distance = (distancex**2 + distancey**2) ** 0.5
    return distance

    
def calculate_force(body1, body2):
    """Returns the force exerted on body1 by body2, in 2 dimensions as a tuple"""
    G = 6.6743 * (10**-11)
    if (body1[1][0] - body2[1][0])**2 != 0:
        force_x = (float(G)* (body1[0]) * (body2[0])) / ((body1[1][0] - body2[1][0])**2)
    else: 
        force_x = 0
    if (body1[1][1] - body2[1][1])**2 != 0:
        force_y = ((G* body1[0]) * body2[0]) / ((body1[1][1] - body2[1][1])**2)
    else:
        force_y = 0
    force = (force_x, force_y)
    return force


def calculate_net_force_on(body, system):
    """Returns the net force exerted on a body by all other bodies in the system, in 2 dimensions as a tuple"""
    force_list = [0,0]
    for b in system:
        if b != body:
            force_comp = calculate_force(body, b)
            force_list[0] += force_comp[0]
            force_list[1] += force_comp[1]
        else:
            continue
        force = (force_list[0], force_list[1])
    return force

# body1 = (1, (0, 0), (0, 0))
# body2 = (1, (1, 0), (0, 0))
# body3 = (1, (2, 0), (0, 0))
# system1 = [body1, body2, body3]
# print(calculate_net_force_on(body1,system1))

def calculate_acceleration(body, system):
    """Returns the acceleration of a body due to the net force exerted on it by all other bodies in the system, in 2 dimensions as a tuple"""
    force = calculate_force(body,system)
    acc_x = force[0]/body[0]
    acc_y = force[1]/body[0]
    acc = (acc_x, acc_y)
    return acc
body1 = (2, (0, 0), (0, 0))
body2 = (1, (1, 0), (0, 0))
body3 = (1, (2, 0), (0, 0))
system2 = [body1, body2, body3]
print(calculate_acceleration(body1, system2))

def update_velocity(system, dt):
    """Updates the velocities of all bodies in the system, given a time step dt"""
    system_new = []
    for b in system:
        mass, position, velocity = b
        new_v_x = dt * calculate_acceleration(b,system)[0] + velocity[0]
        new_v_y = dt * calculate_acceleration(b,system)[1] + velocity[1]
        new_v = (new_v_x, new_v_y)
        new_state = (mass, position, new_v)
        system_new.append(new_state)
    return system_new
        

   

def update(system, dt):
    """Update the positions of all bodies in the system, given a time step dt"""
    system_new = []
    for b in update_velocity(system, dt):
        mass, position, new_v = b
        new_x_position = position[0] + new_v[0] * dt
        new_y_position = position[1] + new_v[1] * dt
        new_position = (new_x_position, new_y_position)
        new_state = (mass, new_position, new_v)
        system_new.append(new_state)
    return system_new

def simulate(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps"""
    new_system = system.copy() 
    for i in range(1, num_steps):
        new_system = update(new_system, dt)
    return new_system

def simulate_with_visualization(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps, and visualizes the motion"""
    pass

if __name__ == '__main__':
    pass





