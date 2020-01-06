from sklearn.decomposition import TruncatedSVD
import numpy as np
from scipy.spatial import distance
from preferences.models import preferences

# from cse535.authen.models import Appuser
# from django.db import models
# from authen.models import Appuser
# from models import Appuser
def save_group():
    # feature_matrix = [
    #     [5, 1, 3, 4],
    #     [7, 8, 1, 10],
    #     [3, 9, 2, 1],
    #     [4, 9, 3, 5],
    #     [5, 1, 3, 5],
    #     [10, 9, 2, 7],
    #     [10, 9, 3, 8],
    #     [1, 2, 4, 6],
    #     [4, 8, 3, 2],
    #     [1, 7, 5, 9],
    #     [9, 2, 7, 1],
    #     [10, 4, 3, 1],
    #     [5, 6, 7, 8],
    #     [3, 4, 5, 6],
    #     [8, 6, 4, 2],
    #     [5, 5, 5, 5],
    #     [2, 4, 7, 10],
    #     [2, 9, 9, 4],
    #     [9, 4, 9, 2],
    #     [8, 4, 10, 10],
    #     ]
    # feature_matrix = [
    #     [5, 1, 3, 4, 7],
    #     [7, 8, 1, 10, 4],
    #     [3, 9, 2, 1, 6],
    #     [4, 9, 3, 5, 4],
    #     [5, 1, 3, 5, 9],
    #     [10, 9, 2, 7, 3],
    #     [10, 9, 3, 8, 5],
    #     [1, 2, 4, 6, 7],
    #     [4, 8, 3, 2, 3],
    #     [1, 7, 5, 9, 5],
    #     [9, 2, 7, 1, 7],
    #     [10, 4, 3, 1, 4],
    #     [5, 6, 7, 8, 8],
    #     [3, 4, 5, 6, 5],
    #     [8, 6, 4, 2, 9],
    #     [5, 5, 5, 5, 6],
    #     [2, 4, 7, 10, 8],
    #     [2, 9, 9, 4, 6],
    #     [9, 4, 9, 2, 3],
    #     [8, 4, 10, 10, 7],
    #     ]
    feature_matrix = [
        [6, 6, 5, 5],
        [1, 1, 1, 9],
        [7, 7, 6, 8],
        [5, 7, 5, 5],
        [9, 7, 9, 6],
        [10, 7, 7, 10],
        [6, 6, 6, 6],
        [5, 3, 6, 4],
        [4, 3, 4, 3],
        [7, 7, 8, 8],
        [8, 7, 8, 7],
        [8, 5, 4, 6]]
    # uses Singular Value Decomposition to reduce the dimensions to 2 features
    svd_model = TruncatedSVD(n_components=2)
    reduced_feature_matrix = svd_model.fit_transform(feature_matrix)

    subject_subject_similarity_matrix = []
    subject_subject_distances_matrix = []

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

    ## To make the scores with subject own self neagtive
    for row_number in range(len(subject_subject_similarity_matrix)):
        subject_subject_similarity_matrix[row_number][row_number]=-1
    print(subject_subject_similarity_matrix)

    ## Create groups with decreasing compatibility (Grp 1 most compatible)
    groupsize = 2
    groups = []
    grp = 1
    for i in range(6):
        mx = -1
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

    for el in groups:
        print(el)
    return(groups)
    # print(subject_subject_similarity_matrix)

def getpreferences():
    allpref = preferences.objects.filter().order_by('userid')
    data = []
    for userpref in allpref:
        tmp = []
        tmp.append(userpref.topic1)
        tmp.append(userpref.topic2)
        tmp.append(userpref.topic3)
        tmp.append(userpref.topic4)
        tmp.append(userpref.topic5)
        data.append(tmp)

    return data



def calperformance():
    from questions.models import Questions
    from authen.models import Group
    ideal_answers = ['A']*20
    all_group_answers = list(Questions.objects.all())
    for group_ans in all_group_answers:
        score = 0
        given_answer = []
        given_answer.append(group_ans.solution1)
        given_answer.append(group_ans.solution2)
        given_answer.append(group_ans.solution3)
        given_answer.append(group_ans.solution4)
        given_answer.append(group_ans.solution5)
        given_answer.append(group_ans.solution6)
        given_answer.append(group_ans.solution7)
        given_answer.append(group_ans.solution8)
        given_answer.append(group_ans.solution9)
        given_answer.append(group_ans.solution10)
        given_answer.append(group_ans.solution11)
        given_answer.append(group_ans.solution12)
        given_answer.append(group_ans.solution13)
        given_answer.append(group_ans.solution14)
        given_answer.append(group_ans.solution15)
        given_answer.append(group_ans.solution16)
        given_answer.append(group_ans.solution17)
        given_answer.append(group_ans.solution18)
        given_answer.append(group_ans.solution19)
        given_answer.append(group_ans.solution20)
        for i in range(20):
            if given_answer[i]==ideal_answers[i]:
                score +=1
        groupobj = group_ans.group
        groupobj.score = score
        groupobj.save()
