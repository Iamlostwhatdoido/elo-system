import os

EXE_NAME = "Elo Sorter"
VERSION = "0.1.0"

MAIN_SCRIPT = "main"
ICON_FILE = "icon.ico"
RELEASE_DIR = "releases"

if not os.path.exists(f"./{RELEASE_DIR}"):
	os.mkdir(f"{RELEASE_DIR}")

if os.path.exists(f"./releases/{EXE_NAME} v{VERSION}.exe"):
	print(f"ERROR : Version {VERSION} already exists.")
else:
	command = f"python -m PyInstaller {MAIN_SCRIPT}.py " \
		f"--onefile --noconsole " \
		f"--icon {ICON_FILE} " \
		f"--distpath releases " \
		f'-n "{EXE_NAME} v{VERSION}"'

	print(command)
	os.system(command)

	os.system("rm -rf build")
	os.remove(f"{EXE_NAME} v{VERSION}.spec")