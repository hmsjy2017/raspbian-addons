#!/usr/bin/env python3
import os
import base64
import platform
import argparse

arch = platform.machine()
   
def logo():
    print(" ____                 _     _                  _       _     _                  ")
    print("|  _ \ __ _ ___ _ __ | |__ (_) __ _ _ __      / \   __| | __| | ___  _ __  ___  ")
    print("| |_) / _` / __| '_ \| '_ \| |/ _` | '_ \    / _ \ / _` |/ _` |/ _ \| '_ \/ __| ")
    print("|  _ < (_| \__ \ |_) | |_) | | (_| | | | |  / ___ \ (_| | (_| | (_) | | | \__ \ ")
    print("|_| \_\__,_|___/ .__/|_.__/|_|\__,_|_| |_| /_/   \_\__,_|\__,_|\___/|_| |_|___/ ")
    print("               |_|                                                              ")

    copyright_title = 'ICAgICAgICAgICAgICAgICAgIEFQVCByZXBvc2l0b3J5IGZvciBleHRyYSBSUGkgc29mdHdhcmU='
    copyright_url = 'aHR0cHM6Ly9naXRodWIuY29tL2NodW5reS1taWxrL3Jhc3BiaWFuLWFkZG9ucz09'
    print('')
    print(base64.b64decode(copyright_title).decode('utf-8'))
    print(base64.b64decode(copyright_url).decode('utf-8'))
    print('Choose a mirror:\n')
    print(' 1.OSDN (Main Server, USA)          2.xTom (California, USA)')
    print(' 3.GigeNET (California, USA)        4.Constant ( New Jersey, USA)')
    print(' 5.Purdue (Indiana, USA)            6.Princeton (New Jersey, USA)')
    print(' 7.Tsinghua (Beijing, China)        8.BFSU (Beijing, China)')
    print(' 9.SJTU (Shanghai, China)          10.NJU (Nanjing, China)')
    print('11.xTom (Hong Kong, China)         12.NCHC (Taiwan, China) ')
    print('13.IIJ (Osaka, Japan)              14.JAIST (Nomi, Japan)')
    print('15.YMU (Yamagata, Japan)           16.UME (Umeå, Sweden)')
    print('17.RWTH Aachen (NRW, Germany)      18.Dotsrc (Aalborg, Denmark)')
    print('19.Onet (Krakow, Poland)           20.Liquid Telecom (Nairobi, Kenya)\n')
    print('Other options: ')
    print('21.Remove                          22.Exit')
    print('')
    return copyright_title, copyright_url

def add_gpg_key():
    print('Installing GnuPG...')
    os.system('sudo apt update && sudo apt install -y gnupg || error "Failed to install GnuPG!" ')
    print('Adding GPG key...')
    os.system('wget -qO- https://chunky-milk.github.io/raspbian-addons/KEY.gpg | sudo apt-key add - || error "Failed to add GPG key!"')
    print('Creating package list... || error "Failed to create package list!"')

def update():
    print('Updating APT lists...')
    os.system('sudo apt update || error "Failed to update APT lists!"')
    print('Done!')


if __name__ == "__main__":
    copyright = logo()

    if copyright[0][10:13] != 'AgI' or copyright[1][13:16] != 'XRo':
        print('Verification failed! Exit.')
        os._exit(0)

    if arch != 'aarch64' or arch != 'armv7l':
        print('This script is only intended to run on ARM devices.\n')
        os._exit(0)


    try:
        option = input('\nPlease select the action to be performed: ')
    except  EOFError: 
        pass

    if int(option) == 1:
        add_gpg_key()
        os.system('echo "deb http://storage.osdn.net/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()
        

    elif int(option) == 2:
        add_gpg_key()
        os.system('echo "deb https://mirrors.xtom.com/osdn/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 3:
        add_gpg_key()
        os.system('echo "deb https://mirrors.gigenet.com/OSDN/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 4:
        add_gpg_key()
        os.system('echo "deb https://osdn.mirror.constant.com/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 5:
        add_gpg_key()
        os.system('echo "deb https://plug-mirror.rcac.purdue.edu/osdn/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 6:
        add_gpg_key()
        os.system('echo "deb https://mirror.math.princeton.edu/pub/osdn/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 7:
        add_gpg_key()
        os.system('echo "deb https://mirrors.tuna.tsinghua.edu.cn/osdn/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 8:
        add_gpg_key()
        os.system('echo "deb https://mirrors.bfsu.edu.cn/osdn/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 9:
        add_gpg_key()
        os.system('echo "deb https://mirror.sjtu.edu.cn/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 10:
        add_gpg_key()
        os.system('echo "deb https://mirrors.nju.edu.cn/osdn/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 11:
        add_gpg_key()
        os.system('echo "deb https://mirror.xtom.com.hk/osdn/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 12:
        add_gpg_key()
        os.system('echo "deb https://free.nchc.org.tw/osdn/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 13:
        add_gpg_key()
        os.system('echo "deb https://ftp.iij.ad.jp/pub/osdn.jp/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 14:
        add_gpg_key()
        os.system('echo "deb https://ftp.jaist.ac.jp/pub/sourceforge.jp/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 15:
        add_gpg_key()
        os.system('echo "deb https://ymu.dl.osdn.jp/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 16:
        add_gpg_key()
        os.system('echo "deb https://ftp.acc.umu.se/mirror/osdn.net/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 17:
        add_gpg_key()
        os.system('echo "deb http://ftp.halifax.rwth-aachen.de/osdn/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 18:
        add_gpg_key()
        os.system('echo "deb http://mirrors.dotsrc.org/osdn/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 19:
        add_gpg_key()
        os.system('echo "deb http://ftp.onet.pl/pub/mirrors/sourceforge.jp/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 20:
        add_gpg_key()
        os.system('echo "deb http://mirror.liquidtelecom.com/osdn/storage/g/r/ra/raspbian-addons/debian buster main" | sudo tee /etc/apt/sources.list.d/rpirepo.list || error "Failed to create package list!"')
        update()

    elif int(option) == 21:
        print('Removing package list... || error "Failed to remove package list!"')
        os.system('sudo rm /etc/apt/sources.list.d/rpirepo.list')
        print('Done!')

    elif int(option) == 22:
        os._exit(0)
    else:
        print('Illegal input option. Please re-enter.')
        