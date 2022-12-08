from numpy import array
from numpy import argwhere
from numpy import where

with open("input.txt") as file:
    data = file.read().splitlines()

data = [list(map(int, list(line))) for line in data]

trees = array(data)

column = trees[:, 0]

highest_score = 0
for line_number, line in enumerate(trees):
    for column_number, tree in enumerate(line):
        column = trees[:, column_number]
        xs_of_higher_trees = argwhere(column >= tree)
        x_index_of_our_tree = where(xs_of_higher_trees == [line_number])[0][0]
        if x_index_of_our_tree != 0:
            distance_to_a_higher_tree_upwards = line_number - xs_of_higher_trees[x_index_of_our_tree - 1][0]
        else:
            distance_to_a_higher_tree_upwards = line_number
        if x_index_of_our_tree != len(xs_of_higher_trees) - 1:
            distance_to_a_higher_tree_downwards = xs_of_higher_trees[x_index_of_our_tree + 1][0] - line_number
        else:
            distance_to_a_higher_tree_downwards = 99 - line_number - 1

        line = trees[line_number, :]
        ys_of_higher_trees = argwhere(line >= tree)
        y_index_of_our_tree = where(ys_of_higher_trees == [column_number])[0][0]
        if y_index_of_our_tree != 0:
            distance_to_a_higher_tree_leftwards = column_number - ys_of_higher_trees[y_index_of_our_tree - 1][0]
        else:
            distance_to_a_higher_tree_leftwards = column_number
        if y_index_of_our_tree != len(ys_of_higher_trees) - 1:
            distance_to_a_higher_tree_rightwards = ys_of_higher_trees[y_index_of_our_tree + 1][0] - column_number
        else:
            distance_to_a_higher_tree_rightwards = 99 - column_number - 1

        score = distance_to_a_higher_tree_leftwards * distance_to_a_higher_tree_rightwards * distance_to_a_higher_tree_upwards * distance_to_a_higher_tree_downwards
        if score > highest_score:
            highest_score = score

print(highest_score)
