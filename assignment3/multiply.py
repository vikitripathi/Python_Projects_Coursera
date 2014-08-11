import MapReduce
import sys

mr = MapReduce.MapReduce()

"""
On a few Social Networking websites, if you are my friend, does not mean that I am your friend.
This is Python code to find all those asymmetric friendships.
"""

# =============================
# Do not modify above this line

#sted={}



def mapper(record):
	key = record[0]
	value = record[3]
	#vald=value[:-10]
	#print key
	#print record[1]
	#print vald
	if key == "a":
            i=record[1]
            j=record[2]
            for x in range(0,5):
                mr.emit_intermediate((i,x),record)
        else:
            j=record[1]
            k=record[2]
            for x in range(0,5):
                mr.emit_intermediate((x,k),record)

                
        """
	if key in dicti:
		dicti[key].append(value)
	else:
		dicti[key] = []
		dicti[key].append(value)
	if value not in dicti:
		dicti[value] = []
	"""	
	#mr.emit_intermediate(vald, key)
	
def reducer(key, list_of_values):
        #print key
        #val=list_of_values[0]
        #print key
        #print list_of_values
        #dicti = {}
        #print val
        #mr.emit((key))
        i=key[0]
        k=key[1]
        lista=[]
        listb=[]
        value=[]
        sum=0
        product=0
        
        for v in list_of_values:
            group=v[0]
            if group == "a":
                lista.append(v[1:])
            else:
                listb.append(v[1:])
                
        la=len(lista)
        lb=len(listb)
        for l in range(la):
            for m in range(lb):
                if lista[l][1]==listb[m][0]:
                    product=lista[l][2]*listb[m][2]
                    value.append(product)

        for v in value:
              sum +=v

        sumf = (sum,)      
        mr.emit((key + sumf))    
            
        """
        if val in sted:
             i+=1         
            
        else:
            sted[key] = []
	    sted[key].append(val)
            mr.emit((val))
            """
	        
        """
        if val not in  sted:
               #dicti[key]=[]
               sted[key] = []
	       sted[key].append(list_of_values)
	       mr.emit((list_of_values))
        """       
			

# Do not modify below this line
# =============================
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
