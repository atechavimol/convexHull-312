
from module import Node, Hull

# Time Complexity: O(n)
# Space Complexity: O(1)
def calc_slope(node1, node2):
    # takes in two nodes and find the slope with their x and y coordinates
    point1 = node1.point
    point2 = node2.point
    return (point1.y() - point2.y()) / (point1.x() - point2.x())

# Time Complexity: O(n)
# Space Complexity: O(1)
def combineHulls(hullL, hullR):
    # find the left and right point of the upper tangent line from hullL and hullR
    upper_left, upper_right = getUpperTangent(hullL, hullR)
    # find the left and right point of the lower tangent line from hullL and hullR
    lower_left, lower_right = getLowerTangent(hullL, hullR)

    # connect upper left tangent point to upper right tangent point
    upper_left.next = upper_right
    upper_right.prev = upper_left

    # connect lower left tangent point to lower right tangent point
    lower_left.prev = lower_right
    lower_right.next = lower_left

    # return a new hull with the leftmost point being the leftmost of hullL, and the rightmost being the rightmost of hullR
    return Hull(hullL.leftmost, hullR.rightmost)

# Time complexity: O(nlogn)
# Space complexity: O(n)
def findHull(points):
    # base case: if there is one point left, make it into a Node and make a new Hull with that Node being the leftmost and rightmost in the Hull
    if len(points) == 1:
        node = Node(points[0])
        return Hull(node, node)

    halfway = len(points) // 2

    # recurse with the first half of the points
    hullL = findHull(points[:halfway])
    # recurse with the second half the points
    hullR = findHull(points[halfway:])

    # return the combined hull of hullL and hullR
    return combineHulls(hullL, hullR)

# Time complexity: O(n)
# Space Complexity: O(1)
def getUpperTangent(hullL, hullR):
    # the starting points to find the tangent
    left_anchor = hullL.rightmost
    right_anchor = hullR.leftmost

    done = False

    while not done:
        done = True

        while calc_slope(left_anchor.prev, right_anchor) < calc_slope(left_anchor, right_anchor):
            # while the slope of left_anchor's prev node and right_anchor is smaller than the slope of left_anchor and right anchor, move left_anchor up
            left_anchor = left_anchor.prev
            # since we changed left_anchor, we are not done calculating the anchors
            done = False

        while calc_slope(left_anchor, right_anchor.next) > calc_slope(left_anchor, right_anchor):
            # while the slope of left_anchor and right_anchor' next node is greater than the slope of left_anchor and right anchor, move right_anchor up
            right_anchor = right_anchor.next
            # since we changed right_anchor, we are not done calculating the anchors
            done = False

    # return the two points that make the upper tangent line
    return left_anchor, right_anchor

# Time Complexity: O(n)
# Space Complexity: O(1)
def getLowerTangent(hullL, hullR):
    # the starting points to find the tangent

    left_anchor = hullL.rightmost
    right_anchor = hullR.leftmost

    done = False

    while not done:
        done = True
        while calc_slope(left_anchor.next, right_anchor) > calc_slope(left_anchor, right_anchor):
            # while the slope of left_anchor's next node and right_anchor is greater than the slope of left_anchor and right anchor, move left_anchor down
            left_anchor = left_anchor.next
            # since we changed left_anchor, we are not done calculating the anchors
            done = False

        while calc_slope(left_anchor, right_anchor.prev) < calc_slope(left_anchor, right_anchor):
            # while the slope of left_anchor and right_anchor' prev node is smaller than the slope of left_anchor and right anchor, move right_anchor down
            right_anchor = right_anchor.prev
            # since we changed right_anchor, we are not done calculating the anchors

            done = False

    # return the two points that make the lower tangent line
    return left_anchor, right_anchor
