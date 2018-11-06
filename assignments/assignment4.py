import csv
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import random

#random attack function
def randomAttack(graph,pos,perc):
	print('\n'+'-------------- RANDOM ATTACK -------------- '+'\n')
	G = graph.copy()
	n = round(len(G.nodes)*perc)
	#print(graph.nodes
	print('\n'+'Initial Metrics')
	#print(len(graph.nodes))
	d = computeMetrics(G)
	for i in range (0,n):
		index = random.choice(list(G.nodes))
		#print(index)
		G.remove_node(index)
	print('\n'+'After random attack')
	#print(len(graph.nodes))
	d = computeMetrics(G)
	#plt.figure(figsize=(18,9))
	#nx.draw(G, pos1,with_labels=True,node_color='darkgray')
	#plt.show()
	return d
	
#hub attack function
def hubAttack(graph,pos,perc):
	print('\n'+'-------------- HUBs ATTACK -------------- '+'\n')
	G = graph.copy()
	n = round(len(G.nodes)*perc)
	#print(graph.nodes
	print('Initial Metrics')
	#print(len(graph.nodes))
	d = computeMetrics(G)
	degrees = dict(G.degree)
	#print(degrees)
	node_sequence = sorted(degrees,key=degrees.__getitem__,reverse=True)
	#print(node_sequence)
	degree_sequence = sorted(degrees.values(),reverse = True)
	#print(degree_sequence)
	for i in range (0,n):
		G.remove_node(node_sequence[i])
	print('\n'+'After Hub attack')
	#print(len(graph.nodes))
	d = computeMetrics(G)
	#plt.figure(figsize=(18,9))
	#nx.draw(G, pos1,with_labels=True,node_color='darkgray')
	#plt.show()
	return d

#Page rank nodes attack function
def PRAttack(graph,pos,perc):
	print('\n'+'-------------- PAGERANKed NODES ATTACK -------------- '+'\n')
	G = graph.copy()
	n = round(len(G.nodes)*perc)
	#print(graph.nodes
	print('Initial Metrics')
	#print(len(graph.nodes))
	d = computeMetrics(G)
	pr = nx.pagerank(G, alpha=0.85, max_iter=100, tol=1e-06)
	node_rank = sorted(pr, key=pr.__getitem__,reverse=True)
	pr_rank = sorted(pr.values(),reverse = True)
	for i in range (0,n):
		G.remove_node(node_rank[i])
	print('\n'+'After high PageRank nodes attack')
	#print(len(graph.nodes))
	d = computeMetrics(G)
	#plt.figure(figsize=(18,9))
	#nx.draw(G, pos1,with_labels=True,node_color='darkgray')
	#plt.show()
	return d

#high clustering nodes attack function
def clusAttack(graph,pos,perc):
	print('\n'+'-------------- LOW CLUSTERING NODES ATTACK -------------- '+'\n')
	G = graph.copy()
	n = round(len(G.nodes)*perc)
	#print(graph.nodes
	print('Initial Metrics')
	#print(len(graph.nodes))
	d = computeMetrics(G)
	local_clustering = nx.clustering(G)
	cluster_rank = sorted(local_clustering, key=local_clustering.__getitem__)
	for i in range (0,n):
		G.remove_node(cluster_rank[i])
	print('\n'+'After high Clustering nodes attack')
	#print(len(graph.nodes))
	d = computeMetrics(G)
	#plt.figure(figsize=(18,9))
	#nx.draw(G, pos1,with_labels=True,node_color='darkgray')
	#plt.show()
	return d

#High betweeness nodes attack
def betweenAttack(graph,pos,perc):
	print('\n'+'-------------- HIGH BETWEENESS NODES ATTACK -------------- '+'\n')
	G = graph.copy()
	n = round(len(G.nodes)*perc)
	#print(graph.nodes
	print('\n'+'Initial Metrics')
	d = computeMetrics(G)
	betweenness = nx.betweenness_centrality(G,normalized=True)
	btw_rank = sorted(betweenness, key=betweenness.__getitem__, reverse=True)
	for i in range (0,n):
		G.remove_node(btw_rank[i])
	print('\n'+'After Broker attack')
	#print(len(graph.nodes))
	#plt.figure(figsize=(18,9))
	#nx.draw(G, pos1,with_labels=True,node_color='darkgray')
	d = computeMetrics(G)
	#plt.show()
	return d
	
#mesurements computing function
def computeMetrics(G):
	n = G.number_of_nodes()
	print('Number of Nodes: ' +str(n))
	m = G.number_of_edges()
	print('Number of Edges: '+str(m))
	degrees = dict(G.degree)
	avg_degree = sum(degrees.values())/n
	print('Average degree: '+str(round(avg_degree,3)))
	netdensity = nx.density(G)
	print('Density: '+str(round(netdensity,3)))
	Gcc = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)
	print('Number of connected Components: '+ str(len(Gcc)))
	giant = Gcc[0]
	n = giant.number_of_nodes()
	print('Number of Nodes in Giant component: ' +str(n))
	netd = nx.diameter(giant)
	print('Diameter of Giant component : ' +str(netd))
	avgpl = nx.average_shortest_path_length(giant)
	print('Average length of shortest paths of Giant component : '+str(avgpl))
	return netd

#drawing different attacks function	
def drawAttacks(graph,pos,perc,step,gtype):
	G = graph.copy()
	dr_array = []
	dh_array = []
	dpr_array = []
	dcl_array = []
	db_array = []
	perc_array = []
	for i in range(0,10):
		dr = randomAttack(G,pos,perc)
		dh = hubAttack(G,pos,perc)
		dpr = PRAttack(G,pos,perc)
		dcl = clusAttack(G,pos, perc)
		db = betweenAttack(G,pos,perc)
		dr_array.append(dr)
		dh_array.append(dh)
		dpr_array.append(dpr)
		dcl_array.append(dcl)
		db_array.append(db)
		perc_array.append(perc)
		perc = perc+step
	plt.axis([0, 1, 0, 22])
	plt.ylabel("Diameter d")
	plt.xlabel("Threshold f")
	plt.plot(perc_array,dr_array , '-', linewidth=3, color='gray')
	plt.plot(perc_array,dh_array , '-', linewidth=3, color='red')
	plt.plot(perc_array,dpr_array , '-', linewidth=2, color='black')
	plt.plot(perc_array,dcl_array , '-', linewidth=2, color='blue')
	plt.plot(perc_array,db_array , '-', linewidth=2, color='green')

	plt.legend(['Random Attack', 'Hub Attack', 'PageRank Attack', 'Cluster Attack','Betweeness Attack'], loc='upper right')
	if(gtype =='random'):
		plt.title('Random Graph Attacks')
		plt.savefig('pics/randomGraphAttacks.png')
	elif(gtype =='powerlaw'):
		plt.title('Power Law Graph Attacks')
		plt.savefig('pics/powerLawGraphAttacks.png')
	else:
		plt.title('Movie Graph Attacks')
		plt.savefig('pics/graphAttacks.png')
		
	plt.show() 


#creation of random and power law graphs from networkx library
G1 = nx.gnp_random_graph(100,0.1)
G2 = nx.powerlaw_cluster_graph(100, 5, 0.4)
pos1 = nx.spring_layout(G1)
#plt.figure(figsize=(18,9))
#nx.draw(G1, pos1,with_labels=True,node_color='darkgray')
#plt.show()
pos2 = nx.spring_layout(G2)
#plt.figure(figsize=(18,9))
#nx.draw(G2,pos2, with_labels=True,node_color='darkgray')
#plt.show()


#import of my own graph
data = []
with open("genreGraph.csv") as f:
	reader = csv.reader(f)
	for r in reader:
		if(r !=[]):
			data.append(r)
f.close()
G = nx.Graph(data)
pos = nx.kamada_kawai_layout(G)
#plt.figure(figsize=(18,9))
#nx.draw(G2,pos2, with_labels=True,node_color='darkgray')
#plt.show()

#percentage of initial nodes removal
perc = 0.05

#step to add to the percentage at each iteration 
step = 0.1

#different attacks on different graphs
print('\n'+'*********************** RANDOM GRAPH ***************************')
drawAttacks(G1,pos1,perc,step,'random')
print('\n'+'*********************** POWER LAW GRAPH ***************************')
drawAttacks(G2,pos2,perc,step,'powerlaw')
print('\n'+'*********************** MOVIE GRAPH ***************************')
drawAttacks(G,pos,perc,step,'')