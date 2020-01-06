from sklearn.decomposition import TruncatedSVD
import numpy as np
from scipy.spatial import distance


feature_matrix = [
    [5, 1, 3, 4],
    [7, 8, 1, 10],
    [3, 9, 2, 1],
    [4, 9, 3, 5],
    [5, 1, 3, 5],
    [10, 9, 2, 7],
    [10, 9, 3, 8],
    [1, 2, 4, 6],
    [4, 8, 3, 2],
    [1, 7, 5, 9],
    [9, 2, 7, 1],
    [10, 4, 3, 1],
    [5, 6, 7, 8],
    [3, 4, 5, 6],
    [8, 6, 4, 2],
    [5, 5, 5, 5],
    [2, 4, 7, 10],
    [2, 9, 9, 4],
    [9, 4, 9, 2],
    [8, 4, 10, 10],
    ]

# uses Singular Value Decomposition to reduce the dimensions to 2 features
svd_model = TruncatedSVD(n_components=2)
reduced_feature_matrix = svd_model.fit_transform(feature_matrix)

subject_subject_distances_matrix = []
subject_subject_similarity_matrix = []

# iterates through each subject in the reduced feature matrix
for query_subject_array in reduced_feature_matrix:

    distances = []
    max_distances = []
    for subject_array in reduced_feature_matrix:
        # calculates the euclidean distance
        dist = distance.euclidean(query_subject_array, subject_array)
        # stores the distances in a list
        distances.append(dist)
    subject_subject_distances_matrix.append(distances)
    max_distances.append(max(distances))

# calculates the overall maximum distance 
max_distance = max(max_distances)
print("Max Distance:" + str(max_distance))

# assigns similarity scores based on distance measures
for query_distance_array in subject_subject_distances_matrix:
    similarity_scores = []
    for d in query_distance_array:
        score = (1 - d/max_distance)
        # formats the score into a percentage with 2 decimals

        # score = '{:.2}'.format(score)
        score = round(score,3)

        # stores the similarity scores in a list
        similarity_scores.append(score)

    # adds the similarity scores for a subject into the subject-subject similarity matrix
    subject_subject_similarity_matrix.append(similarity_scores)

for s in subject_subject_similarity_matrix:
    print("Subject #" + str(subject_subject_similarity_matrix.index(s) + 1))
    print(s)
    print()

for row_number in range(len(subject_subject_similarity_matrix)):
    subject_subject_similarity_matrix[row_number][row_number]=-1
#print(subject_subject_similarity_matrix)

groups = []
grp = 1
for i in range(10):
    mx = 0
    for row_number in range(len(subject_subject_similarity_matrix)):
        for col_number in range(len(subject_subject_similarity_matrix[0])):
            sim = subject_subject_similarity_matrix[row_number][col_number]
            if sim > mx:
                mx = sim
                sub1 = row_number+1
                sub2 = col_number+1
    # print(grp,sub1,sub2,mx)
    groups.append((grp,sub1,sub2,mx))
    for k in range(len(subject_subject_similarity_matrix)):
        subject_subject_similarity_matrix[sub1-1][k] = -1
        subject_subject_similarity_matrix[k][sub2-1] = -1
        subject_subject_similarity_matrix[k][sub1-1] = -1
        subject_subject_similarity_matrix[sub2-1][k] = -1
    subject_subject_similarity_matrix[sub1-1][sub2-1]=-1
    subject_subject_similarity_matrix[sub2-1][sub1-1] = -1
    grp+=1

print(groups)