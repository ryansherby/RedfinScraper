from redfin_scraper import RedfinScraper

scraper=RedfinScraper()
scraper.setup('JUNK')

scraper=RedfinScraper()
scraper.setup('./zip_code_database.csv')

scraper=RedfinScraper()
scraper.setup() # From Config

scraper=RedfinScraper()
scraper.setup(None)

scraper.setup() # Test for no re-download

scraper.scrape(city_states=None,zip_codes=['JUNK'])
scraper.scrape(city_states=None,zip_codes='JUNK')
scraper.scrape(city_states=['Omaha, NE'],zip_codes='JUNK')
scraper.scrape(city_states=None,zip_codes=['77002','JUNK','77003'])
scraper.scrape(city_states=['Omaha,NE'],zip_codes=None)
scraper.scrape(city_states=[('Houston', 'TX'),'JUNK, JUNKY'],zip_codes=None)
scraper.scrape(city_states=['junk, junky'],zip_codes=['77002'])
scraper.scrape() # From Config

for i in range(1,7):
    try:
        scraper.get_data(id=f"D00{i}")
    except:
        print("Failed")