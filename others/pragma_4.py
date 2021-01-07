# PRAGMA TEST 4 *NOT READY TO GO YET
# Santiago Garcia Arango

def minCost(numProjects, projectId, bid):

    # Vector of ids needed [0, 1, 2, 3, ..., N]
    vector_of_ids = []
    for i in range(numProjects):
        vector_of_ids.append(i)

    possibilities = []
    for i in range(len(vector_of_ids)):
        current = []
        for j in range(len(projectId)):
            if projectId[j] == i:
                current.append(bid[j])
        
        possibilities.append(current)

    total = 0

    for i in range(len(possibilities)):
        # Check =if a job has NO id offers
        if possibilities[i] == []:
            return -1
        
        total = total + min(possibilities[i])

        print("TOTAL: ", total)
        print(possibilities[i])
    
    return total





if __name__ == "__main__":
    numProjects = 2
    ProjectId = [0, 1, 0, 1, 1]
    bid = [4, 74, 47, 744, 7]
    print(minCost(numProjects, ProjectId, bid))
