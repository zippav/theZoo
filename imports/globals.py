#!/usr/bin/env python

    # Malware DB - the most awesome free malware database on the air
    # Copyright (C) 2014, Yuval Nativ, Lahad Ludar, 5Fingers

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <http://www.gnu.org/licenses/>.
import sys
import os
import random


class init:

    def init(self):
        # Global Variables
        version = "0.6.0 Moat"
        appname = "theZoo"
        codename = "Moat"
        authors = "Yuval Nativ, Lahad Ludar, 5fingers"
        licensev = "GPL v3.0"
        fulllicense = appname + " Copyright (C) 2014 " + authors + "\n"
        fulllicense += "This program comes with ABSOLUTELY NO WARRANTY; for details type '" + \
            sys.argv[0] + " -w'.\n"
        fulllicense += "This is free software, and you are welcome to redistribute it."

        usage = '\nUsage: ' + sys.argv[0] + \
            ' -s search_query -t trojan -p vb\n\n'
        usage += 'The search engine can search by regular search or using specified arguments:\n\nOPTIONS:\n   -h  --help\t\tShow this message\n   -t  --type\t\tMalware type, can be virus/trojan/botnet/spyware/ransomeware.\n   -p  --language\tProgramming language, can be c/cpp/vb/asm/bin/java.\n   -u  --update\t\tUpdate malware index. Rebuilds main CSV file. \n   -s  --search\t\tSearch query for name or anything. \n   -v  --version\tPrint the version information.\n   -w\t\t\tPrint GNU license.\n'

        conf_folder = 'conf'
        eula_file = conf_folder + '/eula_run.conf'
        maldb_ver_file = conf_folder + '/db.ver'
        giturl = 'https://github.com/ytisf/theZoo/blob/master'


##########################################################
class Completer:
    def __init__(self, commands):
        self.commands = commands
        self.prefix = None

    def complete(self, prefix, index):
        if prefix != self.prefix:
            self.matchingCommand = [w for w in self.commands if w.startswith(prefix)
                ]
            self.prefix = prefix
        try:
            return self.matchingCommand[index]
        except IndexError:
            return None
################################################################

class bcolors:
    PURPLE = ''
    BLUE = ''
    GREEN = ''
    YELLOW = ''
    RED = ''
    WHITE = ''
    if os.name is not 'nt':
        PURPLE = '\033[95m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        WHITE = '\033[0m'


class vars:
    version = "0.6.0 'Moat'"
    appname = "Malware DB"
    authors = "Yuval Nativ, Lahad Ludar, 5fingers"
    licensev = "GPL v3.0"

    ############ DEBUGGING ###############
    #### SET TO ZERO BEFORE COMMIT #######

        # DEBUG_LEVEL 0 = NO DEBUGGING
        # DEBUG_LEVEL 1 = DEBUG DOWNLOADS
        # DEBUG_LEVEL 2 = DEBUG SQL QUERIES
    DEBUG_LEVEL = 0

    fulllicense = appname + " Copyright (C) 2014 " + authors + "\n"
    fulllicense += "This program comes with ABSOLUTELY NO WARRANTY; for details type '" + \
        sys.argv[0] + " -w'.\n"
    fulllicense += "This is free software, and you are welcome to redistribute it."

    usage = '\nUsage: ' + sys.argv[0] + ' -s search_query -t trojan -p vb\n\n'
    usage += 'The search engine can search by regular search or using specified arguments:\n\nOPTIONS:\n   -h  --help\t\tShow this message\n   -t  --type\t\tMalware type, can be virus/trojan/botnet/spyware/ransomeware.\n   -p  --language\tProgramming language, can be c/cpp/vb/asm/bin/java.\n   -u  --update\t\tUpdate malware index. Rebuilds main CSV file. \n   -s  --search\t\tSearch query for name or anything. \n   -v  --version\tPrint the version information.\n   -w\t\t\tPrint GNU license.\n'

    # :todo: add filter usage

    column_for_pl = 6
    column_for_type = 2
    column_for_location = 1
    colomn_for_time = 7
    column_for_version = 4
    column_for_name = 3
    column_for_uid = 0
    column_for_arch = 8
    column_for_plat = 9
    column_for_vip = 10

    opts = [
        ("type", ("virus", "worm", "ransomware", "botnet", "apt", "rootkit", "trojan", "exploitkit", "dropper")),
        ("architecture", ("x86", "x64", "arm", "web")),
        ("platform", ("win32", "win64", "android", "ios", "mac", "*nix32", "*nix64")),
        ("language", ("c", "cpp", "asm", "bin", "java", "apk", "vb", "php"))]

    conf_folder = 'conf'
    eula_file = conf_folder + '/eula_run.conf'
    maldb_ver_file = conf_folder + '/db.ver'
    db_path = conf_folder + "/maldb.db"
    giturl_dl = 'https://github.com/ytisf/theZoo/raw/master/'
    giturl = 'https://github.com/ytisf/theZoo'

    with file(maldb_ver_file) as f:
        db_ver = f.read()

    # ASCII Art is a must...
    screen = random.randrange(1, 4)

    if screen is 1:
        maldb_banner = "\n"
        maldb_banner += "        sMMs              oMMy      \n"
        maldb_banner += "        :ooooo/        /ooooo:      \n"
        maldb_banner += "        ```+MMd````````hMMo```      \n"
        maldb_banner += "        oNNNMMMNNNNNNNNMMMNNNs      \n"
        maldb_banner += "     /oodMMdooyMMMMMMMMyoodMMdoo/   \ttheZoo " + version + "\n"
        maldb_banner += "  `..dMMMMMy. :MMMMMMMM/  sMMMMMm..`\t DB ver. " + db_ver + "\n"
        maldb_banner += "  dmmMMMMMMNmmNMMMMMMMMNmmNMMMMMMmmm\n"
        maldb_banner += "  NMMyoodMMMMMMMMMMMMMMMMMMMMdoosMMM\t" + giturl + "\n"
        maldb_banner += "  NMM-  sMMMNNNNNNNNNNNNNNNMMy  .MMM\n"
        maldb_banner += "  NMM-  sMMy``````````````sMMy  .MMM\n"
        maldb_banner += "  ooo.  :ooooooo+    +ooooooo/  `ooo\n"
        maldb_banner += "           /MMMMN    mMMMM+         \n"
        maldb_banner += "                                 Authors: " + authors + "\n"

    elif screen is 2:
        maldb_banner = "           ____.----. \n"
        maldb_banner += " ____.----'          \ \n"
        maldb_banner += "  \                    \ \ttheZoo " + version + "\n"
        maldb_banner += "    \          ____.----'`--.__ \t" + giturl + "\n"
        maldb_banner += "     \___.----'          |     `--.____\n"
        maldb_banner += "    /`-._                |       __.-' \ \n"
        maldb_banner += "   /     `-._            ___.---'       \ \n"
        maldb_banner += "  /          `-.____.---'                \ \n"
        maldb_banner += " '_         /   |   \            __.--'--'\n"
        maldb_banner += "   `-._    /    |    \     __.--'     |\n"
        maldb_banner += "     | `-./     |     \_.-'           |\n"
        maldb_banner += "     |          |                     |\n"
        maldb_banner += "     |          |      Free Malwares  |\n"
        maldb_banner += "     |          |          & Hugs     |\n"
        maldb_banner += "_____|          |                     |______\n"
        maldb_banner += "     `-.        |  /\              _.-'\n"
        maldb_banner += "        `-.     |  || UP    __..--'\n"
        maldb_banner += "           `-.  |      __.-'\n"
        maldb_banner += "              `-|__.--'\n"

    elif screen is 3:
        maldb_banner = "           __  ___      __                               ____  ____\n"
        maldb_banner += "          /  |/  /___ _/ /      ______ _________        / __ \/ __ )\n"
        maldb_banner += "         / /|_/ / __ `/ / | /| / / __ `/ ___/ _ \______/ / / / __ |\n"
        maldb_banner += "        / /  / / /_/ / /| |/ |/ / /_/ / /  /  __/_____/ /_/ / /_/ /\n"
        maldb_banner += "       /_/  /_/\__,_/_/ |__/|__/\__,_/_/   \___/     /_____/_____/\n\n"
        maldb_banner += "                                version: " + version + "\n"
        maldb_banner += "                                db_version: " + db_ver + "\n"
        maldb_banner += "                                built by: " + authors + "\n\n"
