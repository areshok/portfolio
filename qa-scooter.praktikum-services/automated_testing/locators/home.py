from selenium.webdriver.common.by import By


class HomeLocator:
    order = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']")

    class Question:
        status_answer = "hidden"
        question_xpath_pattern = (By.XPATH, ".//div[@id='accordion__heading-{}']")
        answer_xpath_pattern = ".//div[@id='accordion__panel-{}']"
        answer_xpath_pattern_question = (By.XPATH, ".//div[@id='accordion__heading-{}']/ancestor::div/following-sibling::div[@id='accordion__panel-{}']")
