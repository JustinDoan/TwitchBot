import string
import json
import re

class Viewer:
        # figure out how to grab each user one by one.

        def __init__(self, name):
                self.name = name
                self.dibz = 0;
        def SetDibz(self, Dibz):
                self.dibz =Dibz

        
        
        def GetAllViewers():
                import bot as b
                NameOfViewers = str((b.get_viewers("","")))

                NameOfViewers = NameOfViewers.replace("\'","\"")
                NameOfViewers = NameOfViewers.replace("\[", None)
                NameOfViewers = NameOfViewers.replace("\]", None)
                print(type(NameOfViewers))

                if "ivigideon" in NameOfViewers:
                        print("That name was found.")
                
                return NameOfViewers




