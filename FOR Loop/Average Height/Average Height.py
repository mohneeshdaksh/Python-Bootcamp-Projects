print("\n*AVERAGE HEIGHT CALCULATOR*")
heights = input("\nPlease enter heights (in cms) and separate them with single space:\n").split()
for n in range(0, len(heights)):
  heights[n] = int(heights[n])

total_height = 0
for height in heights:
  total_height += height

no_of_people = 0
for student in heights:
  no_of_people += 1

average_height = round(total_height / no_of_people)
print(f"\nAverage Height = {average_height}")

print("\nMore info:")
print(f"Total Height = {total_height}")
print(f"Number of people = {no_of_people}\n")