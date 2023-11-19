# Basic program to hide your treasure using Lists.

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

map = [line1, line2, line3]

print("\nHiding your treasure! X marks the spot.")

position = input().lower()

reference_list = ["a", "b", "c"]

first_index = int(position[1]) - 1
second_index = reference_list.index(position[0])
map[first_index][second_index] = "X"

print(f"{line1}\n{line2}\n{line3}")