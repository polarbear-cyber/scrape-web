from booking.booking import Booking

try:
    with Booking() as bot:
        bot.launchBrowser()
        bot.acceptCookie()
        bot.changeCurrency(currency='GBP')
        bot.placeStay('New York')
        bot.dateStay(check_in = '2021-05-16',
                    check_out = '2021-05-23')
        bot.numberPeople(adult=10)
        bot.submitSearch()
        bot.apply_filtrations()
        bot.refresh() # A workaround to let our bot to grab the data properly
        bot.report_results()
        
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise