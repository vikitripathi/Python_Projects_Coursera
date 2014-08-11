import MapReduce
import sys

mr = MapReduce.MapReduce()

"""
On a few Social Networking websites, if you are my friend, does not mean that I am your friend.
This is Python code to find all those asymmetric friendships.
"""

# =============================
# Do not modify above this line

sted={}
i=0


def mapper(record):
	key = record[0]
	value = record[1]
	vald=value[:-10]
	#print key
	#print record[1]
	#print vald
        """
	if key in dicti:
		dicti[key].append(value)
	else:
		dicti[key] = []
		dicti[key].append(value)
	if value not in dicti:
		dicti[value] = []
	"""	
	mr.emit_intermediate(vald, key)
	
def reducer(key, list_of_values):
        #print key
        i=0
        val=list_of_values[0]
        #print list_of_values
        #dicti = {}
        #print val
        mr.emit((key))
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
