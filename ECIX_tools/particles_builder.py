import numpy as np

def polar_grid_particles(line, pzeta=0, zeta=0, sigma0=0, sigma=7, num_r=216, num_theta=128, theta_x=0, theta_y=0, ref_emitt=2.5e-6):

    import xpart as xp

    r = np.linspace(sigma0, sigma, num_r+1)[1:]
    theta = np.linspace(0,np.pi/2, num_theta+1, endpoint = True)[1:]

    rr, tcos= np.meshgrid(r, np.cos(theta))
    rr, tsin = np.meshgrid(r, np.sin(theta))

    Ax_norm = (rr*tcos).flatten()
    Ay_norm = (rr*tsin).flatten()

    x_norm = Ax_norm*np.cos(theta_x)
    y_norm = Ay_norm*np.cos(theta_y)
    px_norm = -Ax_norm*np.sin(theta_x)
    py_norm = -Ay_norm*np.sin(theta_y)
    
    particles = xp.build_particles(line=line, x_norm=x_norm, y_norm=y_norm, 
                                   px_norm=px_norm, py_norm=py_norm,
                                   zeta=zeta, pzeta=pzeta,
                                   nemitt_x=ref_emitt, nemitt_y=ref_emitt)

    return particles, Ax_norm, Ay_norm

def extract_coords(particles):
    context = particles._context
    
    data = {
        'x' : context.nparray_from_context_array(particles.x),
        'px' : context.nparray_from_context_array(particles.px),
        'y' : context.nparray_from_context_array(particles.y),
        'py' : context.nparray_from_context_array(particles.py),
        'zeta' : context.nparray_from_context_array(particles.zeta),
        'pzeta' : context.nparray_from_context_array(particles.pzeta),
        'at_turn' : context.nparray_from_context_array(particles.at_turn),
        'id' : context.nparray_from_context_array(particles.particle_id),
        'state' : context.nparray_from_context_array(particles.state),
    }
    return data