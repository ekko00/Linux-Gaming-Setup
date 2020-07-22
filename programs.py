from clint.textui import colored
import os, distro,sys,
import addRepo

def WINE(dist):
	if dist == "arch":
		print('''WINE allows you to run Windows software in other OS, like Linux.''')
		print(colored.green("Installing wine dependencies"))
		os.system("sudo pacman -S wine-staging giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader --needed")
	elif dist =="ubuntu":
		print('''WINE allows you to run Windows software in other OS, like Linux.''')
		print(colored.green("Enabling 32-bit architecture"))
		os.system("sudo dpkg --add-architecture i386 ")
		print(colored.green("Adding repository key for WINE"))
		os.system("wget -nc https://dl.winehq.org/wine-builds/winehq.key")
		os.system("sudo apt-key add winehq.key")
		codename = distro.linux_distribution()[2].lower()		
		print(colored.green("Adding repository"))
		os.system("sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ {} main'".format(codename))
		print(colored.green("Updating packages, installing wine and wine dependencies"))
		os.system("sudo apt-get update")
		os.system("sudo apt-get install --install-recommends wine-stable")
		# FIXME: Add error handler for this
		op = input("Did you received this error? -> The following packages have unmet dependencies [Y/N] -> ")
		if op == "Y" or op == "y":
			print(colored.green("Executing alternative command for solve that error"))
			os.system("sudo apt-get install --install-recommends winehq-stable wine-stable wine-stable-i386 wine-stable-amd64")
		elif op == "N" or op == "n":
			print(colored.green("Proceeding to continue"))
		else:
			print(colored.red("Wrong option"))
				
		os.system("sudo apt-get install libgnutls30:i386 libldap-2.4-2:i386 libgpg-error0:i386 libxml2:i386 libasound2-plugins:i386 libsdl2-2.0-0:i386 libfreetype6:i386 libdbus-1-3:i386 libsqlite3-0:i386")
		
	elif dist == "debian":
		print('''WINE allows you to run Windows software in other OS, like Linux.''')
		print(colored.green("Enabling 32-bit architecture"))
		os.system("sudo dpkg --add-architecture i386")
		os.system("wget -nc https://dl.winehq.org/wine-builds/Release.key")
		os.system("sudo apt-key add Release.key")
		addRepo.debianRepo()
	else:
		print("FIXME: Add more distros?")

def Lutris(dist):
	if dist == "arch":
		print(colored.green("Installing lutris"))
		os.system("sudo pacman -S lutris --needed")
	elif dist == "ubuntu":
		print(colored.green("Adding lutris repository"))
		os.system("sudo add-apt-repository ppa:lutris-team/lutris")
		os.system("sudo apt-get update")
		os.system("sudo apt-get install lutris")
	elif dist == "debian":
		os.system('echo "deb http://download.opensuse.org/repositories/home:/strycore/Debian_10/ ./" | sudo tee /etc/apt/sources.list.d/lutris.list')
		os.system("wget -q https://download.opensuse.org/repositories/home:/strycore/Debian_10/Release.key -O- | sudo apt-key add -")
		os.system("sudo apt-get update")
		os.system("sudo apt-get install lutris")
	else:
		print("FIXME: Add more distros?")


def GOverlwMango(dist):
	if dist == "arch":
		print(colored.green("Updating packages"))
		os.system("sudo pacman -Sy")
		print(colored.green("Enabling multilib"))
		os.system("sudo python3 enableMultilib.py program")

		print(colored.green("Installing GOverlay, optional and MangoHUD"))
		# GOverlay
		if os.WEXITSTATUS(os.system("yay goverlay")) == 127:
			goverlay = input(print("Seems like you don't have yay installed (it's an AUR helper for install packages from the AUR), proceed to install yay? [Y/N] ->"))
			if goverlay == "y" or goverlay == "Y":
				if os.WEXITSTATUS(os.system("git clone https://aur.archlinux.org/yay.git")) == 127:
					git = input(print(colored.red("Cannot found Git, Git is needed for install some programs, proceed to install Git? [Y/N]")))
					if git == "y" or git=="Y":
						Git("arch")
						os.system("git clone https://aur.archlinux.org/yay.git")
						os.chdir("yay")
						os.system("makepkg -si")
					elif git == "N" or git == "n":
						sys.exit("cancelled installation")
					else:
						print("Wrong option!")
				os.system("yay goverlay")
			elif goverlay == "n" or goverlay == "N":
				sys.exit("Installation cancelled")
			else:
				print("Wrong option!")
		os.system("sudo pacman -S mesa-demos lib32-mesa-demos vulkan-tools --needed" )
		os.system("yay mangohud")
	elif dist == "ubuntu":
		mHUDGOInst()		
	elif dist == "debian":
		mHUDGOInst()
	else:
		print("FIXME: Add more distros?")


def mHUDGOInst():
	if os.path.isfile("/usr/bin/mangohud"):
		print(colored.green("MangoHud already installed, proceeding to install GOverlay"))
		if os.path.isfile("/usr/bin/goverlay"):
			print(colored.green("GOverlay already installed"))
		else:
			os.system("mkdir GOverlay")
			if os.path.exists("./GOverlay"):
				print(colored.green("Installing GOverlay..."))
				os.chdir("./GOverlay")
				# FIXME: Add an automatic update for GOverlay
				os.system("wget https://github.com/benjamimgois/goverlay/releases/download/0.3.1/goverlay_0_3_1.tar.gz")
				os.system("tar -xf goverlay_0_3_1.tar.gz")
				os.system("sudo cp goverlay /usr/bin/")
				if os.path.isfile("/usr/bin/goverlay"):
					print(colored.green("GOverlay installed succesfuly"))
				else:
					print(colored.red("Something went wrong installing GOverlay, please try again, or report the issue"))
			else:
				print(colored.red("Cannot found GOverlay directory"))
				# FIXME: Add error handler
	else:
		print(colored.green("Installing MangoHUD..."))
		os.system("mkdir MangoHUD")
		if os.path.exists("./MangoHUD"):
			os.chdir("./MangoHUD")
			# FIXME: Add an automatic update for mangohud
			os.system("wget https://github.com/flightlessmango/MangoHud/releases/download/v0.3.1/MangoHud-v0.3.1.tar.gz")
			os.system("tar -xf MangoHud-v0.3.1.tar.gz")
			if os.path.exists("./MangoHud"):
				os.chdir("./MangoHud")
				os.system("./mangohud-setup.sh install")
				if os.path.isfile("/usr/bin/mangohud"):
					print(colored.green("MangoHUD installed succesfuly"))
					mHUDGOInst()
				else:
					print(colored.red("Something went wrong installing MangoHUD, please try again, or report the issue"))
					# FIXME: Add error handler
			else:
				print(colored.red("Cannot found MangoHud directory"))
		else:
			print(colored.red("Cannot found MangoHUD directory"))

def Steam(dist):
	if dist == "arch":
		eB.pacmanConf("program")
		os.system("sudo pacman -S steam --needed")
	elif dist == "ubuntu":
		os.system("sudo apt install steam-installer")
	else:
		print(colored.red("This shouldn't happen"))

def feralGamemode(dist):
	if dist == "arch":
		os.system("sudo pacman -S meson systemd git dbus")
		cloneFeralGamemode("arch")
	elif dist == "ubuntu":
		os.system("sudo apt install meson libsystemd-dev pkg-config ninja-build git libdbus-1-dev libinih-dev")
		cloneFeralGamemode("ubuntu")
	else:
		print("wrong distro")


def Git(dist):
	if dist == "arch":
		os.system("sudo pacman -S git")
	elif dist == "ubuntu":
		os.system("sudo apt update")
		os.system("sudo apt install git")
	else:
		print(colored.red("wrong distro"))

def cloneFeralGamemode(dist):
		if os.path.exists("./Gamemode"):
			os.chdir("./Gamemode")
		else:
			os.system("mkdir Gamemode")
			os.chdir("./Gamemode")
		if os.WEXITSTATUS(os.system("git clone https://github.com/FeralInteractive/gamemode.git")) == 127:
			git = input(print(colored.red("Cannot found Git, Git is needed for install some programs, proceed to install Git? [Y/N]")))
			if git == "y" or git == "Y":
				Git(dist)
				os.system("git clone https://github.com/FeralInteractive/gamemode.git")
			elif git == "n" or git == "N":
				sys.exit("Installation cancelled")
		os.chdir("gamemode")
		os.system("git checkout 1.5.1")
		os.system("sudo chmod +x bootstrap.sh")
		os.system("./bootstrap.sh")
		

