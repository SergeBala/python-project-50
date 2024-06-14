from gendiff import generate_diff

diff = generate_diff("./file1.json", "./file2.json")
print(diff)
diff = generate_diff("./file1.json", "./file1.json")
print(diff)
diff = generate_diff("./doesnt_exist.json", "./doesnt_exist_either.json")
print(diff)
diff = generate_diff("./empty.json", "./file1.json")
print(diff)
diff = generate_diff("./list.json", "./file1.json")
print(diff)
diff = generate_diff("./text", "./file1.json")
print(diff)
