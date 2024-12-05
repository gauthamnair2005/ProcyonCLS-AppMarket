import sys
import os
import requests

folder1_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder1_path)

import kernel
import ekernel

def fetchNOTD():
    try:
        url = "https://raw.githubusercontent.com/gauthamnair2005/ProcyonCLS-NOTD/main/notd.txt"
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except:
        return None

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] >= "v1.4.0":
            ekernel.splashScreen("ProcyonCLS Dev News", "Version 1.1 | Procyonis Computing")
            ekernel.printHeader("Dev News")
            kernel.printInfo("Today's News")
            kernel.printInfo("----------------------")
            print(fetchNOTD())
        else:
            kernel.printError("This version of Dev News is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()
