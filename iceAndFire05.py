#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint
import json

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"
AOIF_HOUSE = "https://www.anapioficeandfire.com/api/houses/"
AOIF_BOOK = "https://www.anapioficeandfire.com/api/books/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()

        allegiances = got_dj['allegiances']
        books = got_dj['books']
        name = got_dj['name']

        #pprint.pprint(got_dj)
        #with open ("character.json", "w") as f:
        #    json.dump(got_dj, f)

        ## Print Name
        pprint.pprint("Character Name: ")
        pprint.pprint(name)

        ## House Allegiances:
        pprint.pprint("House Allegiances: ")
        
        allies = []
        for ally in allegiances:
            r = requests.get(ally)
            allies.append(r.json()["name"])
            
        pprint.pprint(allies)
        #print("House Allegiances: ", sep.join(allies))

        ## Books
        #pprint.pprint("Books Character is in: ")

        book_names = [requests.get(book).json()["name"] for book in books]
        
        sep = '\n- '
        #pprint.pprint(book_names)
        print("Books Character is in: ", sep.join(book_names))
        

if __name__ == "__main__":
        main()

