# -*- coding: utf-8 -*-
import xLoop

def main():
    C = xLoop.loadingConfigs()
    while True:
        xLoop.mainLoop(C)
        
if __name__ == "__main__":
    main()