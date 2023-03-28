# Github Informations                              
USER      = "Emericdefay"                                             # EDIT ME
REPO      = "k0rp-game"                                               # EDIT ME
TAG_FRONT = ""                                                        # EDIT ME
TAG_BACK  = ""                                                        # EDIT ME
APP_NAME  = "K0RP.Game"                                               # EDIT ME
UPT_NAME  = "update"                                                  # EDIT ME


# Generate Informations
with open("./version.txt", 'r') as f:
    version = f.read()
import datetime
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Retrieve Informations
GIT_URL   = f"https://github.com/{USER}/{REPO}.git"
VERSION   = version
DATE_UPD  = date