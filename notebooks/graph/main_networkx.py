# Author: Aric Hagberg <aric.hagberg@gmail.com>

#    Copyright (C) 2011-2019 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.
import json

import flask
import networkx as nx
from networkx.readwrite import json_graph

G = nx.barbell_graph(6, 3)
# this d3 example uses the name attribute for the mouse-hover value,
# so add a name to each node
for n in G:
    G.nodes[n]['name'] = n
# write json formatted data
d = json_graph.node_link_data(G)  # node-link format to serialize
# write json
json.dump(d, open('force/force.json', 'w'))
print('Wrote node-link JSON data to force/force.json')

# Serve the file over http to allow for cross origin requests
app = flask.Flask(__name__, static_folder="force")

@app.route('/')
def static_proxy():
    return app.send_static_file('force.html')

print('\nGo to http://localhost:8000 to see the example\n')
app.run(port=8000)
