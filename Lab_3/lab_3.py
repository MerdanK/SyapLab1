
def funk(lst):
  
  numbers = []
  count = 1
  a = 3.14
  for element in range(lst):
        result = a * count
        numbers.append(result) 
        count += 1
  return numbers
        
  

perem = int(input("вводите число: "))
arr =  funk(perem)
print(arr);