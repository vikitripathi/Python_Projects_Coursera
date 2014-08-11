import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

#above we create a MapReduce object that is used to pass data between
#the map function and the reduce function you wont need to use this object directly.

# =============================
# Do not modify above this line

def mapper(record):
    #the mapper function tokenizes each document and emits a key-value pair.
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    #list= []
    #words = value.split()
    mr.emit_intermediate(key , 1)

def reducer(key, list_of_values):
    #the reducer function sums up the list of occurrence counts and emits a count for word
    # key: word
    # value: list of occurrence counts
    #after shuffle phase
    #print key
    #print list_of_values
    total = 0
    for v in list_of_values:
      total += v
      # total +=1
    mr.emit((key, total))

# Do not modify below this line
# =============================
#the code loads the json file and executes the MapReduce query which prints the result to stdout.
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
