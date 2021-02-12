"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""
#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from setuptools import setup

APP = ['password_locker.py']
DATA_FILES = ['clave.key','passwords.key','xd.png','candado.png']
OPTIONS = {
'iconfile':'candado.icns',
"plist":{"CFBundleShortVersionString":"0.1.0",
"CFBundleName":"password secure 🔒"},
"packages":["cryptography","tkinter","sys","os","pyperclip"]}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requieres=["cryptography","tkinter","sys","os","pyperclip"]
)