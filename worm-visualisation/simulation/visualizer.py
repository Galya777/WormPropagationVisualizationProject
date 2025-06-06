import networkx as nx
import matplotlib.pyplot as plt
import time
import os

LOG_DIR = "/home/galya777/PycharmProjects/WormPropagationVisualizationProject/worm-visualisation/vagrant/logs"
FILES = ["code_red.log", "voyager.log"]

G = nx.Graph()

# Web graph
G.add_edges_from([
    ("web1", "web2"), ("web2", "web3"), ("web3", "web4"),
    ("web4", "web5"), ("web5", "web6"), ("web6", "web1"),
    ("web1", "bridge1"), ("bridge1", "monitor"),
    ("monitor", "control"), ("bridge1", "control"),
])

# Oracle graph
G.add_edges_from([
    ("oracle1", "oracle2"), ("oracle2", "oracle3"),
    ("oracle3", "oracle4"), ("oracle4", "oracle5"),
    ("oracle5", "oracle1"), ("bridge2", "oracle1"),
    ("bridge2", "monitor"), ("bridge2", "control")
])

# Типове възли
for node in G.nodes():
    if node.startswith("web"):
        G.nodes[node]["type"] = "web"
    elif node.startswith("oracle"):
        G.nodes[node]["type"] = "oracle"
    else:
        G.nodes[node]["type"] = "infra"

# Инфектирани възли
code_red_infected = set()
voyager_infected = set()
dfs_edges = []

# Фиксирани позиции — само веднъж
pos = nx.spring_layout(G, seed=42)

# DFS път
def dfs_path(graph, start, visited=None, edges=None):
    if visited is None:
        visited = set()
    if edges is None:
        edges = []
    visited.add(start)
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            edges.append((start, neighbor))
            dfs_path(graph, neighbor, visited, edges)
    return edges

# Глобална фигура
fig, ax = plt.subplots()

def update_graph():
    plt.clf()
    colors = []
    edge_colors = []

    for node in G.nodes():
        if node in code_red_infected:
            colors.append("red")
        elif node in voyager_infected:
            colors.append("purple")
        else:
            colors.append("lightgray")

    for edge in G.edges():
        if edge in dfs_edges or (edge[1], edge[0]) in dfs_edges:
            edge_colors.append("blue")
        else:
            edge_colors.append("black")

    nx.draw(G, pos, with_labels=True, node_color=colors, edge_color=edge_colors,
            node_size=800, font_size=9)
    plt.title("Worm Infection Visualizer (DFS Highlighted)")
    plt.pause(0.3)


def parse_line(line):
    # Пример: [2025-05-28 09:52:57] Voyager infected oracle5
    if "infected" in line:
        parts = line.strip().split()
        worm = parts[2].lower()
        node = parts[-1]

        if worm == "code_red":
            code_red_infected.add(node)
        elif worm == "voyager":
            voyager_infected.add(node)

        print(f"Parsed infection: {worm} -> {node}")


def main():
    plt.ion()
    global dfs_edges
    dfs_edges = dfs_path(G, "web1")

    for file in FILES:
        path = os.path.join(LOG_DIR, file)
        if not os.path.exists(path):
            print(f"File {file} not found.")
            continue
        with open(path, "r") as f:
            for line in f:
                parse_line(line)
                update_graph()
                time.sleep(0.3)

    print("Visualization complete.")
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()
