import subprocess, os
x = {
    "󰙯   Vesktop Start Minimized":  "hyprctl dispatch exec \"vesktop --start-minimized\"",
    "   Discordo":                 "killall electron & hyprctl dispatch exec \"[float; size 90% 90%; center]\" 'kitty -e discordo --token",
    "Minecraft":                    "hyprctl dispatch exec \"~/Downloads/prismlauncher/./PrismLauncher-Cracked-Linux-x86_64.AppImage\"",
    "Witcher 3":                    "cd /mnt/E/'New folder'/'The Witcher 3 - Wild Hunt'/bin/x64/ && wine witcher3.exe & disown",
    "Skyrim":                       "cd /mnt/D/skyrim && wine skse64_loader.exe & disown",
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
            "--height=180",
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
