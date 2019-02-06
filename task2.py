def tuple_required(filename ):
	fin = open(filename,"r")
	for line in fin:
		line = line.split(" ")
		tp = (line[2], line[4], line[6], line[7])
		print(tp)

fin = open("street_centerlines.csv","r")
print(tuple_required("street_centrelines.csv"))
