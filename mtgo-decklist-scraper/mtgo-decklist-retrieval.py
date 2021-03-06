#!/usr/bin/env python
# coding: utf-8

import sys

#Program which allows retrieval of decks from any format from MTGO, 
#using a set start and end date in a YYYY-MM-DD format and a format 
#(standard, modern, legacy, pauper, pioneer, vintage).

def getmtgDecklists(startDate, endDate, format_):

    #Import necessary libraries
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    from datetime import datetime, timedelta
    
    #Assign empty variables 
    requestslist = []
    decklistsdata = []
    
    #Convert start and end dates into Date objects, as well as assign interval for checking
    startdateobj = datetime.strptime(startDate,'%Y-%m-%d')
    enddateobj = datetime.strptime(endDate,'%Y-%m-%d')
    delta = timedelta(days=1)
    
    #Scrape each instance of published leagues and challenges of the chosen format for each day and add it to a request list. 
    while startdateobj <= enddateobj:
        requestslist.append('https://magic.wizards.com/en/articles/archive/mtgo-standings/' + format_ + '-league-' + startdateobj.strftime('%Y-%m-%d'))
        requestslist.append('https://magic.wizards.com/en/articles/archive/mtgo-standings/' + format_ + '-challenge-' + startdateobj.strftime('%Y-%m-%d'))
        startdateobj += delta
    
    #Iterate through each possible URL. For each that is not negative for decklists, add the list of cards to decklistsdata.
    for website in requestslist:
        
        #Request each URL, translate into a parsable format, and filter all individual instances of decklists.
        mtgpage = requests.get(website)
        mtgsoup = BeautifulSoup(mtgpage.content, "html.parser")
        decklists = mtgsoup.find_all('div', class_='sorted-by-overview-container sortedContainer')
        
        if decklists != []:
            
            #For each individual decklist, search for each card count, then each cardname, 
            #then match them in a dictionary and append them to decklistdata
            for deck in decklists:

                cardcount = []
                cardnames = []
                cardtuples = {}

                for ccount in deck.find_all('span',class_='card-count'):
                    cardcount.append(int(ccount.contents[0]))

                for names in deck.find_all('a', class_='deck-list-link'):
                    cardnames.append(names.contents[0])

                for entries in range(len(cardnames)):
                    cardtuples[cardnames[entries]] = cardcount[entries]


                decklistsdata.append(cardtuples)
                
    #Transform a list of dictionaries into a DataFrame, replace NaN's with 0, and drop all cards with >4 copies (basic lands, etc.)
    deckmatrix = pd.DataFrame(decklistsdata).fillna(0)
    deckmatrix = deckmatrix[deckmatrix <= 4].dropna(axis = 1)
                
    return deckmatrix


if __name__ == '__main__':
    # Map command line arguments to function arguments.
    getmtgDecklists(sys.argv[1:])