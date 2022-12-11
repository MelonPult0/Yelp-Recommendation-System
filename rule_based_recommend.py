import networkx as nx
import csv
import pandas as pd
from collections import defaultdict


def make_bipartite_graph(positive_review_path):
    G = nx.Graph()
    with open(positive_review_path) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        i = 0
        for line in csv_reader:
            user_id = line[1]
            business_id = line[2]
            G.add_node(user_id, bipartite='User ID')

            G.add_node(business_id, bipartite='Business ID')

            G.add_edge(user_id, business_id)

    return G


def map_business_id_to_name(positive_review_path):
    df = pd.read_csv(positive_review_path)
    businesses_map = dict(zip(df.business_id, df.name))
    return businesses_map

# Define get_nodes_from_partition()
def get_nodes_from_partition(G, partition):
    # Initialize an empty list for nodes to be returned
    nodes = []
    # Iterate over each node in the graph G
    for n in G.nodes():
        # Check that the node belongs to the particular partition
        if G.nodes[n]["bipartite"] == partition:
            # If so, append it to the list of nodes
            nodes.append(n)
    return nodes


def shared_business_nodes(G, user1, user2):
    user1_n = G.neighbors(user1)
    user2_n = G.neighbors(user2)
    overlap = set(user1_n).intersection(user2_n)

    return overlap


def user_similarity(G, user1, user2, proj_nodes):
    # Check that the nodes belong to the 'users' partition
    assert G.nodes[user1]['bipartite'] == 'User ID'
    assert G.nodes[user2]['bipartite'] == 'User ID'

    # Get the set of nodes shared between the two users
    shared_nodes = shared_business_nodes(G, user1, user2)

    # Return the fraction of nodes in the bussiness partition
    return len(shared_nodes) / len(proj_nodes)


def most_similar_users(G, user, user_nodes, business_nodes):
    # Data checks
    assert G.nodes[user]['bipartite'] == 'User ID'

    # Get other nodes from user partition
    user_nodes = set(user_nodes)
    user_nodes.remove(user)

    # Create the dictionary: similarities
    similarities = defaultdict(list)
    for n in user_nodes:
        similarity = user_similarity(G, user, n, business_nodes)
        similarities[similarity].append(n)

    # Compute maximum similarity score: max_similarity
    max_similarity = max(similarities.keys())
    # print("the max_similarity from other users is:", max_similarity)
    # Return list of users that share maximal similarity
    return similarities[max_similarity]


def recommend_business(G,most_similar_users_list, to_user, businesses):
    l = []
    # print(from_user)
    # Get the set of business ids that from_user gives a positive review
    for i in most_similar_users_list:
        for business_id in set(G.neighbors(i)):
            l.append(business_id)

    # Get the set of business ids that to_user gives a positive review
    business_exist = set(G.neighbors(to_user))

    # Identify business ids  that the from_user is connected to but the to_user is not connected to
    recommendation_id_set= set(l).difference(business_exist)
    recommendation_business_names = []
    for id in recommendation_id_set:
        recommendation_business_names.append(businesses[id])
    return recommendation_business_names


def get_recommendation(positive_view_path, userID):
    G = make_bipartite_graph(positive_view_path)
    user_nodes = get_nodes_from_partition(G, 'User ID')
    business_nodes = get_nodes_from_partition(G, 'Business ID')
    most_similar_users_list = most_similar_users(G, userID, user_nodes, business_nodes)
    business_map = map_business_id_to_name(positive_view_path)
    recommendations = recommend_business(G, most_similar_users_list, userID, business_map)
    print(recommendations)


print(get_recommendation("yelpdata/Positive Reviews.csv", 'N3udcZJAoPzkKkGFt2vHTA'))
