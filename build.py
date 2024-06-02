import os
import sys

from version import version
print(version(n=True))

def main():
    parameters = sys.argv[1:]
        
    if "-v" in parameters:
        print("Build with console enabled")
        os.system(f"nuitka --onefile --follow-imports --enable-plugin=pyqt6 -o aviso-bot-debug --output-dir=build --windows-icon-from-ico=./windows/icon.ico --include-data-files=./windows/icon.ico=windows/icon.ico --include-data-files=./res/version.json=res/version.json --deployment --company-name=Lil4ipsik --product-name=\"Aviso Bot (debug)\" --product-version={version(True)} main.py")
    elif "--linux" in parameters:
        print("Build for Linux")
        os.system(f"nuitka --onefile --follow-imports --enable-plugin=pyqt6 -o aviso-bot --output-dir=build --linux-onefile-icon=./windows/icon.ico --include-data-files=./linux/icon.png=linux/icon.png --include-data-files=./res/version.json=res/version.json --deployment --company-name=Lil4ipsik --product-name=\"Aviso Bot\" --product-version={version(True)} main.py")
    else:
        print("Build with console disabled (default)")
        os.system(f"nuitka --onefile --follow-imports --enable-plugin=pyqt6 -o aviso-bot --disable-console --output-dir=build --windows-icon-from-ico=./windows/icon.ico --include-data-files=./windows/icon.ico=windows/icon.ico --include-data-files=./res/version.json=res/version.json --deployment --company-name=Lil4ipsik --product-name=\"Aviso Bot\" --product-version={version(True)} main.py")
    
if __name__ == "__main__":
    main()