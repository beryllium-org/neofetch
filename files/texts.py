vr(
    "tex",
    [
        (
            colors.yellow_t
            + be.based.system_vars["USER"]
            + "@"
            + be.based.system_vars["HOSTNAME"]
            + colors.endc
        ),
        "---------",
        (
            colors.yellow_t
            + "Kernel"
            + colors.endc
            + ": "
            + (colors.be_main if vr("lomg") else colors.yellow_t)
            + (
                be.based.system_vars["VERSION"]
                if vr("lomg")
                else be.based.system_vars["VERSION"][
                    : be.based.system_vars["VERSION"].find("-")
                ]
            )
            + colors.endc
        ),
        (colors.yellow_t + "Host" + colors.endc + ": " + be.based.system_vars["BOARD"]),
        (
            colors.yellow_t
            + "CircuitPython"
            + colors.endc
            + ": "
            + be.based.system_vars["IMPLEMENTATION"]
        ),
        "{}Uptime{}: {}".format(colors.yellow_t, colors.endc, vr("ustr")),
        f"{colors.yellow_t}Packages{colors.endc}: "
        + str(len(listdir(pv[0]["root"] + "/etc/jpkg/Installed")))
        + " (jpkg)",
        "{}Resolution:{} {}x{}".format(
            colors.yellow_t, colors.endc, vr("size")[1], vr("size")[0]
        ),
    ],
)
if vr("lomg"):
    vrp(
        "tex",
        [
            "{}CPU{}: {}".format(colors.yellow_t, colors.endc, vr("cpul")),
            "{}Terminal{}: {}".format(
                colors.yellow_t, colors.endc, pv[0]["console_active"]
            ),
        ],
    )
vrp(
    "tex",
    [
        "{}{}Memory{}: {}".format(
            colors.yellow_t, "System " if vr("lomg") else "", colors.endc, vr("raml")
        ),
    ],
)

if vr("lomg"):
    vrp(
        "tex",
        [
            "",
            (
                f"{colors.black_t}███{colors.endc}{colors.red_t}███{colors.endc}"
                + f"{colors.green_t}███{colors.endc}{colors.yellow_t}███{colors.endc}"
                + f"{colors.blue_t}███{colors.endc}{colors.magenta_t}███{colors.endc}"
                + f"{colors.cyan_t}███{colors.endc}{colors.white_t}███{colors.endc}"
            ),
            (
                f"{colors.black_t}███{colors.endc}"
                + f"{colors.red_t}███{colors.endc}{colors.green_t}███{colors.endc}"
                + f"{colors.yellow_t}███{colors.endc}{colors.blue_t}███{colors.endc}"
                + f"{colors.magenta_t}███{colors.endc}{colors.cyan_t}███{colors.endc}"
                + f"{colors.white_t}███{colors.endc}"
            ),
        ],
    )
