from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith heard about a sweet new online to-do app.
        # She goes to check out it's home page
        self.browser.get(self.live_server_url)
        
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
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        self.wait_for_row_in_list_table('1: Fill out paper work for ODNR')
                
        # There is still a text box inviting her to add another item.
        # She enters "order parts"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('order parts')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and shows both items on her list
        self.wait_for_row_in_list_table('1: Fill out paper work for ODNR')
        self.wait_for_row_in_list_table('2: order parts')
        
        #  Satisifed, she goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self)
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
    
        # Now a new user, Francis, comes along to the site

        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies
        self.browser.quit()
        self.browser.webdriver.Firefox()

        # Francis visits the home page, there is no sign of Ediths lists
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('order parts', page_text)

        # Francis starts a new list by entering a new item. He is less interesting than Edith
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets his own unique URL
        fancis_list_url = self.browser.current_url
        assertRegex(francis_list_url, '/lists/+')


        # Edith wonders if the site will remember her list
        # She see's that the site has generated a unique URL for her  -- there is 
        # some explanatory text to that effect
        self.fail('Finish the test!')

        # She visits that URL - her to-do list is still there

        # Satisfied, she goe s back to sleep
        