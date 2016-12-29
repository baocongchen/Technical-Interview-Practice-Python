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
question2('')
#There is no palindrome in the string
question2('h')
#There is no palindrome in the string
question2('hawls')
#There is no palindrome in the string
question2('noon')
#The longest palindrome is:  noon
question2('non')
#The longest palindrome is:  non
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
  def get_edge_list(self):
    edge_list = []
    for edge_object in self.edges:
      edge = (edge_object.value, edge_object.node_from.value, edge_object.node_to.value)
      edge_list.append(edge)
    return edge_list

  def get_adjacency_list(self):
    max_index = self.find_max_index()
    adjacency_list = [None] * (max_index + 1)
    for edge_object in self.edges:
      if adjacency_list[edge_object.node_from.value]:
        adjacency_list[edge_object.node_from.value].append((edge_object.node_to.value, edge_object.value))
      else:
        adjacency_list[edge_object.node_from.value] = [(edge_object.node_to.value, edge_object.value)]
    return adjacency_list

  def get_adjacency_matrix(self):
    max_index = self.find_max_index()
    adjacency_matrix = [[0 for i in range(max_index + 1)] for j in range(max_index + 1)]
    for edge_object in self.edges:
      adjacency_matrix[edge_object.node_from.value][edge_object.node_to.value] = edge_object.value
    return adjacency_matrix

  def find_max_index(self):
    max_index = -1
    if len(self.nodes):
      for node in self.nodes:
        if node.value > max_index:
          max_index = node.value
    return max_index
  return get_adjacency_list(G)

# I don't know how to answer question 3, can you explain what I should do to 
# answer the question.


#==============================================================================
# Question 4
# Find the least common ancestor between two nodes on a binary search tree. The
# least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be
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
  
def question4():
  return 
    
# I don't know how to answer question 4, can you explain what I should do to 
# answer the question.


#==============================================================================
# Question 5
# Find the element in a singly linked list that's m elements from the end. For 
# example, if a linked list has 5 elements, the 3rd element from the end is the 
# 3rd element. The function definition should look like question5(ll, m), where 
# ll is the first node of a linked list and m is the "mth number from the end". 
# You should copy/paste the Node class below to use as a representation of a node
# in the linked list. Return the value of the node at that position.
#==============================================================================

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None  
def question5():
  return
  
# I don't know how to answer question 5, can you explain what I should do to 
# answer the question.