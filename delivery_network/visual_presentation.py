"""definition of the input file"""
import os
os.chdir('/home/onyxia/projet_info/result')
print(os.getcwd())

"""importation"""
import sys

sys.path.append("/opt/mamba/lib/python3.10/site-packages")
import graphviz 
import matplotlib.pyplot as plt
import numpy as np
from random import random

sys.path.pop()
sys.path.append("/home/onyxia/projet_info/delivery_network")
from graph import Graph, graph_from_file
import trajet_truck 

data_path = "/home/onyxia/projet_info/input/"


"""creation of a color palette with the help of a color map"""

cmap = plt.cm.jet

"""generation of random numbers to help in the creation of color"""
a = random()*100
d = random()*100

def generate_color(i):
    """this function creates a color associated with the truck model i with the help of RGB values linked to i

    Parameters: 
    -----------
    i : int
        the model of the truck

    Outputs : 
    -----------
    color : str
        a string containg a color in the format RGB
    """
    r =  int((i*a) % 255)
    g = int((i*d) % 255)
    b = int(125 + 50*(-1)**i)
    color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return color


def display_allocation(nb_road, nb_truck):

    """
    This function displays the allocation in road network  with the help of the graphviz module.

    Parameters : 
    ------------

    nb_road : int
        the number of the road network studied
    nb_truck : int
        the number of the truck catalog studied


    Outputs : 
    ------------
        a png file containing the graph
        the nodes are represenated in a circle and are linked if there is a travel used between them. The color of the dege indicates the model of the truck used for this travel
    """

    """getting acces to the allocation"""
    _, affectation, _, _, _, nb_affectation = trajet_truck.knapsack_greedy(nb_road, nb_truck, 25*10**9)

    visual_affectation = graphviz.Graph()
    created_node = ()

    """creation of the node if in the allocation the travel is used"""
    for travel in affectation:
        """Checking if the nodes are in the graph and adding them if it is not the case"""
        if travel[0][0] not in created_node:
            visual_affectation.node(str(travel[0][0]))
        if travel[0][1] not in created_node:
            visual_affectation.node(str(travel[0][1]))

        model_truck = int((travel[1]))
        
        visual_affectation.edge(str(travel[0][0]), str(travel[0][1]), color=generate_color(model_truck))
    """improve the graph to have a clear circular layout"""
    visual_affectation.attr(layout="circo")


    """display of the graph"""
    name = "allocation in the network " + str(nb_road) + " withe the " + str(nb_truck)+ " truck catalog"
    visual_affectation.render(name, format='png', view=True)
    visual_affectation.view()
    return visual_affectation



