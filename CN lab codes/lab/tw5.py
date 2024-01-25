import sys
class Network:
    def __init__(self,nodes):
        self.nodes=nodes
        self.graph={}
        self.distance_vector={}
    def add_link(self,node1,node2,cost):
        if node1 not in self.graph:
            self.graph[node1]={}
        self.graph[node1][node2]=cost
        if node2 not in self.graph:
            self.graph[node2]={}
        self.graph[node2][node1]=cost
    def initialize_distance_vector(self,node):
        self.distance_vector[node]={node:0}
        for n in self.nodes:
            if n!=node:
                self.distance_vector[node][n]=sys.maxsize
    def update_distance_vector(self,node):
        for dest in self.nodes:
            if dest!=node:
                min_cost=sys.maxsize
                for neighbor in self.graph[node]:
                    if dest in self.distance_vector[neighbor]:
                        cost=self.distance_vector[neighbor][dest]+self.graph[node][neighbor]
                    if cost<min_cost:
                        min_cost=cost
                    self.distance_vector[node][dest]=min_cost
    def print_routing_table(self,node):
        print("Routing table ")
        print("Destination\t\tcost")
        for dest,cost in self.distance_vector[node].items():
            print(f"{dest}\t\t{cost}")
        print()
if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    network = Network(nodes)

network.add_link(1, 2, 2)
network.add_link(1, 3, 2)
network.add_link(1, 4, 1)
network.add_link(2, 3, 1)
network.add_link(2, 5, 1)
network.add_link(3, 4, 1)
network.add_link(3, 5, 1)

for node in nodes:
    network.initialize_distance_vector(node)

num_iterations = 6  # Number of iterations to update the distance vectors
for _ in range(num_iterations):
        for node in nodes:
            network.update_distance_vector(node)

for node in nodes:
        network.print_routing_table(node)
