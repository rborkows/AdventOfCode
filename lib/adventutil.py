import sys
import os
#sys.path.append("AdventOfCode/lib")
import session
import requests

class InputFetcher:
    def __init__(self, year, day) -> None:
        self.year = year
        self.day = day
        self.inputfile = f"AdventOfCode/{year}/{day}/input"
        
    def fetch(self, rstrip = True, commasplit = False, small = False):
        if small:
            with open(self.inputfile + ".small", "r") as f: # throws exception if small file does not exist
                input = f.readlines()
        else:
            if not os.path.exists(self.inputfile):
                print("Fetching input from web")
                url = f"https://adventofcode.com/{self.year}/day/{self.day}/input"
                r = requests.get(url, cookies = session.cookie, headers = {"User-Agent": "github.com/rborkows/AdventOfCode Robert Borkowski"})
                with open(self.inputfile, "wb") as f:
                    f.write(r.content)
                
            with open(self.inputfile, "r") as f:
                input = f.readlines()

        if rstrip:
            input = [ l.rstrip() for l in input ]

        if commasplit:
            input = [ l.split(",") for l in input ]

        return input
        

        