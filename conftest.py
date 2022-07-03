import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', \
        help='Choose browser language in two letters format')
    parser.addoption('--browser_name', action='store', default='chrome',\
        help='Choose browser: chrome or firefox')
    
@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    
    link = 'http://selenium1py.pythonanywhere.com/'

    user_language = request.config.getoption('language')
    if len(user_language) != 2:
        raise pytest.UsageError('--language should content two letters')
    
    if browser_name.lower() == 'chrome':
        print('\nstart chrome for test..')
        browser = webdriver.Chrome()
        
        options = Options()
        
        options.add_experimental_option('prefs', {'intl.accepr_languages': \
            user_language})
        browser = webdriver.Chrome(options=options)
        
    elif browser_name.lower() == 'firefox':
        print('\nstart firefox to test..')
        browser = webdriver.Firefox()
        
        fire_prof = webdriver.FirefoxProfile()
        fire_prof.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=fire_prof)
    
    else:
        raise pytest.UsageError('--browser_name was wrong, should be \
            chrome or firefox')
    yield browser, link
    print('\nquit browser')
    browser.quit()
    