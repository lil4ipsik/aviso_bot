call venv/Scripts/activate.bat
call .venv/Scripts/activate.bat


python -m nuitka --follow-imports --onefile --include-data-files=windows/icon.ico=windows/icon.ico --disable-console --enable-plugin=pyside6 --output-dir=build --product-name="Aviso Bot" --windows-icon-from-ico=windows/icon.ico --product-version=0.0.1 -o "aviso-bot" .\main.py

pause