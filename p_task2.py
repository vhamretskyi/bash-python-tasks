

input= [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
 
        
def remove_duplicates(input):
        output = []
        for x in input:
            if x not in output:
                output.append(x)
        return tuple(output)
    

def min_max(input):
    print("Min: ", min(input))
    print("Max: ", max(input))
        
print(remove_duplicates(input))
min_max(input)