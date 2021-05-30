from selenium import webdriver

browser = webdriver.Firefox()

# Edith heard about a sweet new online to-do app.
# She goes to check out it's home page
browser.get('http://localhost:8000')

# She notices the page title and header mention To-Do lists
assert 'To-Do' in browser.title

# She is invited to enter a todo item straight away

# She types "Fill out paper work for ODNR"

# When she hits enter, the page updates, and not the page lists
# "1: Fill out paper work for ODNR" as an item in a to-do list

# There is still a text box inviting her to add another item.
# She enters "order parts for bike shop"

# The page updates again, and shows both items on her list

# Edith wonders if the site will remember her list
# She see's that the site has generated a unique URL for her  -- there is 
# some explanatory tesxt to that effect

# She visits that URL - her to-do list is still there

# Satisfied, she goe s back to sleep

browser.quit()

