import os, sys, glob, shutil

EXE_NAME = "Elo Sorter"
VERSION = "0.1.3"

MAIN_SCRIPT = "main"
ICON_FILE = "icon.ico"
RELEASE_DIR = "releases"
PUBLISH_DIR = "D:/[02] Code/06 Releases/elo-sorter" # dernière version, prête à l'emploi

if not os.path.exists(f"./{RELEASE_DIR}"):
	os.mkdir(f"{RELEASE_DIR}")

if os.path.exists(f"{PUBLISH_DIR}/{EXE_NAME} v{VERSION}.exe"):
	print(f"ERROR : Version {VERSION} already exists.")
else:
	command = f'"{sys.executable}" -m PyInstaller {MAIN_SCRIPT}.py ' \
		f"--onefile --noconsole " \
		f"--icon {ICON_FILE} " \
		f"--distpath {RELEASE_DIR} " \
		f'-n "{EXE_NAME} v{VERSION}"'

	print(command)
	os.system(command)

	shutil.rmtree("build", ignore_errors=True)
	os.remove(f"{EXE_NAME} v{VERSION}.spec")

	exe_path = f"{RELEASE_DIR}/{EXE_NAME} v{VERSION}.exe"
	if os.path.exists(exe_path):
		os.makedirs(PUBLISH_DIR, exist_ok=True)
		for old_exe in glob.glob(f"{PUBLISH_DIR}/{EXE_NAME} v*.exe"):
			os.remove(old_exe)
		shutil.move(exe_path, PUBLISH_DIR)
		print(f"Published to {PUBLISH_DIR}")
