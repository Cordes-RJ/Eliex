# -*- coding: utf-8 -*-
import hermes

def main():
    C = hermes.loadingConfigs()
    while True:
        hermes.mainLoop(C)
        
if __name__ == "__main__":
    main()