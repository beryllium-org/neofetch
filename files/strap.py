try:
    mkdir(path.join(root, "bin/neofetch"))
except FileExistsError:
    pass

shutil.copyfile("neofetch.lja", path.join(root, "bin", "neofetch.lja"))

for i in ["logo.py", "main.py", "texts.py"]:
    shutil.copyfile(i, path.join(root, "bin/neofetch", i))

shutil.copyfile("neofetch.man", path.join(root, "usr/share/man", "neofetch.man"))
