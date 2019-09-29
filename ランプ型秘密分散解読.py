import string
import json

def results_list():
	LIST = []
	for word_1 in (string.ascii_lowercase + string.ascii_uppercase + string.punctuation):
		for word_2 in (string.ascii_lowercase + string.ascii_uppercase + string.punctuation):
			for word_3 in (string.ascii_lowercase + string.ascii_uppercase + string.punctuation):
				r = word_1 + word_2 + word_3
				r = int.from_bytes(r.encode(), byteorder='big')
				LIST.append(r)
	#print(LIST[0])
	#print(LIST[-1])
	return LIST

def gen_matrix(vk):
	matrix = []
	for i in vk:
		row = []
		for j in range(0,6):
			row.append(pow(i[0], j))
		row.append(i[1])
		matrix.append(row)
	return matrix

def Euclid(a, b):
	x1 = 1
	x2 = 0
	y1 = 0
	y2 = 1
	while(b != 0):
		q = a // b
		r = a % b
		a = b
		b = r

		x_temp = x2
		x2 = x1 - q * x2
		x1 = x_temp

		y_temp = y2
		y2 = y1 - q * y2
		y1 = y_temp
	return(x1, y1, a)

def mod_inv(a, b):
	x1, y1, d = Euclid(a, b)
	if(d == 1):
		if(x1 < 0):
			x1 += b
		return x1
	else:
		print('No inv\n')
		return

def simplify_matrix(m, q):
	for i in range(len(m)):
		inv = mod_inv(m[i][i], q)
		for k in range(len(m[i])):
			m[i][k] = m[i][k] * inv % q
		for j in range(len(m)):
			if(j != i):
				sub = m[j][i]
				for k in range(len(m[j])):
					m[j][k] = (m[j][k] - (m[i][k] * sub)) % q
	return(m)

def search_step1(m, sidlist, q):
	M1 = []
	for i in m:
		M1.append(i[-1])
	M2 = []
	for i in m:
		M2.append(i[-2])
		'''
		for j in range(len(i)-1):
			if(i[j] > 1):
				M2.append(i[j])
		'''
	M1.append(0)
	M2.append(-1)
	#print(M1)
	#print(M2)

	M1_ = []
	for i in sidlist:
		s = 0
		for j in range(len(M1)):
			s = s + pow(i, j) * M1[j]
			s %= q
		M1_.append(s)

	M2_ = []
	for i in sidlist:
		s = 0
		for j in range(len(M2)):
			s = s + pow(i, j) * M2[j]
			s %= q
		M2_.append(s)
	r = []
	r.append(M1_)
	r.append(M2_)
	return(r)

def search_step2(M1, M2, q):
	l = string.digits + string.ascii_lowercase + string.ascii_uppercase + " " #+ string.punctuation
	#l = results_list()
	'''
	head = 10000000
	tail = 0
	for i in l:
		if(i >tail):
			tail = i
		if(i < head):b
			head = i
	print(head)
	print(tail)
	'''
	for a4 in range(0, pow(2, 24) - 3):
		r = []
		for i in range(len(M1)):
			temp = (M1[i]-M2[i]*a4) % q
			'''
			if(temp > 8026746):
				#print("No_{}".format(a4))
				break
			'''
			try:
				temp = (temp.to_bytes(3, byteorder='big')).decode()
			except:
				break
			flag = False
			for i in temp:
				if(i not in l):
					flag = True
					break
			if(flag):
				#print("No{}".format(a4))
				break
			'''
			if(temp not in l):
				#print("No{}".format(a4))
				break
			'''
			r.append(temp)
		if(len(r) == 5):
			print("Yes{}".format(a4))
			result = ""
			for k in r:
				result += k
			print(result)
			#json.dump(result, open("game.txt",'a'))

#results_list()
q = pow(2, 24) - 3
#vk = [[1, 9708144], [2, 7078265], [3, 12273249], [4, 2006558], [5, 6811113]]
vk = [[1, 15639325], [2, 12683394], [3, 3235206], [4, 2281303], [5, 13712268]]
n = 20
k = 6
L = 5
idlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sidlist = [21, 22, 23, 24, 25]
m = gen_matrix(vk)
#print(m)
m = simplify_matrix(m, q)
#print(m)
M = search_step1(m, sidlist, q)
M1 = M[0]
M2 = M[1]
search_step2(M1, M2, q)
