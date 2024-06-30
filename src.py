############################# Code for sorting a list of tuples by mergeSort method. #################################
# Code for merging 2 sorted lists of tuples.


def merge(L1, L2, ind):
    # Given two sorted lists L1 and L2, return a new sorted list L3
    # ind is the index of the tuple that is to be sorted.
    L3 = []
    m = len(L1)
    n = len(L2)
    i = 0
    j = 0
    while (i < m) & (j < n): # in each iteration either i or j increases by 1
        if L1[i][ind] <= L2[j][ind]: # find the lower of L[i] and L[j] to copy over to L3
            L3.append(L1[i])
            i += 1
        else:
            L3.append(L2[j])
            j+= 1
    if (i == m):
        while (j < n): # Copy remaining L2 elements
            L3.append(L2[j])
            j+= 1
    else:
        while (i < m): # Copy remaining L1 elements
            L3.append(L1[i])
            i += 1
    return L3 # O(m+n)

# Code for merge sort for a list of tuples.
def mergeSort(L, ind):
    # INPUT L : any list (L s.t. True)
    # ind is the index of the tuple that is to be sorted.
    # OUTPUT L3 is a permutation of L, L3 is sorted
    n = len(L)
    if (n <= 1 ):   # L is already sorted
        return L
    else:
        mid = n//2      # find mid point of list
        # Divide the list in 2 roughly equal parts,
        L1 = L[0:mid]   # first half
        L2 = L[mid:n]   # second half
        # recursively sort first half # T(n//2)
        L1sort = mergeSort(L1, ind)
        # recursively sort second half # T(n//2)
        L2sort = mergeSort(L2, ind)
        # merge sorted lists O(n//2 + n//2)
        L3 = merge(L1sort, L2sort, ind)
        # T(n) = 2 T(n//2) + O(n)
        # Hence, T(n) = n*log(n)
    return L3



class Node:
    # Construction of a node.
    def __init__(self, key) -> None:
        self.cut_value = key
        self.leftChild = None
        self.rightChild = None
        self.is_leaf = False
        self.ytree = None   # Its the associated y-tree with the node.


def build1DRangeTree(set_of_points):
    # It builds a 1D range tree.
    # Input:
    # set_of_points = the collection of points that are to be stored in the tree.
    # Output:
    # Root node of the tree.
    if not set_of_points:
        return None
    elif len(set_of_points) == 1:
        _Node1 = Node(set_of_points[0])
        _Node1.is_leaf = True
        return _Node1
    else:
        mid = len(set_of_points)//2
        _Node = Node(set_of_points[mid])
        _Node.leftChild = build1DRangeTree(set_of_points[:mid])
        _Node.rightChild = build1DRangeTree(set_of_points[(mid+1):])
        return _Node


def build2DRangeTree(set_of_points, prefer_x = True):
    # It builds a 2D range tree.
    # Input:
    # set_of_points = the collection of points that are to be stored in the tree.
    # prefer_x = It is True if you have to build x-tree else False.
    # Output:
    # Root node of the tree.
    if not set_of_points:
        return None
    if len(set_of_points) == 1:
        node = Node(set_of_points[0])
        node.is_leaf = True
    else:
        mid = len(set_of_points)//2
        node = Node(set_of_points[mid])
        node.leftChild = build2DRangeTree(set_of_points[:mid], prefer_x)
        node.rightChild = build2DRangeTree(set_of_points[(mid+1):], prefer_x)
    if prefer_x:
        node.ytree = build2DRangeTree(set_of_points.sort(key = lambda x : x[1]), prefer_x = False)
        return node


def checkInRange(point, range, dimension):
    # Input:
    # point = a point from the set of points.
    # range = the range of allowed values of x and y.
    # dimension = the dimension of the point i.e. 1D or 2D.
    # Output:
    # It returns True id the point is in the range else False.
    if dimension == 1:
        x = point
        if (x >= range[0][0]  and x <= range[0][1] ) :
            return True
        else:
            return False
    elif dimension == 2:
        x = point[0]
        y = point[1]

        if (x >= range[0][0]   and x <= range[0][1]  and y >= range[1][0]  and y <= range[1][1] ) :
            return True
        else:
            return False


def getValue (point, prefer_x, dimension ):
    # Input:
    # point = a point from the set_of_points.
    # prefer_x = True if you have to get the value of x- coord, else False.
    # dimension = the dimension of the point i.e. 1D or 2D.
    if dimension == 1:
        value = point.cut_value
    elif dimension == 2:
        if prefer_x:
            value = point.cut_value[0]
        else:
            value = point.cut_value[1]
    return value



def findSplitNode(root, lower, upper, dimension , prefer_x ):
    # Input:
    # root = root node of the tree.
    # lower = the lower limit of the range.
    # upper = the upper limit of the range.
    # dimension = the dimension of the point i.e. 1D or 2D.
    # prefer_x = prefer_x = True if you have to get the value of x- coord, else False.
    splitnode = root
    while splitnode != None:
        node = getValue(splitnode, prefer_x, dimension)
        if upper < node:
            splitnode = splitnode.leftChild
        elif lower > node:
            splitnode = splitnode.rightChild
        elif lower <= node <= upper :
            break
    return splitnode 


def search1DRangeTree(node, lower, upper, dimension, prefer_x = True):
    # Input:
    # node = a node in the tree.
    # lower = the lower limit of the range.
    # upper = the upper limit of the range.
    # dimension = the dimension of the point i.e. 1D or 2D.
    # prefer_x = prefer_x = True if you have to get the value of x- coord, else False.
    # Output:
    # Searches for the points in range in a 1D tree.
    results1 = []
    splitnode = findSplitNode(node, lower, upper, dimension, prefer_x)
    if splitnode == None:
        return results1
    # Check if the node is a valid node in range
    elif checkInRange(getValue(splitnode, prefer_x, dimension) , [(lower, upper)], 1):
        results1.append(splitnode.value)
    # search for nodes in left subtree
    results1 += search1DRangeTree(splitnode.left, lower, upper,dimension, prefer_x)
    # search for nodes in right subtree
    results1 += search1DRangeTree(splitnode.right, lower, upper, dimension, prefer_x)
    return results1


def search2DRangeTree(tree, x1, x2, y1, y2, dimension, results = []):
    # Input:
    # tree = a node in the tree.
    # lower = the lower limit of the range.
    # upper = the upper limit of the range.
    # dimension = the dimension of the point i.e. 1D or 2D.
    # prefer_x = prefer_x = True if you have to get the value of x- coord, else False.
    # results is the result list.
    # find the node which the least common ancestor in the tree for given range.
    # Output:
    # Searches for the points in range in a 2D tree.
    splitnode = findSplitNode(tree, x1, x2, 2, True)
    if (splitnode == None):
        return results
    elif checkInRange(splitnode.cut_value, [(x1, x2), (y1, y2)], 2) :
        results.append(splitnode.cut_value)
        # Traverse the nodes in left child of split node
        l = splitnode.leftChild 
        while ( l != None ):
            # Check if the node is a valid node in range
            if checkInRange(l.cut_value, [(x1, x2), (y1, y2)], 2):
                results.append(l.cut_value)
            # Search the associated ytree at the left child of current node in xtree
            if (x1 <= l.cut_value[0]):
                if l.rightChild != None:
                    results += search1DRangeTree(l.rightChild.ytree, y1, y2, dimension, False)
                l = l.leftChild
            else:
                l = l.rightChild

        # Traverse the nodes in left child of split node
        r = splitnode.rightChild
        while ( r != None ):
            # Check if the node is a valid node in range
            if checkInRange(r.cut_value, [(x1, x2), (y1, y2)], 2):
                results.append(r.cut_value)
            # Search the associated ytree at the left child of current node in xtree
            if ( x2 >= r.cut_value[0] ):
                if r.leftChild != None:
                    results += search1DRangeTree(r.leftChild.ytree, y1, y2, dimension, False)
                r = r.rightChild
            else:
                r = r.leftChild
        
        return results
    else:
        search2DRangeTree(tree.leftChild, x1, x2, y1, y2, dimension, results)
        search2DRangeTree(tree.rightChild, x1, x2, y1, y2, dimension, results)
        return results

class PointDatabase:
    # Node class for making nodes for range tree that is used below. 
    def __init__(self, pointlist):
        global RangeTree
        RangeTree = build2DRangeTree(pointlist, True)
    def searchNearby(self, q, d):
        return search2DRangeTree(RangeTree, q[0]-d, q[0]+d, q[1]-d, q[1]+d, 2)

pointDbObject = PointDatabase([(1,6), (2,4), (3,7), (4,9), (5,1), (6,3), (7,8), (8,10),(9,2), (10,5)])
print(pointDbObject.searchNearby((4,8), 5))

            

    

        
        
