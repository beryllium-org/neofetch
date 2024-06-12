be.based.run("mkdir /bin/neofetch")

be.based.run("cp neofetch.lja /bin/neofetch.lja")

for pv[get_pid()]["filee"] in ["logo.py", "main.py", "texts.py"]:
    be.based.run("cp " + vr("filee") + " /bin/neofetch" + vr("filee"))

be.based.run("cp neofetch.man /usr/share/man/neofetch.man")

be.api.setvar("return", "0")
