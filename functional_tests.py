from selenium import webdriver
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
        self.fail('Finish the test!')
        #invited to add a todo item strait away

        #types "Buy peacock feathers" into a text box

        #when hitting enter the page updates and now the page lists
        #"1: Buy peacock feathers" as an item in a to-do lists

        # There is still a text box to add another item.
#enter "Use peacock feathers to make a fly"

        # the page updates again. and now shows both items on the list

        #sees there is a unique url for the user -- tere is some
        #eplanitory text to that effect

        #Vist that url the todo list is still there

        # staisfied goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
