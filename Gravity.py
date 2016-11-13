def plot_output(bodies, max_range = 1e13):
    fig = plot.figure()
    colours = ['r','b','g','y','m','c']
    ax = fig.add_subplot(1,1,1, projection='3d')
    ax.set_ylim([-max_range,max_range])    
    ax.set_ylim([-max_range,max_range])
    ax.set_zlim([-max_range,max_range])
    for body in bodies: 
        ax.plot(body["x"], body["y"], body["z"], c = random.choice(colours))
    
    plot.show()