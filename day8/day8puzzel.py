import pandas as pd
import numpy as np

#part 1

Tree= open("day8\data8.txt").read().split("\n")
Tree= pd.DataFrame([[int(t) for t in l] for l in Tree])

Tree_top= Tree.gt(Tree.expanding().max().shift(1).fillna(-1))
Tree_left= Tree.T.gt(Tree.T.expanding().max().shift(1).fillna(-1)).T
Tree_bottom= Tree.iloc[::-1, :].gt(Tree.iloc[::-1, :].expanding().max().shift(1).fillna(-1)).iloc[::-1, :]
Tree_right= Tree.T.iloc[::-1, :].gt(Tree.T.iloc[::-1, :].expanding().max().shift(1).fillna(-1)).iloc[::-1, :].T

#part 2

highest_score= Tree.copy()
for y in Tree.index:
    for x in Tree.columns:
       highest_score.iloc[y, x]= np.prod([line.expanding().max().lt(Tree.iloc[y,x]).sum() + \
                                    int(line.max() >= Tree.iloc[y,x]) for line in \
                                    [Tree.iloc[:y,x].iloc[::-1],Tree.iloc[y+1:,x],Tree.iloc[y,:x].iloc[::-1],Tree.iloc[y,x+1:]]])

#solution

print("part1:",(Tree_top | Tree_left | Tree_bottom | Tree_right ).sum().sum())
print("part2:",highest_score.max().max())

