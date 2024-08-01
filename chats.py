import subprocess, os
x = {
    "   Discord": "hyprctl dispatch exec discord",
    "󰙯  Discord Start Minimized": "hyprctl dispatch exec 'discord --start-minimized'",
    "    Discordo": "killall Discord & hyprctl dispatch exec \"[float; size 90% 90%; center]\" 'kitty -e discordo --token",
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
            "--width=200",
            "--height=150",
            "-b",
            "-d",
            "--prompt",
            "Chats"
            ),
        stdin=chosen.stdout,
        text=True
    )

for stuff in x:
    if stuff == launch.strip():
        if stuff[-8:] == "Discordo":
            with open(os.path.expanduser("~/.config/wofi/token"), "r") as file:
                token = file.read()
            os.system(f"{x[stuff]} {token}'")
            exit()
        else:
            os.system(x[stuff])
            exit()
