from telegram.ext import Updater, InlineQueryHandler, CommandHandler                  
import requests
import re

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def get_url():
    contents =  requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''    
    while file_extension not in allowed_extension:        
        url = get_url()        
        file_extension = re.search("([^.]*)$",url).group(1).lower()   
    print("perrito") 
    return url

def bop(bot, update):
    url = image_url()
    print("encontre")
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)



def main():
    print("Starting bot")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    updater = Updater('805853693:AAHdOhCLO_ajPvEQ1K24VtpGkNcPb84ncfc')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    print("Starting start_polling")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__': 
    main()