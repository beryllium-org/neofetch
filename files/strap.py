for i in ["neofetch.lja", "neofetch.py"]:
    shutil.copy(i, path.join(root, "bin", i))

shutil.copy("neofetch.man", path.join(root, "usr/share/man", "neofetch.man"))

be.api.setvar("return", "0")
