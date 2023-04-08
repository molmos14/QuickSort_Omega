import time as t
#import psutil as p

start_time = t.time()
#peocess = p.Process()
#before_memory = p.memory_info().rss

def partition(lista, p):
	i = 0
	j = len(lista) - 1
	while i <= j:
		while lista[i] < p:
			i += 1
		while lista[j] > p:
			j -= 1
		if i <= j:
			lista[i], lista[j] = lista[j], lista[i]
			i += 1
			j -= 1
		return i
		
def lista(n):
	lista = []
	for i in range(n):
		num = int(input())
		lista.append(num)
	return lista 
	
def pivote(lista):
	p =0
	mod = len(lista) % 2
	if mod == 0:
		p = len(lista) / 2 + 1
		return p 
	else: 
		return len(lista)
		
n = int(input())
lista = lista(n)
p = pivote(lista)
partition(lista,p)

#after_memory = p.memory_info().rss
#memory_used = after_memory - before_memory

end_time = t.time()
duration = end_time - start_time

print(f"\n\ntime: {t.time()}\nmemory: none")
