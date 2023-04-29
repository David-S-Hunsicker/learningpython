from collections import deque
# this tests if the graph is bipartite

def can_be_divided(num_of_people, dislike1, dislike2):
    group = [0] * num_of_people
    adj_list = [[] for i in range(num_of_people)]

    for i in range(len(dislike1)):
        adj_list[dislike1[i]].append(dislike2[i])
        adj_list[dislike2[i]].append(dislike1[i])

    def bfs(root):
        q = deque()
        group[root] = 1
        q.append(root)

        while q:
            person = q.popleft()
            person_group = group[person]
            for disliked_person in adj_list[person]:
                if group[disliked_person] == person_group: return False
                if group[disliked_person] == 0:  # haven't visited
                    if group[person] == 1:
                        group[disliked_person] = 2
                    else:
                        group[disliked_person] = 1
                    q.append(disliked_person)
        return True

    for i in range(num_of_people):
        if group[i] == 0:
            if not bfs(i): return False
    return True


num_of_people= 7
dislike1= [6, 6, 4, 4, 0]
dislike2= [5, 3, 3, 5, 5]
print(can_be_divided(num_of_people, dislike1, dislike2))