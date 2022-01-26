# Tejaswi Avula
# This is an example mapper

f = open("purchases.txt","r")  # open file, read-only
o = open("output.txt", "w") # open file, write
for line in f:  
    a = line.strip().split("    ") 
    print (a )
    print (len(a ))
    if len(a) == 6:
        date, time, location, dept, amount, payType = a  #assign names
        print ("{0}\t{1}".format(location, amount))
        o.write("{0}\t{1}\n".format(location, amount))
f.close()
o.close()

