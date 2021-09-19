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
        # Edith heard about a sweet new online to-do app.
        # She goes to check out it's home page
        self.browser.get('http://localhost:8000')
        
        # She notices the page title and header mention To-Do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        # She is invited to enter a todo item straight away
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Fill out paper work for ODNR"
        input_box.send_keys('Fill out paper work for ODNR')

        # When she hits enter, the page updates, and not the page lists
        # "1: Fill out paper work for ODNR" as an item in a to-do list
        input_box.send_keys('Fill out paper work for ODNR')
        time.sleep(1)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Fill out paper work for ODNR' for row in rows),
            "New To-Do item did appear in table"
        )

        # There is still a text box inviting her to add another item.
        # She enters "order parts for bike shop"
        self.fail('Finish the test!')

        # The page updates again, and shows both items on her list


        # Edith wonders if the site will remember her list
        # She see's that the site has generated a unique URL for her  -- there is 
        # some explanatory tesxt to that effect

        # She visits that URL - her to-do list is still there

        # Satisfied, she goe s back to sleep
        
if __name__ == '__main__':
    unittest.main() 
