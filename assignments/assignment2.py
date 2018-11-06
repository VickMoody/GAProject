import csv
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import collections
from networkx.algorithms import community
import community as cm

#import of my own graph
data = []
with open("genreGraph.csv") as f:
	reader = csv.reader(f)
	for r in reader:
		if(r !=[]):
			data.append(r)
f.close()

G = nx.Graph(data)
degrees = dict(G.degree)
pos = nx.kamada_kawai_layout(G)
node_sizes = []
i=0
max_nsize = 2500
min_nsize = 50
min_degree  = min(degrees.values())
max_degree = max(degrees.values())
for n in G.nodes:
	deg =degrees[list(G.nodes)[i]]
	nscaled = (((deg-min_degree)/(max_degree-min_degree))*(max_nsize-min_nsize))+min_nsize
	node_sizes.append(nscaled)
	i=i+1
plt.figure(figsize=(18,9))
nx.draw(G,pos,with_labels=True,node_color = '#c9ada7',node_size=node_sizes,alpha = 0.5,edge_color='#f2e9e4',width=0.5,font_color ='#22223b',font_size=10)
plt.savefig("pics/graph.png")
plt.axis('off')
plt.show()

#graph metrics
print("--------------------- MOVIE NETWORK STATISTICS ----------------------")
n = G.number_of_nodes()
print('Number of Nodes: ' +str(n))
m = G.number_of_edges()
print('Number of Edges: '+str(m))
avg_degree = sum(degrees.values())/n
print('Average degree: '+str(round(avg_degree,3)))
print('Min degree: '+str(min_degree))
print('Max degree: '+str(max_degree))
netdensity = nx.density(G)
print('Density: '+str(round(netdensity,3)))
netdiameter = nx.diameter(G)
print('Diameter: '+str(netdiameter))
avgpathlen = nx.average_shortest_path_length(G)
print('Average length of shortest paths: '+str(round(avgpathlen,3)))
Gcc = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)
print('Number of connected Components: '+ str(len(Gcc)))

#degree distribution visualization
degree_sequence = sorted(degrees.values())
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

plt.figure(figsize=(18,9))
plt.subplot(211)
plt.bar(deg, cnt, width=3, color='gray')
plt.title("Degree Distribution")
plt.ylabel("Count")
plt.xlabel("Degree")
plt.xticks([d + 0.2 for d in deg],deg)
plt.yticks([d - 0.2 for d in cnt],cnt)
plt.xlim(0, max_degree+5)
plt.subplot(212)
plt.plot(deg, cnt, '-', linewidth=2, color='gray')
plt.ylabel("Count")
plt.xlabel("Degree")
plt.savefig("pics/degreeDistribution.png")
plt.xlim(0, max_degree+5)
plt.show()

#degree centrality
degree = nx.degree_centrality(G)
degree_rank=sorted(degree, key=degree.__getitem__, reverse=True)

print('\n'+'Top 5 Hubs by Degree centrality-------------'+'\n')
for i in degree_rank[0:5]:
	print(i+' : '+str(round(degree.get(i),3)))

#betweenness
betweenness = nx.betweenness_centrality(G,normalized=True)
btw_rank = sorted(betweenness, key=betweenness.__getitem__, reverse=True)
print('\n'+'Top 5 Brokers by Betweenness centrality-------------'+'\n')
for i in btw_rank[0:5]:
	print(i+' : '+str(float(round(betweenness.get(i),3))))

#closeness
closeness = nx.closeness_centrality(G)
close_rank = sorted(closeness, key=closeness.__getitem__, reverse=True)
print('\n'+'Top 5 Central Nodes by Closeness centrality-------------'+'\n')
for i in close_rank[0:5]:
	print(i+' : '+str(round(closeness.get(i),3)))

#local and global clustering
local_clustering = nx.clustering(G)
cluster_rank = sorted(local_clustering, key=local_clustering.__getitem__,reverse = True)
print('\n'+'Top 5 Nodes by Local Clustering Coeff-------------'+'\n')
for i in cluster_rank[0:5]:
	print(i+' : '+str(round(local_clustering.get(i),3)))
global_clustering = nx.average_clustering(G)
print('\n'+'Global clustering: '+str(round(global_clustering,3)))

#PageRank
pr = nx.pagerank(G, alpha=0.85, max_iter=100, tol=1e-06)
pr_rank = sorted(pr, key=pr.__getitem__,reverse=True)
pr_seq = sorted(pr.values())
prCount = collections.Counter(pr_seq)
rank, cnt = zip(*prCount.items())
rank = list(rank)
for i in range(0,len(rank)):
	rank[i] = round(rank[i],4)
plt.figure(figsize=(17,9))
plt.subplot(211)
plt.bar(rank, cnt, width=0.0001, color='gray')
plt.title("PageRank Distribution")
plt.ylabel("Count")
plt.xlabel("Rank")
plt.xticks([round(d,4) for d in rank],rank)
plt.yticks([d - 0.2 for d in cnt],cnt)
plt.xlim(pr.get(len(pr)-1), pr.get(0))
plt.subplot(212)
plt.plot(rank, cnt, linewidth=1, color='gray')
plt.ylabel("Count")
plt.xlabel("Rank")
plt.xticks([round(d,4) for d in rank],rank)
plt.yticks([d - 0.2 for d in cnt],cnt)
plt.xlim(pr.get(len(pr)-1), pr.get(0))
plt.savefig("pics/PageRank.png")
plt.show()

print('\n'+'Top 20 Nodes by PageRank-------------'+'\n')
for i in pr_rank[0:20]:
	print(i+' : '+str(round(pr.get(i),4)))

#HITS
hubs,auths = nx.hits(G, max_iter=100, tol=1e-08,normalized=True)
hubs_rank = sorted(hubs, key=hubs.__getitem__,reverse=True)
auths_rank= sorted(auths, key=auths.__getitem__,reverse=True)
hub_seq = sorted(hubs.values())
auth_seq = sorted(auths.values())
hubCount = collections.Counter(hub_seq)
authCount =collections.Counter(auth_seq)
hub, cnt = zip(*hubCount.items())
auth, cnt1 = zip(*authCount.items())
hub = list(hub)
auth = list(auth)
for i in range(0,len(hub)):
	hub[i] = round(hub[i],4)
	
for i in range(0,len(auth)):
	auth[i] = round(auth[i],4)
		
plt.figure(figsize=(17,9))
plt.subplot(211)
plt.plot(hub, cnt,linewidth =1, color='gray')
plt.title("HITS Hubs Distribution")
plt.ylabel("Count")
plt.xlabel("Hub rank")
plt.xticks([round(d,4) for d in hub],hub)
plt.yticks([d - 0.2 for d in cnt],cnt)
plt.xlim(hubs.get(len(hubs)-1), hubs.get(0))
plt.subplot(212)
plt.plot(auth, cnt1,linewidth =1, color='darkgray')
plt.title("HITS Authorities Distribution")
plt.ylabel("Count")
plt.xlabel("Authority rank")
plt.xticks([round(d,4) for d in auth],auth)
plt.yticks([d - 0.2 for d in cnt1],cnt1)
plt.xlim(auths.get(len(auths)-1), auths.get(0))
plt.savefig("pics/HITS.png")
plt.show()

print('\n'+'Top 20 Hubs by HITS-------------'+'\n')
for i in hubs_rank[0:20]:
	print(i+' : '+str(round(hubs.get(i),5)))
	hubs_rank = sorted(hubs, key=hubs.__getitem__,reverse=True)

print('\n'+'Top 20 Authorities by HITS-------------'+'\n')
for i in auths_rank[0:20]:
	print(i+' : '+str(round(auths.get(i),5)))
	

#Communities and modularity
partition = cm.best_partition(G)
size = float(len(set(partition.values())))
print('\n'+'Number of Communities found: '+str(size)+'\n')
count = 0
plt.figure(figsize=(18,9))
for com in set(partition.values()):
	list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
	count = count + 1
	ncolor ='#22223b'
	if(count==1):
		ncolor = '#4a4e69'
	elif(count==2):
		ncolor = '#9a8c98'
	elif(count==3):
		ncolor= '#c9ada7'
	nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 50, node_color = ncolor)
	
nx.draw_networkx_edges(G,pos, alpha=0.4, edge_color = '#f2e9e4')
plt.axis('off')
plt.savefig("pics/communities.png")
plt.show()
modularity = cm.modularity(partition,G)
print('\n'+'Modularity: '+ str(round(modularity,3))+'\n')
