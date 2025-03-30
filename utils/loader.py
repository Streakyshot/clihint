from cheats import (
    cyber_recon,
    payload_crafting,
    git_version,
    linux_essentials,
    osint_tools,
    web_recon,
    networking,
    red_team_auto,
    terminal_fu
)

from cheats.programming import (
    python_cheats1,
    python_cheats2,
    python_cheats3,
    python_cheats4,
    python_cheats5,
    python_cheats6,
    python_cheats7,
    python_cheats8,
    python_cheats9,
    python_cheats10
)

def load_cheat_modules():
    all_python = (
        python_cheats1.cheats + python_cheats2.cheats + python_cheats3.cheats +
        python_cheats4.cheats + python_cheats5.cheats + python_cheats6.cheats +
        python_cheats7.cheats + python_cheats8.cheats + python_cheats9.cheats +
        python_cheats10.cheats
    )

    return {
        "Python Programming": all_python,
        "Cyber Recon": cyber_recon.cheats,
        "Payload Crafting": payload_crafting.cheats,
        "Git & Version Control": git_version.cheats,
        "Linux Essentials": linux_essentials.cheats,
        "OSINT Tools": osint_tools.cheats,
        "Web Recon & Enumeration": web_recon.cheats,
        "Networking & Sockets": networking.cheats,
        "Red Team Automation": red_team_auto.cheats,
        "Misc Terminal Fu": terminal_fu.cheats
    }
