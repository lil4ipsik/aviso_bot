call venv/Scripts/activate.bat
call .venv/Scripts/activate.bat


python -m nuitka --onefile --include-data-files=windows/icon.ico=windows/icon.ico --include-data-files=res/version.json=res/version.json --deployment --disable-console --enable-plugin=pyside6 --output-dir=build --product-name="Aviso Bot" --windows-icon-from-ico=windows/icon.ico --product-version=0.0.0.5 -o "aviso bot" .\main.py

pause