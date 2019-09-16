import numpy as np
import os
import random

def compute_euclidean_distance(point, centroid):
    return np.sqrt(np.sum((point - centroid)**2))

def assign_label_cluster(distance, data_point, centroids):
    index_of_minimum = min(distance, key=distance.get)
    return [index_of_minimum, data_point, centroids[index_of_minimum]]

def compute_new_centroids(cluster_label, centroids):
    return np.array(cluster_label + centroids)/2

def iterate_k_means(data_points, centroids, total_iteration):
    label = []
    cluster_label = []
    total_points = len(data_points)
    k = len(centroids)
    
    for iteration in range(0, total_iteration):
        for index_point in range(0, total_points):
            distance = {}
            for index_centroid in range(0, k):
                distance[index_centroid] = compute_euclidean_distance(data_points[index_point], centroids[index_centroid])
            label = assign_label_cluster(distance, data_points[index_point], centroids)
            centroids[label[0]] = compute_new_centroids(label[1], centroids[label[0]])

            if iteration == (total_iteration - 1):
                cluster_label.append(label)

    return [cluster_label, centroids]

def print_label_data(result):
    print("Result of k-Means Clustering: \n")
    for data in result[0]:
        print("data point: {}".format(data[1]))
        print("cluster number: {} \n".format(data[0]))
    print("Last centroids position: \n {}".format(result[1]))

def create_centroids(data_points, n_centroids):    
    centroids = list()
    
    max_x = 0
    max_y = 0 
    for p in data_points:
        if(p[0] > max_x):
            max_x = p[0]
        if(p[1] > max_y):
            max_y = p[1]
            
    centroids = gen_rand_points(max_x, max_y, n_centroids)
    
    return np.array(centroids)


def gen_rand_points(max_x, max_y, num_points):
    x_values = list()
    y_values = list()
    
    while(len(x_values) < num_points):
        rand_x = random.randrange(max_x + 1)
        if(rand_x not in x_values):
            x_values.append(rand_x)
            
    while(len(y_values) < num_points):
        rand_y = random.randrange(max_y + 1)
        if(rand_y not in y_values):
            y_values.append(rand_y)
            
    points = list()
    for i in range(0, len(x_values)):
        points.append([x_values[i], y_values[i]])
    
    return points
        

if __name__ == "__main__":
    filename = "C:\\Users\\giova\\Desktop\\git\\Simple-k-Means-Clustering-Python-master\\Simple-k-Means-Clustering-Python-master\\data2.csv"
    data_points = np.genfromtxt(filename, delimiter=",")

    centroids = create_centroids(data_points, 8)
    total_iteration = 100
    
    [cluster_label, new_centroids] = iterate_k_means(data_points, centroids, total_iteration)
    print_label_data([cluster_label, new_centroids])
    print()