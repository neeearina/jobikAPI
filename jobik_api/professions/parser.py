import os
import time

import django
import selenium
import selenium.webdriver

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "jobik_api.settings")
django.setup()

import professions.models

__all__ = []


class CategoryProfessionParser:
    def __init__(self):
        self.browser = selenium.webdriver.Chrome()

    def create_category_table(self):
        try:
            self.browser.get("https://www.profguide.io/professions/")
            time.sleep(2)
            category_container = self.browser.find_element(
                selenium.webdriver.common.by.By.CLASS_NAME, "list-prof-cat")
            categories = category_container.find_elements(
                selenium.webdriver.common.by.By.TAG_NAME, "li")
            for category in categories:
                category_elements = category.find_element(
                    selenium.webdriver.common.by.By.TAG_NAME, "a")
                category_title = category_elements.text
                link = category_elements.get_attribute("href")
                num_of_professions = int(category.find_element(
                    selenium.webdriver.common.by.By.TAG_NAME, "span").text)
                professions.models.CategoriesModel.objects.create(
                    name=category_title,
                    link_to_professions=link,
                    num_of_professions=num_of_professions,
                    is_published=True,
                )
            time.sleep(2)
            self.browser.quit()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "jobik_api.settings")
    django.setup()
    parser = CategoryProfessionParser()
    parser.create_category_table()
