#This is a basic model for infection on a random network and it is used as a backbone for the worms
import networkx as nx
import random
import matplotlib.pyplot as plt

#Creating a random graph
G = nx.erdos_renyi_graph(100, 0.05)
infected =set([random.choice(list(G.nodes()))])
history = [infected.copy()]

#Simulation
for i in range(10):
    new_infected = set()
    for node in infected:
        for neighbor in G.neighbors(node):
            if neighbor not in infected and random.random() < 0.2:
                new_infected.add(neighbor)
    infected.update(new_infected)
    history.append(infected.copy())

#Visualization
nx.draw(G, node_color=["red" if n in infected else "blue" for n in G.nodes()])
plt.show()
