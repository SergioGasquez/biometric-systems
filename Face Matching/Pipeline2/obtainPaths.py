import sys

image_path = ("C:/Users/sergi/Desktop/SBS/lfw2/")


f = open('pairsDevTest2.txt', 'r')
buffer = f.read()

table = [map(str, row.split()) for row in buffer.strip().split("\n")]
len(table)
for i in range(0, len(table)):
	a=table[i]
	o= len(table[i])
	if (o == 3):
		folder=image_path+a[0]+"/"+a[0]
		sys.stdout.write(folder)
		sys.stdout.write("_")
		sys.stdout.write(a[1].zfill(4))
		sys.stdout.write(".jpg\n")
		sys.stdout.write(folder)
		sys.stdout.write("_")
		sys.stdout.write(a[2].zfill(4))
		sys.stdout.write(".jpg\n")
	else:
		folder=image_path+a[0]+"/"+a[0]
		sys.stdout.write(folder)
		sys.stdout.write("_")
		sys.stdout.write(a[1].zfill(4))
		sys.stdout.write(".jpg\n")
		sys.stdout.write(image_path+a[2]+"/")
		sys.stdout.write(a[2])
		sys.stdout.write("_")
		sys.stdout.write(a[3].zfill(4))
		sys.stdout.write(".jpg\n")

f.close()

