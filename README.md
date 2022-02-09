# :flower_playing_cards: May's MtG Projects :flower_playing_cards:
A collection of helpful utilities that allow for the scraping and analysis of various aspects of Magic: the Gathering cards.

## :globe_with_meridians: MTGO Decklist Scraping Tool
This tool allows for easy collection of decklist data from all formats regularly played on Magic the Gathering Online (MTGO). The program takes an input of a start date and end date in YYYY-MM-DD format, as well as a string naming the chosen competitive format (Standard, Modern, Legacy, Pauper, Vintage, Pioneer, etc.)
### Extraction
Data is scraped directly from [Wizards' MtG website](https://magic.wizards.com) and converted into a parsable format via [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/). 
### Transformation
The tool returns a DataFrame object which contains each individual deck as a row and each card as a column, with the values being the number of cards in its respective deck. This allows for further analysis of the relationships between each card, as well as the decklists themselves.

## :detective: MtG Card Reccomendations
These tools analyze the relationships between cards in decks and, when provided the input of a card name and a chosen DataFrame, reccomends the top 10 cards that are most played with that specific card across all of the top decks. 
### Method 1: Number of Cards Dependent
This method reccomends the cards that are played most with the input, considering the number of copies. A potential upside of this method is that cards played more often are more likely to be useful, however a small number of decks that play the maximum number of cards (4x) can skew the results.
### Method 2: Number of Cards Independent
This method reccomends the cards that are played most with the input, independent of the number of copies. This allows for cards that are played at smaller numbers regularly to appear, however it also artifically elevates the prevalence of lands and other cards that are played in small quantities. 
### Limitations
Given the relatively low number of deck archetypes played competitively, it is difficult for this reccomendation system to "break the mold" and allow for innovation beyond the decks that are already published. This could be mitigated by collecting decks from sources besides the official Wizards website such as [TappedOut](https://www.tappedout.com), but this could also introduce decks that have not been competitively proven. 

## :chart_with_upwards_trend: Future Directions
### Scryfall API Integration
By combining the DataFrame output with the large number of datapoints available from [Scryfall](https://www.scryfall.com/), such as card color, card type, mana value, and price, this would allow for significantly more in-depth analysis of deck specifics. 
