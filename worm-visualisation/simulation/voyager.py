import networkx as nx
import random
import time
import os
from datetime import datetime
import matplotlib.pyplot as plt

# Graph
G = nx.Graph()
G.add_edges_from([
    ("oracle1", "oracle2"),
    ("oracle2", "oracle3"),
    ("oracle3", "oracle4"),
    ("oracle4", "oracle5"),
    ("oracle5", "oracle1"),
    ("bridge2", "oracle1"),
    ("bridge2", "monitor"),
    ("bridge2", "control"),
    ("monitor", "control"),
])

# Node types
for node in G.nodes():
    G.nodes[node]['type'] = 'oracle' if node.startswith("oracle") else 'infra'

infected = set(["oracle1"])

def log_infection(node, worm_name):
    os.makedirs("/home/galya777/PycharmProjects/WormPropagationVisualizationProject/worm-visualisation/vagrant/logs", exist_ok=True)
    with open(f"/home/galya777/PycharmProjects/WormPropagationVisualizationProject/worm-visualisation/vagrant/logs/{worm_name.lower()}.log", "a") as f:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.write(f"{timestamp} {worm_name} infected {node}\n")

def voyager_propagation(G, infected):
    new_infected = set()
    for node in infected:
        if G.nodes[node]['type'] != 'oracle':
            continue
        for neighbor in G.neighbors(node):
            if neighbor not in infected and G.nodes[neighbor]['type'] == 'oracle':
                if random.random() < 0.5:
                    new_infected.add(neighbor)
    return new_infected

# Simulation loop
worm_name = "Voyager"
steps = 10
for i in range(steps):
    newly = voyager_propagation(G, infected)
    if not newly:
        break
    for node in newly:
        log_infection(node, worm_name)
    infected.update(newly)
    time.sleep(0.5)

# Final visualization
colors = ["purple" if n in infected else "yellow" for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=colors)
plt.title("Voyager Infection Spread")
plt.show()
