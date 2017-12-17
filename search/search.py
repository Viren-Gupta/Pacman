# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def dfsearch(list,presentState,problem,visited):
	position=presentState[0]

	if(problem.isGoalState(position)):
		list.push(presentState)
		return True;
	
	if(position in visited):
		return False;

	list.push(presentState)	
	visited.append(position)
	for s in (problem.getSuccessors(position)):
		ans=dfsearch(list,s,problem,visited)
		if (ans==True):
			return True

	list.pop()
	return False	



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
"""
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())


    list=util.Stack()
    visited=[];
    arr=[problem.getStartState(),"START",-1]
    result=dfsearch(list,arr,problem,visited)
    
    if (result==True):
    	temp=util.Stack()
    	while (list.isEmpty()==False):
    		temp.push(list.pop())

    	from game import Directions
    	
    	path=[]	
    	while (temp.isEmpty()==False):
    		dir=(temp.pop())[1]
    		if(dir=="START"):
    			continue
    				
    		path.append(dir)


    	#print path	
    	return path
    		
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    list1=util.Queue()
    list1.push([[problem.getStartState(),"START",0]])

    visited=[]
    visited.append(problem.getStartState())

    while (list1.isEmpty()==False):
    	value=list1.pop()
    	lastElement=value[len(value)-1]
    	if (problem.isGoalState(lastElement[0])):
    		answer=[]
    		from game import Directions
    		for v in value:
    			dir=v[1]
    			if(dir=="START"):
    				continue
	    		answer.append(dir)
	    			
    		return answer

    	for s in (problem.getSuccessors(lastElement[0])):
    		if (s[0] not in visited):
    			visited.append(s[0])
	    		path=[]
	    		path=value+[s]
	    		list1.push(path)
	    		
    return []		
    util.raiseNotDefined()


def TreeSearch(problem,list1):
    """Search the shallowest nodes in the search tree first."""
    arr=[]
    count=-1
    visited=[]
    visited.append(problem.getStartState())

    if(problem.isGoalState(problem.getStartState())):
    	return []

    while (list1.isEmpty()==False or count==-1):
    	count=count+1
    	if(count==0):
    		value=[problem.getStartState(),"Stop",0]
    		lastElement=value
    	else:	
    		value=list1.pop()
    		lastElement=value[len(value)-1]
    	if count==0:
    		a=0
    	elif lastElement[0] in visited:
			continue


    		
    	if (problem.isGoalState(lastElement[0])):
    		answer=[]
    		from game import Directions
    		for v in value:		
    			dir=v[1]
    			if(dir=="Stop"):
    				continue
	    		answer.append(dir)
	    			
    		return answer

    	visited.append(lastElement[0])
    	for s in (problem.getSuccessors(lastElement[0])):
    		if s[0] in visited:
    			continue
    		else:
	    		path=[]
	    		if(count==0):
	    			path=[s]
	    		else:
	    			path=value+[s]

	    		arr=[]
	    		for i in path:
	    			arr.append(i[1])

	    		cost=problem.getCostOfActions(arr)	
	    		list1.push(path,cost)

    return []		
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    #cost = lambda path: problem.getCostOfActions([x[1] for x in path])
    list1=util.PriorityQueue()
    return TreeSearch(problem,list1)
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def TreeSearchAStar(problem,list1,heuristic):
    """Search the shallowest nodes in the search tree first."""
    arr=[]
    count=-1
    visited=[]
    visited.append(problem.getStartState())

    if(problem.isGoalState(problem.getStartState())):
    	return []

    while (list1.isEmpty()==False or count==-1):
    	count=count+1
    	if(count==0):
    		value=[problem.getStartState(),"Stop",0]
    		lastElement=value
    	else:	
    		value=list1.pop()
    		lastElement=value[len(value)-1]
    	if count==0:
    		a=0
    	elif lastElement[0] in visited:
			continue


    		
    	if (problem.isGoalState(lastElement[0])):
    		answer=[]
    		from game import Directions
    		for v in value:		
    			dir=v[1]
    			if(dir=="Stop"):
    				continue
	    		answer.append(dir)
	    			
    		return answer

    	visited.append(lastElement[0])
    	for s in (problem.getSuccessors(lastElement[0])):
    		if s[0] in visited:
    			continue
    		else:
	    		path=[]
	    		if(count==0):
	    			path=[s]
	    		else:
	    			path=value+[s]

	    		arr=[]
	    		for i in path:
	    			arr.append(i[1])

	    		cost=problem.getCostOfActions(arr)+heuristic(s[0],problem)	
	    		list1.push(path,cost)

    return []		
    util.raiseNotDefined()


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    list1=util.PriorityQueue()
    
    return TreeSearchAStar(problem,list1,heuristic)
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
