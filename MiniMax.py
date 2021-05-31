import math 

def minimax (currentDepth, nodeIndex, 
			maxTurn, scores, 
			targetDepth): 

	if (currentDepth == targetDepth): 
		return scores[nodeIndex] 
	
	if (maxTurn): 
		return max(minimax(currentDepth + 1, nodeIndex * 2, 
					False, scores, targetDepth), 
				minimax(currentDepth + 1, nodeIndex * 2 + 1, 
					False, scores, targetDepth)) 
	
	else: 
		return min(minimax(currentDepth + 1, nodeIndex * 2, 
					True, scores, targetDepth), 
				minimax(currentDepth + 1, nodeIndex * 2 + 1, 
					True, scores, targetDepth)) 
	
# Driver code 
scores = [3, 5, 2, 9, 12, 5, 23, 23] 

treeDepth = math.log(len(scores), 2) 

print("The optimal value is : ", end = "") 
print(minimax(0, 0, True, scores, treeDepth)) 