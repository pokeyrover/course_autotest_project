import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', \
        help='Choose browser language in two letters format')                               #Adding choosing browser language option by --language
    parser.addoption('--browser_name', action='store', default='chrome',\
        help='Choose browser: chrome or firefox')                                           #Adding choosing browser option by --browser_name
    
@pytest.fixture(scope='function')
def browser(request):                                                                       #function for open choosed browser for each test
    browser_name = request.config.getoption('browser_name')
    browser = None
    
    user_language = request.config.getoption('language')
    if len(user_language) != 2:
        raise pytest.UsageError('--language should content two letters')
    
    if browser_name.lower() == 'chrome':                                                    #will open chrome
        print('\nstart chrome for test..')
        
        options = Options()
        
        options.add_experimental_option('prefs', {'intl.accepr_languages': user_language})
        browser = webdriver.Chrome(options=options)
        
    elif browser_name.lower() == 'firefox':                                                 #will open firefox
        print('\nstart firefox to test..')
        
        fire_prof = webdriver.FirefoxProfile()
        fire_prof.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=fire_prof)
    
    else:
        raise pytest.UsageError('--browser_name was wrong, should be \
            chrome or firefox')
    yield browser
    print('\nquit browser')                                                                 #browser will close after each test
    browser.quit()
    