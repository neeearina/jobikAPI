import os
import time

import django
import selenium
import selenium.webdriver

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobik_api.settings")
django.setup()

import categories.models
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
                selenium.webdriver.common.by.By.CLASS_NAME, "list-prof-cat",
            )
            categories_list = category_container.find_elements(
                selenium.webdriver.common.by.By.TAG_NAME, "li",
            )
            for category in categories_list:
                category_elements = category.find_element(
                    selenium.webdriver.common.by.By.TAG_NAME, "a",
                )
                category_title = category_elements.text
                link = category_elements.get_attribute("href")
                num_of_professions = int(
                    category.find_element(
                        selenium.webdriver.common.by.By.TAG_NAME, "span",
                    ).text,
                )
                categories.models.CategoriesModel.objects.create(
                    name=category_title,
                    link_to_professions=link,
                    num_of_professions=num_of_professions,
                    is_published=True,
                )
            time.sleep(1)
            self.browser.quit()
        except Exception as e:
            print(e)

    def create_professions_table(self):
        profession_urls = (
            categories.models.CategoriesModel.objects.professions_urls()
        )
        try:
            for url in profession_urls:
                self.browser.get(url.get("link_to_professions"))
                time.sleep(2)
                container_for_professions = self.browser.find_element(
                    selenium.webdriver.common.by.By.CLASS_NAME, "grid-view",
                )
                professions_list = container_for_professions.find_elements(
                    selenium.webdriver.common.by.By.TAG_NAME, "tr",
                )
                for profession in professions_list:
                    profession_info = profession.find_elements(
                        selenium.webdriver.common.by.By.TAG_NAME, "td",
                    )
                    if len(profession_info) < 3:
                        continue
                    category_object = (
                        categories.models.CategoriesModel.objects.get(
                            pk=url.get("id"))
                    )
                    wage = (
                        profession_info[1].text
                        .replace("₽", "").replace(" ", "")
                    )
                    if not wage.isdigit():
                        wage = 0
                    professions.models.ProfessionsModel.objects.create(
                        name=profession_info[0].text,
                        description=profession_info[2].text,
                        wage=wage,
                        is_published=True,
                        category=category_object,
                    )
        except Exception as e:
            print(e)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobik_api.settings")
    django.setup()
    parser = CategoryProfessionParser()
    # parser.create_category_table()
    os.environ["PYTHONIOENCODING"] = "utf-8"
    parser.create_professions_table()
    del os.environ["PYTHONIOENCODING"]
