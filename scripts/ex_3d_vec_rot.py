# import the rigid body motion module
import rbm
import math
import numpy as np

if __name__ == '__main__':
	# Define a test angle:
	theta = -math.pi / 2
	
	# update the output format:
	np.set_printoptions(precision = 2, suppress = True)
	
	# define a 3D vector:
	v0 = rbm.vec(0, 1, 1)  # THIS DEFINES THE VECTOR
	
	# define a 3D rotation about the y axes
	Ry = rbm.rot_y(theta)  # THIS DEFINES THE ROTATION
	
	# calculate the results of rotation
	v01 = Ry.dot(v0)  # THIS APPLIES THE ROTATION TO THE VECTOR
	print('The transformed vector is:\n', v01) 
