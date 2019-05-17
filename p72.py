from collections import defaultdict, Counter


def find_largest_value_backtrack(s, edges):
    nodes = defaultdict(list) # could build adjacency list using list
    for start, end in edges:
        nodes[start].append(end)

    def helper(start, visited, chars):
        if start not in nodes:
            return max(*chars.values()) # we could keep a running max
        else:
            m = 0
            for dest in nodes[start]:
                if dest in visited:
                    return None
                else:
                    visited.add(dest)
                    chars[s[dest]] += 1
                    val = helper(dest, visited, chars)
                    if val is None:
                        return None
                    m = max(val, m)
                    chars[s[dest]] -= 1
                    visited.remove(dest)
            return m

    m = 0
    for node in nodes.keys():
        chars = defaultdict(int)
        chars[s[node]] += 1
        val = helper(node, set([node]), chars)
        if val is None:
            return None
        m = max(val, m)

    return m


def find_largest_value_backtrack_golf(s, edges): # not tested
    nodes = defaultdict(list)
    for start, end in edges:
        nodes[start].append(end)

    def helper(cur=None, visited=None, cnt=None):
        dest, val = nodes[cur] if cur is not None else nodes.keys(), 0
        if not dest:
            return cnt.most_common(1)[0][1]
        for next in dest:
            if next in visited:
                raise ValueError("Next node is already visited. Infinite loop")
            visited.add(next)
            cnt[s[next]] += 1
            val = max(val, helper(next, visited, cnt))
            cnt[s[next]] -= 1
            visited.remove(next)
        return val

    try:
        return helper(visited=set(), cnt=Counter())
    except ValueError:
        return None 


print(find_largest_value_backtrack("ABACA", [(0, 1), (0, 2), (2, 3), (3, 4)]))
print(find_largest_value_backtrack("A", [(0, 0)]))

def find_largest_value_dfs(s, edges):
    nodes = defaultdict(list)
    for start, end in edges:
        nodes[start].append(end)

    m = 0 
    for node in nodes.keys():
        stack = [(s[node], set([node]), node)]
        while stack:
            path, visited, cur = stack.pop()
            m = max(m, Counter(path).most_common(1)[0][1])
            if cur not in nodes:
                continue
            for dest in nodes[cur]:
                if dest in visited:
                    return None 
                stack.append((path + s[dest], visited.union([dest]), dest))

    return m 


print(find_largest_value_dfs("ABACA", [(0, 1), (0, 2), (2, 3), (3, 4)]))
print(find_largest_value_dfs("A", [(0, 0)]))

def find_largest_value_dp(s, edges): # starred, backtrack keeps check on the paths and dp trims them further
    nodes = defaultdict(list)
    for start, end in edges:
        nodes[start].append(end)

    cache = [[0] * 26 for _ in range(len(s) + 1)]

    def helper(cur=None, visited=None):
        if cur in nodes or cur is None:
            dest, cur = (nodes[cur], cur) if cur is not None else (nodes.keys(), len(s))
            
            for neighbour in dest:
                if neighbour in visited:
                    raise ValueError("Infinite loop.")
                if not max(cache[neighbour]):
                    visited.add(neighbour)
                    helper(neighbour, visited)
                    visited.remove(neighbour)
                for i in range(26):
                    cache[cur][i] = max(cache[neighbour][i], cache[cur][i])
        
        if cur != len(s):
            cache[cur][ord(s[cur]) - ord('A')] += 1
            
    try:
        helper(cur=None, visited=set())
        return max(cache[len(s)])
    except ValueError:
        return None 
                

print(find_largest_value_dp("ABACA", [(0, 1), (0, 2), (2, 3), (3, 4)]))
print(find_largest_value_dp("A", [(0, 0)]))


    
    

# prac
# import collections 
# def max_path_val(s, edges):
#     nodes = collections.defaultdict(list)
#     for start, end in edges:
#         nodes[start].append(end)

#     max_val = 0 
#     for node in nodes.keys():
#         stack = [(s[node], set([node]), node)]
#         while stack:
#             path, visited, cur = stack.pop()
#             if dest not in nodes:
#                 max_val = max(max_val, collections.Counter(path).most_common(1)[0][1])
#                 continue
#             for dest in nodes[cur]:
#                 if dest in visited:
#                     return None
#                 stack.append((path + s[dest], visited.union([dest]), dest))
    
#     return max_val
                