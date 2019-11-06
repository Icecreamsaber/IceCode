import numpy as np
import math

def Matrix_R1(Alpha):
	R1 = np.array([(1,0,0), (0,math.cos(Alpha),math.sin(Alpha)), (0,-math.sin(Alpha),math.cos(Alpha))])
	return R1

def Matrix_R2(Alpha):
	R2 = np.array([(math.cos(Alpha),0,-math.sin(Alpha)), (0,1,0), (math.sin(Alpha),0,math.cos(Alpha))])
	return R2

def Matrix_R3(Alpha):
	R3 = np.array([(math.cos(Alpha),math.sin(Alpha),0), (-math.sin(Alpha),math.cos(Alpha),0), (0,0,1)])
	return R3

def Cos_Th_edge(a, b, Alpha):
	square_c = pow(a,2) + pow(b,2) - 2*a*b*math.cos(Alpha)
	return square_c

def Cos_Th_angle(a, b, c):
	if(a*b == 0):
		return -1
	Cos_c = (pow(a,2) + pow(b,2) - pow(c,2)) / (2*a*b)
	return Cos_c

def Cos_Th_angle_ex(a, b, c):
	if(a*b == 0):
		return 1
	Cos_c = (pow(a,2) + pow(b,2) - pow(c,2)) / (2*a*b)
	return Cos_c

def Sin_Th_angle(a, b, sinb):
	if(b == 0):
		return 0
	sina = a * sinb / b
	return sina

def Coord_change(Theta1, Theta2, Theta3, l1, l2, l3, l4, sl4, L1):
	Theta1 = 2*math.pi - Theta1
	
	square_x = Cos_Th_edge(L1,l2,abs(Theta2-Theta3))
	cos_alpha1 = Cos_Th_angle(sl4, math.sqrt(square_x), l3)
	sin_alpha1 = math.sqrt(1-pow(cos_alpha1,2))
	sin_alpha2 = Sin_Th_angle(L1,math.sqrt(square_x),math.sin(abs(Theta2-Theta3)))
	cos_alpha2 = Cos_Th_angle_ex(math.sqrt(square_x),l2,L1)
	sin_alpha = -(sin_alpha1*cos_alpha2+sin_alpha2*cos_alpha1)
	cos_alpha = -(cos_alpha1*cos_alpha2-sin_alpha1*sin_alpha2)

	#print(sin_alpha, cos_alpha)
	#print(math.asin(sin_alpha)*180/math.pi, math.acos(cos_alpha)*180/math.pi)
	Input_coord = np.array([l4,0,0,1])

	M1 = np.array([(cos_alpha,0,-sin_alpha), (0,1,0), (sin_alpha,0,cos_alpha)])
	O_coord = np.array([[l2, 0, 0]])
	M1 = np.insert(M1.T, 3, values = O_coord, axis = 1)
	m = np.array([[0, 0, 0, 1]])
	M1 = np.insert(M1, 3, values = m, axis = 0)
	#print(M1.dot(Input_coord))

	M2 = Matrix_R2(Theta2)
	O_coord = np.array([[1, 0, 0]])
	M2 = np.insert(M2.T, 3, values = O_coord, axis = 1)
	M2 = np.insert(M2, 3, values = m, axis = 0)
	#print(M2.dot(M1.dot(Input_coord)))

	M3 = Matrix_R1(Theta1)
	O_coord = np.array([[0, 0, 0]])
	M3 = np.insert(M3.T, 3, values = O_coord, axis = 1)
	M3 = np.insert(M3, 3, values = m, axis = 0)
	#print(M3.dot(M2.dot(M1.dot(Input_coord))))

	M4 = Matrix_R2(math.pi/2)
	O_coord = np.array([[0, 0, 0]])
	M4 = np.insert(M4.T, 3, values = O_coord, axis = 1)
	M4 = np.insert(M4, 3, values = m, axis = 0)

	Result_coord = M4.dot(M3.dot(M2.dot(M1.dot(Input_coord))))
	return Result_coord[:3]
	
#Test Example l1=l2=l3=l4=sl4=L1 = 1 Theta1 = 90 Theta2 = -90 Theta3 = -90
print(Coord_change(math.pi/2,-math.pi/2,-math.pi/2,1,1,1,1,1,1))
#Test Example l1=l2=l3=l4=sl4=L1 = 1 Theta1 = 0 Theta2 = -90 Theta3 = -90
print(Coord_change(0,-math.pi/2,-math.pi/2,1,1,1,1,1,1))
#Test Example l1=l2=l3=l4=sl4=L1 = 1 Theta1 = -45 Theta2 = -90 Theta3 = -90
print(Coord_change(-math.pi/4,-math.pi/2,-math.pi/2,1,1,1,1,1,1))
#Test Example l1=l2=l3=l4=sl4=L1 = 1 Theta1 = -45 Theta2 = -45 Theta3 = -45
print(Coord_change(-math.pi/4,-math.pi/4,-math.pi/4,1,1,1,1,1,1))
#Test Example l1=l2=l3=l4=sl4=L1 = 1 Theta1 = -45 Theta2 = 0 Theta3 = 0
print(Coord_change(-math.pi/4,0,0,1,1,1,1,1,1))
#Test Example l1=l2=l3=l4=sl4=L1 = 1 Theta1 = -45 Theta2 = -180 Theta3 = -180
print(Coord_change(-math.pi/4,-math.pi,-math.pi,1,1,1,1,1,1))
#Test Example l1=l2=l3=l4=sl4=L1 = 1 Theta1 = 0 Theta2 = -30 Theta3 = -180
print(Coord_change(0,-math.pi/6,-math.pi,1,1,1,1,1,1))
#Test Example l1=l2=l3=l4=sl4=L1 = 1 Theta1 = -45 Theta2 = -30 Theta3 = -180
print(Coord_change(-math.pi/4,-math.pi/6,-math.pi,1,1,1,1,1,1))