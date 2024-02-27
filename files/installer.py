for pv[get_pid()]["filee"] in ["neofetch.lja", "neofetch.py"]:
    be.based.run("cp " + vr("filee") + " /bin/" + vr("filee"))

be.based.run("cp neofetch.man /usr/share/man/neofetch.man")

be.api.setvar("return", "0")
