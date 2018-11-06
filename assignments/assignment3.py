import csv
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from random import randrange
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics.ThresholdModel as th

#creation of the graph from the networkx library
G = nx.karate_club_graph()
nx.draw_circular(G, with_labels=True,node_color='darkgray')
plt.axis('off')
plt.savefig("pics/karateClub.png")
plt.show()

#percentage of initially infected nodes
perc = 0.12

#payoff matrix for coordination game
payoffm = np.zeros((2, 2))
payoffm[0][0] =6
payoffm[0][1] = 0
payoffm[1][0] =0
payoffm[1][1] = 3

#decision threshold
threshold = payoffm[1][1]/(payoffm[0][0]+payoffm[1][1])

#creation of diffusion model
model = th.ThresholdModel(G)
config = mc.Configuration()
config.add_model_parameter('percentage_infected', perc)
for i in G.nodes():
    config.add_node_configuration("threshold", i, threshold)
model.set_initial_status(config)

#simulation of the spread
iterations = model.iteration_bunch(10)


#visualization of the diffusion 
allnodes = list(iterations[0]['status'].keys())
labels = list(iterations[0]['status'].values())
snodes = []
inodes = []
for i in range(0,len(allnodes)):
	if labels[i]==0:
		snodes.append(allnodes[i])
	else:	
		inodes.append(allnodes[i])
		
nx.draw_networkx_nodes(G, pos=nx.circular_layout(G), nodelist=snodes, node_size=300, node_color='gray' ,with_labels=True)
nx.draw_networkx_nodes(G, pos=nx.circular_layout(G), nodelist=inodes, node_size=300, node_color='red' ,with_labels=True)
nx.draw_networkx_edges(G, pos=nx.circular_layout(G))
plt.axis('off')
plt.savefig("pics/contagion0.png")
plt.show()
for iter in range(1,len(iterations)):
	allnodes = list(iterations[iter]['status'].keys())
	labels = list(iterations[iter]['status'].values())
	for i in range(0,len(allnodes)):
		if labels[i]==1:
			snodes.remove(allnodes[i])	
			inodes.append(allnodes[i])
	nx.draw_networkx_nodes(G, pos=nx.circular_layout(G), nodelist=snodes, node_size=300, node_color='gray' ,with_labels=True)
	nx.draw_networkx_nodes(G, pos=nx.circular_layout(G), nodelist=inodes, node_size=300, node_color='red' ,with_labels=True)
	nx.draw_networkx_edges(G, pos=nx.circular_layout(G))
	plt.axis('off')
	plt.savefig("pics/contagion"+str(iter)+".png")
	plt.show()
	if (len(snodes)==0):
		print('Complete Cascade done in : '+str(iter)+ ' iterations')
		break

#import of the my own graph
data = []

with open("genreGraph.csv") as f:
	reader = csv.reader(f)
	for r in reader:
		if(r !=[]):
			data.append(r)
f.close()

G1 = nx.Graph(data)
degrees = dict(G1.degree)
pos = nx.kamada_kawai_layout(G1)
node_sizes = []
i=0
max_nsize = 2500
min_nsize = 50
min_degree  = min(degrees.values())
max_degree = max(degrees.values())
for n in G1.nodes:
	deg =degrees[list(G1.nodes)[i]]
	nscaled = (((deg-min_degree)/(max_degree-min_degree))*(max_nsize-min_nsize))+min_nsize
	node_sizes.append(nscaled)
	i=i+1
plt.figure(figsize=(18,9))
nx.draw(G1,pos,with_labels=True,node_color = '#c9ada7',node_size=node_sizes,alpha = 0.5,edge_color='#f2e9e4',width=0.5,font_color ='#22223b',font_size=10)
plt.axis('off')
plt.show()


#percentage of initially infected nodes
perc = 0.25

#payoff matrix for coordination game
payoffm[0][0] =6.5
payoffm[0][1] = 0
payoffm[1][0] =0
payoffm[1][1] = 3

#decision threshold
threshold = payoffm[1][1]/(payoffm[0][0]+payoffm[1][1])

#creation of diffusion model
model1 = th.ThresholdModel(G1)
config1 = mc.Configuration()
config1.add_model_parameter('percentage_infected', perc)
#threshold = 0.25
for i in G1.nodes():
    config1.add_node_configuration("threshold", i, threshold)
model1.set_initial_status(config1)

#simulation of the spread
iterations1 = model1.iteration_bunch(15)

#visualization of the diffusion
allnodes1 = list(iterations1[0]['status'].keys())
labels1 = list(iterations1[0]['status'].values())
snodes1 = []
inodes1 = []
for i in range(0,len(allnodes1)):
	if labels1[i]==0:
		snodes1.append(allnodes1[i])
	else:	
		inodes1.append(allnodes1[i])
		
plt.figure(figsize=(18,9))
nx.draw_networkx_nodes(G1, pos, nodelist=snodes1, node_size=200, node_color='gray' ,with_labels=True)
nx.draw_networkx_nodes(G1, pos, nodelist=inodes1, node_size=200, node_color='red' ,with_labels=True)
nx.draw_networkx_edges(G1, pos)
plt.axis('off')
plt.savefig("pics/myGcontagion0.png")
plt.show()
for iter in range(1,len(iterations1)):
	allnodes1 = list(iterations1[iter]['status'].keys())
	labels1 = list(iterations1[iter]['status'].values())
	for i in range(0,len(allnodes1)):
		if labels1[i]==1:
			snodes1.remove(allnodes1[i])	
			inodes1.append(allnodes1[i])
	plt.figure(figsize=(18,9))
	nx.draw_networkx_nodes(G1, pos, nodelist=snodes1, node_size=200, node_color='gray' ,with_labels=True)
	nx.draw_networkx_nodes(G1, pos, nodelist=inodes1, node_size=200, node_color='red' ,with_labels=True)
	nx.draw_networkx_edges(G1, pos)
	plt.axis('off')
	plt.savefig("pics/myGcontagion"+str(iter)+".png")
	plt.show()
	if (len(snodes1)==0):
		print('Complete Cascade done in : '+str(iter)+ ' iterations')
		break


	
	
	

	
