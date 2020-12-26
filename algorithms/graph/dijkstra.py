import heapq

def solution(graph, start):
    distances = {node: float('inf') for node in graph}