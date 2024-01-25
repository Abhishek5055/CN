count = 1000
packets = [200,500,450,700,600,300,200]

length = len(packets)
index = length -1 

while index>=0:
    while index>=0 and count > packets[index]:
        print("packet moved out of the queue is",packets[index])
        count = count-packets[index]
        index = index-1
    
    if index >=0:
        print("Count is less than packet value:")
        count = 1000

print("All packets are moved out of the queue successfully")