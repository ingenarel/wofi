import subprocess, os
x = {
    "   Vesktop": "vesktop",
    "󰙯   Vesktop Start Minimized": "vesktop --start-minimized",
    "   Discordo": "killall electron & hyprctl dispatch exec \"[float; size 90% 90%; center]\" 'kitty -e discordo --token",
    "󰋾   Instagram": "hyprctl dispatch exec \"[float; size 90% 90%; center; fakefullscreen]\" 'mullvad-browser --new-window www.instagram.com'"
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
