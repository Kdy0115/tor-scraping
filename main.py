import configparser

from impl.scrapinglogic import ScrapingLogic
            
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

general_settings = config_ini['DEFAULT']
system_settings  = config_ini['SYSTEM']
            
def main(url:str, system_settings:dict):
    scraping_logic = ScrapingLogic(system_settings)
    scraping_logic.scraping(url)

if __name__ == '__main__':
    main(general_settings['TARGET_URL'], system_settings)
                

