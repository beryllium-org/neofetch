rename_process("neofetch")

vr("ramt", gc.mem_alloc() + gc.mem_free())

try:
    import espidf

    vr("idftotal", espidf.heap_caps_get_total_size())
    if vr("idftotal") > vr("ramt"):
        vr("ramt", vr("idftotal"))
    vrd("idftotal")
    del espidf
except ImportError:
    pass

gc.collect()
gc.collect()
gc.collect()
gc.collect()

vr(
    "raml",
    "{}KiB / {}KiB".format(
        trunc((vr("ramt") - gc.mem_free()) / 1024),
        int(vr("ramt") / 1024),
    ),
)

vr("size", term.detect_size(3))
vr("lomg", vr("size")[1] > 50)
vr("time", int(pv[0]["uptimee"] + time.monotonic()))
vr("ustr", "")
vr("hr", vr("time") // 3600)  # Take out the hours
vrm("time", vr("hr") * 3600)
vr("min", vr("time") // 60)  # Take out the minutes
vrm("time", vr("min") * 60)
if vr("hr") > 0:
    vrp("ustr", str(vr("hr")) + " hours, ")
if vr("min") > 0 and (vr("lomg") or not vr("hr")):
    vrp("ustr", str(vr("min")) + " minutes, ")
if vr("time") > 0 and (vr("lomg") or not (vr("hr") or vr("min"))):
    vrp("ustr", str(vr("time")) + " seconds")
else:
    vr("ustr", vr("ustr")[:-2])

if vr("lomg"):
    vr("cpul", str(platform))
    vrp("cpul", f" (1) @ {trunc(cpu.frequency / 1000000)}Mhz")

be.api.subscript("/bin/neofetch/logo.py")
be.api.subscript("/bin/neofetch/texts.py")

for pv[get_pid()]["i"] in range(0, max(len(vr("logo")), len(vr("tex")))):
    try:
        vr("ansiless", vr("logo")[vr("i")])
        for pv[get_pid()]["j"] in [
            colors.black_t,
            colors.red_t,
            colors.green_t,
            colors.yellow_t,
            colors.blue_t,
            colors.magenta_t,
            colors.white_t,
            colors.cyan_t,
            colors.be_main,
            colors.endc,
        ]:
            vr("ansiless", vr("ansiless").replace(vr("j"), ""))
        term.nwrite(vr("logo")[vr("i")] + ((vr("sep") - len(vr("ansiless"))) * " "))
    except IndexError:
        term.nwrite(vr("sep") * " ")

    try:
        term.nwrite(vr("tex")[vr("i")])
    except IndexError:
        pass
    term.write()
