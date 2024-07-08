#!/bin/bash

# Display options using Wofi
chosen=$(echo -e "Shutdown\nReboot\nHibernate\nSuspend" | wofi --width=190 --height=150 -b -d --prompt "Power Menu")

# Perform action based on choice
case "$chosen" in
    "Shutdown")
        systemctl poweroff
        ;;
    "Reboot")
        systemctl reboot
        ;;
    "Hibernate")
        systemctl hibernate
        ;;
    "Suspend")
        systemctl suspend
        ;;
esac

