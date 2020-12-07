GOAL = 2020 

array = []


with open("data.txt", "r") as file: 
     
     for line in file: 
         line = line.strip()
         for word in line.split(" "):    
             array.append(int(word))

array.sort()

left_tail = 0
right_tail = len(array) - 1

while left_tail < right_tail:
    Sum = array[right_tail] + array[left_tail]
    if Sum == 2020: 
        print(array[right_tail] * array[left_tail])
        break

    if Sum > 2020: 
        right_tail -= 1 
    else: 
        left_tail += 1



for i in range(len(array) - 2): 
    left_tail = i + 1
    right_tail = len(array) - 1
        
    while left_tail < right_tail:
        Sum = array[i] + array[right_tail] + array[left_tail]
        if Sum == 2020: 
            print(array[i] * array[right_tail] * array[left_tail])
            break

        if Sum > 2020: 
            right_tail -= 1 
        elif Sum < 2020: 
            left_tail += 1



