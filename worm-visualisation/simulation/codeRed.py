import networkx as nx
import random
import time
import os
from datetime import datetime
import matplotlib.pyplot as plt

# Graph
G = nx.Graph()
G.add_edges_from([
    ("web1", "web2"),
    ("web2", "web3"),
    ("web3", "web4"),
    ("web4", "web5"),
    ("web5", "web6"),
    ("web6", "web1"),
    ("web1", "bridge1"),
    ("bridge1", "monitor"),
    ("monitor", "control"),
    ("bridge1", "control"),
])

# Node types
for node in G.nodes():
    G.nodes[node]['type'] = 'web' if node.startswith("web") else 'infra'

# Infection setup
infected = set(["web1"])  # fixed starting point for reproducibility

def log_infection(node, worm_name):
    os.makedirs("//home/galya777/PycharmProjects/WormPropagationVisualizationProject/worm-visualisation/networkVMs/.vagrant/logs", exist_ok=True)
    with open(f"/home/galya777/PycharmProjects/WormPropagationVisualizationProject/worm-visualisation/vagrant/logs/{worm_name.lower()}.log", "a") as f:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.write(f"{timestamp} {worm_name} infected {node}\n")

#uses DFS graph algorithm
def code_red_propagation(G, infected):
    new_infected = set()
    for node in infected:
        if G.nodes[node]['type'] != 'web':
            continue
        for neighbor in G.neighbors(node):
            if neighbor not in infected and G.nodes[neighbor]['type'] == 'web':
                if random.random() < 0.3:
                    new_infected.add(neighbor)
    return new_infected

# Simulation loop
worm_name = "Code_red"
steps = 10
for i in range(steps):
    newly = code_red_propagation(G, infected)
    if not newly:
        break
    for node in newly:
        log_infection(node, worm_name)
    infected.update(newly)
    time.sleep(0.5)

# Final visualization
colors = ["red" if n in infected else "green" for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=colors)
plt.title("CodeRed Infection Spread")
plt.show()
