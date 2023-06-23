stadii=''
for i in range(1,8,1):
	print('Введите', str(i)+'-й','этап эволюции человека')
	temp=input()
	if i<7:
		stadii=stadii+temp+'=>'
	else:
		stadii=stadii+temp
print(stadii)