#################################
#  IMPORT ##  IMPORT ##  IMPORT #
#################################
from os import system
import os
import sys


###########################
#  MAIN ##  MAIN ##  MAIN #
###########################


if __name__ == "__main__":

    strings = ["a","b","c","d","e"]

    for bla in strings:
        os.system("touch " + bla + " >> " + bla + " && " + "echo " + bla + bla + " >> " + bla)




