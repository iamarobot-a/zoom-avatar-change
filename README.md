# zoom-avatar-change
A script that updates your zoom avatar to a random background image
to a merged picture.
- foreground picture is maybe an image with transparent background
- background is anything from a random picture server
- JWT auth in zoom is planned to be deprecated in 2023. Watch for an update.
- Tested with Python 3.9.2 on Win10.

How to install
    needs python 3.9.2 (maybe other versions work but definitely 3+)
    for venv: python -m venv . 
    scripts/activate.bat
    pip install Pillow requests
    #(Pillow 9.1.1, requests 2.27.1)

How to configure
    Create a zoom app, and a JWT token at zoom app marketplace. Check the expiration date and increase it to a year or more.
    paste the token to avatar.py jwtToken 
    write your email to avatar.py userId

How to run
    Windows: Run avatar.bat (double click)
    Other OS: ...

Common issues
    ModuleNotFoundError: No module named 'PIL' - You did not run activate.py
    You may have to update "python" to "python3" in avatar.bat if it fails (remove exit to check error message)
    