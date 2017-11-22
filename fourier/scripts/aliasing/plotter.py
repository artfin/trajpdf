import matplotlib.pyplot as plt
import numpy as np

def sample_sin( n, freq ):
    
    x = np.linspace( -0.2, 6.2, n )
    y = np.sin( 2 * np.pi * freq * x )

    return y

x_points = [ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0 ]
y_points = [ 0.0, 0.866, 0.866, 0.0, -0.866, -0.866, 0.0 ]

n = 300
x = np.linspace( -0.2, 6.2, n )
y1 = sample_sin( n, 0.166 )
y2 = sample_sin( n, 1.162 )

lw = 1.5
plt.plot( x, y1, color = 'r', linewidth = lw, linestyle = 'dashed' )
plt.plot( x, y2, color = 'b', linewidth = lw, linestyle = 'dashed' )

plt.scatter( x_points, y_points, marker = 's', s = 45, color = 'k' )

plt.grid( linestyle = ':', alpha = 0.7 )
plt.show()
