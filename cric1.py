data = '''kohli ind pak 98
rohit ind ban 69
warner aus s 98
pollard wi ind 49
kohli ind wi 108
rohit ind sl 149'''
l = []
batsman = input ("enter batsman name:")
for row in data.splitlines():
	d = row.split()
	if d[0]==batsman:
		print(l.append(int(d[-1])))
		

