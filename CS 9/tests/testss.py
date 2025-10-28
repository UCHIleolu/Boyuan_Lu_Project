import time

def f1(n):
	l = []
	for i in range(n):
		l.insert(0,i)
	return

def f2(n):
	l = []
	for i in range(n):
		l.append(i)
	return

print("starting f1")
start = time.time()
f1(200000)
end = time.time()
print("time elapsed: ", end - start, "seconds")

print("starting f2")
start = time.time()
f2(200000)
end = time.time()
print("time elapsed: ", end - start, "seconds")
