from __future__ import print_function
import sys
from .parse import parse

class argc:
    argc = dict()
    args = dict()

    def __init__(self, args = sys.argv[1:], detectType = True):
        self.args.update(parse(args, detectType))
    
    def add(self, command, do, exitOn = False):
        if command in self.args:
            if exitOn:
                self.argc.update({command: {"do": do, "exit":True}})
            else:
                self.argc.update({command: {"do": do, "exit":False}})

    def get(self, string, useBool = True):
        if string in self.args:
            if useBool:
                if self.args[string] and useBool:
                    return True
                elif not self.args[string] and useBool:
                    return False
                else:
                    return None
            else:
                # else return data
                return self.args[string]
        else:
            # is not set
            return None
    
    def run(self):
        keys = self.args.keys()
        for i in keys:
            if i in self.argc:

                co = self.argc[i]
                com = co["do"]

                if type(com) == list:
                    for x in com:
                        if hasattr(x, "__call__"):
                            print(x())
                        else:
                            print(x)
                        
                elif hasattr(com, "__call__"):
                    print(com())
                else:
                    print(com)

                if co["exit"]:
                    exit()

            else:
                return None