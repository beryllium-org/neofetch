for i in ["neofetch.lja", "neofetch.py"]:
    shutil.copyfile(i, path.join(root, "bin", i))

shutil.copyfile("neofetch.man", path.join(root, "usr/share/man", "neofetch.man"))
