# import time

# class LeakyBucket:
#     def __init__(self, capacity, rate):
#         self.capacity = capacity  # Maximum bucket size
#         self.rate = rate  # Rate at which the bucket leaks tokens
#         self.tokens = 0  # Current number of tokens in the bucket
#         self.last_time = time.time()

#     def add_token(self):
#         current_time = time.time()
#         time_elapsed = current_time - self.last_time
#         self.tokens = min(self.capacity, self.tokens + time_elapsed * self.rate)
#         self.last_time = current_time

#     def transmit(self, packet_size):
#         if self.tokens >= packet_size:
#             self.tokens -= packet_size
#             print(f"Transmitted {packet_size} bytes")
#             return True
#         else:
#             print("Dropped - Insufficient tokens")
#             return False

# if __name__ == "__main__":
#     bucket = LeakyBucket(capacity=50, rate=10)  # Example: 50 bytes capacity, 10 bytes/second rate

#     for i in range(1, 11):
#         print(f"Time: {i} seconds")
#         bucket.add_token()
#         packet_size = int(input("Enter the Packet size: "))  # Example: 15 bytes packet size
#         bucket.transmit(packet_size)

count = 1000
packets = [200, 500, 600, 700, 450, 400, 200]
length = len(packets)
index = length - 1
while index >= 0 and index<length:
    while  count > packets[index]:
        print("Packet moved out of queue is", packets[index])
        count = count - packets[index]
        index = index - 1
    if index >= 0:
        print("Count is less than packet value:")
        count = 1000
print("All packets are moved out of the queue successfully")
