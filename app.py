import logging
import json
from pandas import json_normalize
import requests
import pandas as pd
from timeit import timeit
import networkx as nx
import matplotlib.pyplot as plt
import tempfile
import pydot
import graphviz
import base64
import io



def familyTree(baseURL, subDomain, assetID):

    df = pd.DataFrame()


    df = pd.read_csv('ancestors.csv', low_memory=False)

    G = nx.DiGraph()

    # Add edges to the graph based on parent-child relationships
    for index, row in df.iterrows():
        G.add_edge(row['Parent ID'], row['Child ID'])

    # Specify the item you want to visualize the hierarchy for
    item_to_visualize = assetID

    # Create a subgraph containing the entire hierarchy tree rooted at the specified item
    subgraph = nx.dfs_tree(G.reverse(), source=item_to_visualize).reverse()

    # Arrange the nodes in a top-down hierarchy using pydot_layout
    pos = nx.drawing.nx_pydot.pydot_layout(subgraph, prog='dot')



    # Plot the subgraph
    # # Save the plot to a temporary file
    plt.figure(figsize=(12, 12))
    nx.draw(subgraph, pos, with_labels=True, node_size=800, node_color='skyblue', font_size=10, verticalalignment='center')
    plt.title(f'Entire Hierarchy of {item_to_visualize}')

#     image_buffer = io.BytesIO()
#     plt.savefig(image_buffer, format="PNG")
#     image_buffer.seek(0)



    # Get the image data as bytes and convert it to base64
    #image_data = base64.b64encode(image_buffer.getvalue()).decode()


    # Return the base64 image data in the HTTP response
    return plt.show()
 






   
    # baseURL = req.params.get('baseURL')
    # subDomain = req.params.get('subDomain')
    # assetID = req.params.get('assetID')
baseURL = 'https://planttrack.structint.com/AIMSAPI/'
subDomain = 'ngbu'
assetID = '2018 11_0089 423'
familyTree(baseURL, subDomain, assetID)




