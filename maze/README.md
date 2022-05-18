# maze
Maze solving cli app
Using it is simple
```sh
python -m maze [file] --algorithm 'astar|bfs|dfs|greedy'
```
It generates a graph.txt that shows the path taken and the correct detected path.
It returs wether it can reach the target or not.
Start is from ? and end is at x.
You can put more than one start or end.It does not matter.It starts at the first found start and ends at the first ends found.
