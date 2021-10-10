import math


def rast(point_1, point_2):
    """ Возвращает расстояние между двумя пунктами """
    a = ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5
    return a
def kratput(toch:list=[(0,2),(2,5)]):
    """Печатает кратчайший путь"""
    pos = []
    full = []
    finish =[]

    for i in range(len(toch)):
        for j in range(len(toch)):
            pos.append(rast(toch[i],toch[j]))
        full.append(pos)
        pos = []
    che = bfs(full,0)
    print(che)
    print("Полный минимальный путь равен:",che[len(che)-1])






def bfs(graph, ver):
    visited = {ver}
    k=0

    T = [math.inf]*(len(graph))
    T[ver] =0
    while ver != -1:
        for j in get_link_ver(ver, graph):
            if j not in visited:
                w = T[ver] + graph[ver][j]
                T[j] = w
                k=ver
        ver = arg_min(T, visited)
        if ver > 0:
            visited.add(ver)
    last = max(T) + rast(graph[k],graph[0])
    T.append(last)
    return T



def arg_min(T, V):
    amin = -1
    m = max(T)
    for i, t in enumerate(T):
        for i,t in enumerate(T):
            if t< m and i not in V:
                m=t

                amin = i

        return amin
def get_link_ver(ver, graph):
    for i,weight in enumerate(graph[ver]):
        if weight > 0.0:
            yield i


kratput([(0,1),(1,4),(4,1),(5,5),(7,2)])



