#!/usr/bin/env python3

# import additional code to complete our task
import shutil
import os

# move into the working directory
os.chdir("/home/student/mycode1/")

# copy the filA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# The following line will create the directory if it does not exist already
# copy the entire directoryA to directoryB
os.system("rm -rf /home/student/mycode1/5g_research_backup/")
shutil.copytree("5g_research/", "5g_research_backup/")
