from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #invited to add a todo item strait away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        #when hitting enter the page updates and now the page lists
        #"1: Buy peacock feathers" as an item in a to-do lists
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )
        # There is still a text box to add another item.

        # the page updates again. and now shows both items on the list

        #sees there is a unique url for the user -- tere is some
        #eplanitory text to that effect

        #Vist that url the todo list is still there

        # staisfied goes back to sleep
        self.fail('Finish the test!')
if __name__ == '__main__':
    unittest.main(warnings='ignore')
