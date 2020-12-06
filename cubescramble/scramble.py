import random

def scramble3(length=-1, number=1, gen2=False):
	ret=[]
	for loop in range(number):
		scr=''
		moves=['R', 'L', 'U', 'D', 'F', 'B']
		if(gen2):
			moves=['R', 'U']
		sides=["", "'", "2"]
		prevmov=-1
		num=-1
		if(length==-1):
			lent=random.randint(15, 25)
		else:
			lent=length
		for i in range(lent):
			while(num==prevmov):
				num=random.randint(0,5)
				if(gen2):
					num=random.randint(0,1)
			side=random.randint(0,2)
			prevmov=num
			scr+=moves[num]+sides[side]+' '
		scr=scr[:-1]
		ret.append(scr)
	if(len(ret)==1):
		return ret[0]
	return ret


def scramble2(length=-1, number=1):
	ret=[]
	for loop in range(number):
		scr=''
		moves=['R', 'F', 'U']
		sides=["", "'", "2"]
		prevmov=-1
		num=-1
		if(length==-1):
			lent=random.randint(8, 13)
		else:
			lent=length
		for i in range(lent):
			while(num==prevmov):
				num=random.randint(0,2)
			side=random.randint(0,2)
			prevmov=num
			scr+=moves[num]+sides[side]+' '
		scr=scr[:-1]
		ret.append(scr)
	if(len(ret)==1):
		return ret[0]
	return ret

def scramble4(length=-1, number=1):
	ret=[]
	for loop in range(number):
		scr=''
		moves=['R', 'L', 'U', 'D', 'F', 'B', 'Rw', 'Lw', 'Uw', 'Dw', 'Fw', 'Bw']
		sides=["", "'", "2"]
		prevmov=-1
		num=-1
		if(length==-1):
			lent=random.randint(38, 52)
		else:
			lent=length
		for i in range(lent):
			while(num==prevmov):
				num=random.randint(0,11)
			side=random.randint(0,2)
			prevmov=num
			scr+=moves[num]+sides[side]+' '
		scr=scr[:-1]
		ret.append(scr)
	if(len(ret)==1):
		return ret[0]
	return ret

def scramble5(length=-1, number=1):
	ret=[]
	for loop in range(number):
		scr=''
		moves=['R', 'L', 'U', 'D', 'F', 'B', 'Rw', 'Lw', 'Uw', 'Dw', 'Fw', 'Bw']
		sides=["", "'", "2"]
		prevmov=-1
		num=-1
		if(length==-1):
			lent=random.randint(38, 52)
		else:
			lent=length
		for i in range(lent):
			while(num==prevmov):
				num=random.randint(0,11)
			side=random.randint(0,2)
			prevmov=num
			scr+=moves[num]+sides[side]+' '
		scr=scr[:-1]
		ret.append(scr)
	if(len(ret)==1):
		return ret[0]
	return ret
