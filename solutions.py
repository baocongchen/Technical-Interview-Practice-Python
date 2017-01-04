# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 11:11:41 2016

@author: Tran
"""
#==============================================================================
# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring 
# of s. For example: if s = "udacity" and t = "ad", then the function returns 
# True. Your function definition should look like: question1(s, t) and return a
# boolean True or False.
#==============================================================================
def question1(s, t):
  # check for each character in string s by using slicing
  for i in range(len(s)):
    try:
      if s[i] in t:
        #if i th character of s is in t, check if is in s starting from i th 
        #character & check if each (i+j) th character of s is in t. If both 
        #conditions are satisfied then continue the loop, otherwise return False
        for j in range(len(t)):
          if t[j] in s[i:len(t)+i] and s[i+j] in t:
            continue
          else:
            return False
        # return True after the loop is done, because they're mutually inclusive
        return True
    except IndexError:
        # return False because string t is longer than s
        return False
  # return False because it fails to find an anagram of t in s
  return False

# test cases  
print 'Case 1: ', question1('hela', 'eoll')
#Case 1:  False
print 'Case 2: ', question1('helol', 'eoll')
#Case 2:  True
print 'Case 3: ', question1('eoll', 'heoll')
#Case 3:  False
print 'Case 4: ', question1('abcd', 'eoll')
#Case 4:  False
print 'Case 5: ', question1('lloex', 'eoll')
#Case 5:  True

#==============================================================================
# Question 2
# Given a string a, find the longest palindromic substring contained in a. Your 
# function definition should look like question2(a), and return a string.
#==============================================================================
def question2(a):
  # find all palindromes in the string and append them to a list
  import re
  regex = re.compile('[^a-zA-Z]')
  palindromes = []
  # loop through each i th character in a;
  # loop through each a(i:j) string in a; 
  # if a(i:j) equals reversed a(i:j), this a(i:j) is a palindrome;
  # so append it to the palindrome list.
  for i in range(0,len(a)-2):
    for j in range(i+3,len(a)+1):
      if regex.sub("",a[i:j]).lower() == ''.join(reversed(regex.sub("",a[i:j]))).lower():
        palindromes.append(a[i:j])
  # find the longest palindrome appended to the list
  if len(palindromes) == 0:
      print "There is no palindrome in the string"
      return None
  else:
    longest_pal = palindromes[0]
    for pal in palindromes[1:]:
      if len(pal) > len(longest_pal):
        longest_pal = pal
    print "The longest palindrome is: ", longest_pal
    return longest_pal
# Ex: redivider, noon, civic, radar, level, rotor, kayak, reviver.
# test cases
print "Case 1"
question2('')
#There is no palindrome in the string
print "Case 2"
question2('h')
#There is no palindrome in the string
print "Case 3"
question2('hawls')
#There is no palindrome in the string
print "Case 4"
question2('noon')
#The longest palindrome is:  noon
print "Case 5"
question2('non')
#The longest palindrome is:  non
print "Case 6"
question2('n oonlev elrediv iderMr. Owl ate my metal worm')
#The longest palindrome is:  Mr. Owl ate my metal worm


#==============================================================================
# Question 3
# Given an undirected graph G, find the minimum spanning tree within G. A minimum 
# spanning tree connects all vertices in a graph with the smallest possible total 
# weight of edges. Your function should take in and return an adjacency list 
# structured like this:
# 
# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)], 
#  'C': [('B', 5)]}
# Vertices are represented as unique strings. The function definition should be 
# question3(G)
#==============================================================================

def question3(G):  
  min_span_tree = G
  # loop through each key (vertice) in graph G
  for vertice in G:
    # outer loop is used to scan through each element of G[vertice]
    for i_index, i in enumerate(G[vertice]):
      # inner loop is used to compare each element to the others
      for j_index, j in enumerate(G[vertice]):
        # find all paths of the same that exist, then delete the longer paths.
        if i[0] == j[0]:
          if i[1] < j[1]:
            del min_span_tree[vertice][j_index]
          elif i[1] > j[1]:
            del min_span_tree[vertice][i_index]
  print min_span_tree
  return min_span_tree
#Case 1
print "Case 1"
G = {'A': [('B', 2),('B', 4)], 'B': [('A', 2), ('C', 5), ('A', 4)], 'C': [('B', 5)]} 
question3(G)
#{'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}  

#Case 2
print "Case 2"
G = {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]} 
question3(G)
#{'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]} 

#Case 3
print "Case 3"
G = {} 
question3(G)
#{}  



#==============================================================================
# Question 4
# Find the least common ancestor between two nodes on a binary search tree. The
# least common ancestor is the farthest node from the root that is an ancestor 
# of both nodes. For example, the root is a common ancestor of all nodes on the
# tree, but if both nodes are descendents of the root's left child, then that 
# left child might be the lowest common ancestor. You can assume that both 
# nodes are in the tree, and the tree itself adheres to all BST properties. The
# function definition should look like question4(T, r, n1, n2), where T is the 
# tree represented as a matrix, where the index of the list is equal to the 
# integer stored in that node and a 1 represents a child node, r is a 
# non-negative integer representing the root, and n1 and n2 are non-negative 
# integers representing the two nodes in no particular order. For example, one 
# test case might be
# 
# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)
# and the answer would be 3.
#==============================================================================

def question4(T, r, n1, n2):
  def rindex(mylist, myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1
  lca = r
  # if the target values are in different subtrees, then current_node is the LCA.
  for i in range(len(T)):
    if n1 < lca < n2:
      break
    # if both target nodes are in the left subtree, then check the left child
    elif n1 < lca and n2 < lca:
      lca = T[lca].index(1)
    # if both target nodes are in the right subtree, then check the right child
    elif n1 > lca and n2 > lca:
      lca = T[lca].rindex(T[lca], 1)
    # return None if there's no LCA existing between n1 and n2
    else:
      print "There's no LCA existing between node", n1, "and node", n2
      lca = None
      return lca
  print "The LCA node is", lca
  return lca


#Case 1
print "Case 1"
question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
#3

#Case 2
print "Case 2"
question4([[0,0,0,0,0,0,0],[1,0,1,0,0,0,0],[0,0,0,0,0,0,0],\
           [0,0,0,1,0,0,1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],4,2,5)
#4

#Case 3
print "Case 3"
question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,0,2)
#None


#==============================================================================
# Question 5
# Find the element in a singly linked list that's m elements from the end. For 
# example, if a linked list has 5 elements, the 3rd element from the end is the 
# 3rd element. The function definition should look like question5(ll, m), where 
# ll is the first node of a linked list and m is the "mth number from the end". 
# You should copy/paste the Node class below to use as a representation of a node
# in the linked list. Return the value of the node at that position.
#==============================================================================

def question5(ll, m):
  class Node(object):
    def __init__(self, data):
      self.data = data
      self.next = None  
      
  class LinkedList:
 
    # Function to initialize head
    def __init__(self):
      self.head = None
 
    # Function to insert a new node at the beginning
    def insert(self, new_data):
      # create a new node
      new_node = Node(new_data)
      # create ref point for the new node
      new_node.next = self.head
      # change head of the linked list to the new node
      self.head = new_node
    # Function to get Nth node from the end
    def printNthFromLast(self, m):
      main_ptr = self.head
      ref_ptr = self.head 
   
      count = 0
      if self.head is not None:
        while count < m:
          if ref_ptr is None:
            print "%d is greater than the number of nodes in the list" %m
            return

          ref_ptr = ref_ptr.next
          count += 1

      while ref_ptr is not None:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next