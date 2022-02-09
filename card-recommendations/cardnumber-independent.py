#!/usr/bin/env python
# coding: utf-8

def TopCardRecs2(cardname, deckmatrix):
    
    import numpy as np
    
    relatedtups = []
    
    
    if cardname not in deckmatrix.columns:
        return print('Card not available.')
    
    else:
        
        cardnamematrix = (deckmatrix[deckmatrix[cardname] > 0] > 0).drop(cardname, axis = 1)
        
        for diffcards in cardnamematrix.columns:
            relatedtups.append((diffcards, np.mean(cardnamematrix[diffcards])))
    
    return sorted(relatedtups, key = lambda x:x[1], reverse = True)[:10]