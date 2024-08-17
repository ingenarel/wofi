import subprocess, os
x = {
    "⏻  Shutdown": "systemctl poweroff",
    "󰚰  Update ⏻  Shutdown": "kitty -e paru -Syyu ; systemctl poweroff",
    "  Reboot": "systemctl reboot",
    "󰚰  Update   Reboot": "kitty -e paru -Syyu ; systemctl reboot",
    "⏼  Hibernate": "systemctl hibernate",
    "󰤄  Suspend": "systemctl suspend",
    "󰿅  Logout": "hyprctl dispatch exit 1",
    "󰷛  LockScreen": "hyprlock",
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
            "--width=13%",
            "--height=27%",
            "-b",
            "-d",
            "--prompt",
            "Power Menu"
            ),
        stdin=chosen.stdout,
        text=True
    )
for stuff in x:
    if stuff == launch.strip():
        os.system(x[stuff])
        break
