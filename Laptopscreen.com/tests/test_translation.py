from locators import *
from   pages.main_page  import BasePage
import logging


logger = logging.getLogger(__name__)


def test_translation(driver):
        main_page=BasePage(driver)
        languages_list=[TO_SPANISH,TO_FRENCH,TO_GERMAN,TO_ITALIAN]  


        for page, locators  in DATABASE.items():
            driver.get(page)
            logger.info(f"Testing translations for page: {page}")

            index=0
            for language in languages_list:
                main_page.change_language(language)
                logger.info(f"Changed language to: {language}")

                for locator,values in  locators.items():
                    element=main_page.find_element_(locator)
                    if element:
                         logger.info(f"Element found with locator: {locator} ")
                         assert element.text==values[index].strip(),  f"mismatch between {element.text}  and {values[index]} "
                    else:
                         logger.warning(f"⚠️ Element not found for locator: {locator}")
                index+=1        
