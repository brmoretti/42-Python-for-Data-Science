from load_image import ft_load


print(ft_load("landscape.jpg"))
# print(ft_load("animal.jpeg"))
# print(ft_load(""))
# print(ft_load("hello.txt"))

# # No permission test:
# import os

# file_path = "landscape.jpg"
# os.chmod(file_path, 0o200)

# print(ft_load("landscape.jpg"))

# os.chmod(file_path, 0o644)
