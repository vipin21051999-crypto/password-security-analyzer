"""
SecureCheck — Advanced Password Security Analyzer
Main Entry Point and Application Launcher.

Author: BCA Cybersecurity Portfolio Project
License: MIT
"""

import sys
import os
from pathlib import Path
import customtkinter as ctk

# Ensure root directory is in python search path
root_dir = Path(__file__).parent
sys.path.insert(0, str(root_dir))

from ui.dashboard import SecureCheckDashboard
from utils.theme import BG_DARK


def main():
    # Configure CustomTkinter settings
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")

    # Create root CTk window
    app = ctk.CTk()
    app.title("SecureCheck — Advanced Password Security Analyzer")
    app.geometry("1120x760")
    app.minsize(1000, 680)
    app.configure(fg_color=BG_DARK)

    # Set Window Icon if logo exists
    logo_path = root_dir / "assets" / "logo.png"
    if logo_path.exists():
        try:
            # On Windows, try loading icon
            app.iconbitmap(default=None)
        except Exception:
            pass

    # Instantiate Main Dashboard
    dashboard = SecureCheckDashboard(app)

    # Start Tkinter Event Loop
    app.mainloop()


if __name__ == "__main__":
    main()
