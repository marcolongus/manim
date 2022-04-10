def wallis_prod(n):
	init_wallis = 1
	for i in range(1,n):
		init_wallis *= ((2*i)/(2*i - 1 ))*((2*i)/(2*i + 1))
		yield init_wallis
	return init_wallis


wallis = wallis_prod(100)
print(wallis)

for _ in range(30):
	print(2*next(wallis)) 