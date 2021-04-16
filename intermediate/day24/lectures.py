# file = open("lectures.txt")
# contents = file.read()

# print(contents)
# # Recommended to close the file once
# # you don't need it anymore
# file.close()

# # Or you can use a with statement
# # it will automatically close after
# # the with statement is complete
# with open("lectures.txt") as file:
#     contents = file.read()
#     print(contents)

# # Writing to the file
# # w to replace all content
# # a to append content
# with open("lectures.txt", mode="a") as file:
#     file.write("\nNew text.")

# Understanding Relative and Absolute File Paths
with open("./intermediate/day24/lectures.txt") as file:
    contents = file.read()
    print(contents)
