import os
import sys
import time
import webbrowser

# ANSI Color Codes for Terminal Styling
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BOLD = "\033[1m"
RESET = "\033[0m"


def print_banner():
    banner = f"""
{MAGENTA}{BOLD}
  =============================================================
  |                                                           |
  |   🎂  ✨  HAPPY    BIRTHDAY     PAYEL  ✨  🎂           |
  |                                                           |
  ============================================================={RESET}
    """
    print(banner)


def animate_cake():
    frames = [
        f"{YELLOW}          (  )  (  )  (  )\n          || || || ||\n        ===============\n       |   HAPPY BD!   |\n       ================={RESET}",
        f"{YELLOW}          (*) (*) (*) (*)\n          || || || ||\n        ===============\n       |   HAPPY BD!   |\n       ================={RESET}",
    ]
    print(f"\n{CYAN}Lighting up the birthday candles...{RESET}\n")
    for _ in range(4):
        for frame in frames:
            sys.stdout.write("\r" + frame)
            sys.stdout.flush()
            time.sleep(0.3)
    print("\n")


def launch_web_card():
    html_file = "index.html"
    file_path = os.path.abspath(html_file)

    if os.path.exists(file_path):
        print(
            f"{GREEN}{BOLD}🚀 Launching your interactive web card in the browser...{RESET}"
        )
        webbrowser.open(f"file://{file_path}")
    else:
        print(
            f"{YELLOW}⚠️  Could not find 'index.html'. Make sure it's in the same folder!{RESET}"
        )


if __name__ == "__main__":
    # Clear terminal screen
    os.system("cls" if os.name == "nt" else "clear")

    print_banner()
    animate_cake()
    time.sleep(1)
    launch_web_card()
    print(
        f"\n{CYAN}✨ Hope you have a wonderful year filled with success and happiness! ✨{RESET}\n"
    )