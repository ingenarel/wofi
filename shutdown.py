import subprocess, os
x = {
    "⏻  Shutdown": "systemctl poweroff",
    "  Reboot": "systemctl reboot",
    "⏼  Hibernate": "systemctl hibernate",
    "󰤄  Suspend": "systemctl suspend",
    }

chosen = subprocess.Popen(
        (
            "echo",
            "-e",
            "".join(choice+"\n" for choice in x)[:-1]
        ),
        stdout=subprocess.PIPE
    )

launch = subprocess.check_output(
        (
            "wofi",
            "--width=190",
            "--height=150",
            "-b",
            "-d",
            "--prompt",
            "Power Menu"
            ),
        stdin=chosen.stdout
    )
for stuff in x:
    if stuff == str(launch)[2:-3]:
        os.system(x[stuff])
        break
