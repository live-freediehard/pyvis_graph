from pyvis.network import Network
import pandas as pd

got_net = Network(height="750px", width="100%", bgcolor="white", font_color="black", directed =True, select_menu=True,cdn_resources="local")


# set the physics layout of the network
#got_net.barnes_hut()
#got_net.force_atlas_2based()
#got_net.hrepulsion()
got_net.repulsion()

got_data = pd.read_csv("stormofswords.csv")

sources = got_data['Source']
targets = got_data['Target']
weights = got_data['Weight']

edge_data = zip(sources, targets, weights)

for e in edge_data:
                src = e[0]
                dst = e[1]
                w = e[2]

                got_net.add_node(src, src, title=src)
                got_net.add_node(dst, dst, title=dst)
                got_net.add_edge(src, dst, value=w)

neighbor_map = got_net.get_adj_list()

# add neighbor data to node hover data
for node in got_net.nodes:
                node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
                node["value"] = len(neighbor_map[node["id"]])

got_net.show("gameofthrones.html", notebook=False)