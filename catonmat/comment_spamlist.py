import re

r = re.compile

spamlist_names = [
    r('classifieds', re.I),
    r('credit card', re.I),
    r('austin home', re.I),
    r('noah theme', re.I),
    r('cash loan', re.I),
    r('payday loan', re.I),
    r('silver price', re.I),
    r('ed hardy', re.I),
    r('florida.*fishing', re.I),
    r('fishing.*florida', re.I),
    r('real estate', re.I),
    r('free dating', re.I),
    r('dating site', re.I),
    r('countertop', re.I),
    r('solar panel', re.I),
    r('dentists', re.I),
    r('.+dentist', re.I),
    r('dental clinic', re.I),
    r('locksmith in', re.I),
    r('buy.*online', re.I),
    r('coupons', re.I),
    r('self diagnosis', re.I),
    r('handicapped vans', re.I),
    r('hotel finder', re.I),
    r('horoscope', re.I),
    r('garmin.*forerunner', re.I),
    r('replica purses', re.I),
    r('cheap.*insurance', re.I),
    r('mobile.*review', re.I),
    r('.+app?artment', re.I),
    r('refurbished.+', re.I),
    r('water damage', re.I),
    r('fire damage', re.I),
    r('.+ seo', re.I),
    r('light bulb', re.I),
    r('.+ tour', re.I),
    r('surgery', re.I),
    r('.+ restoration', re.I),
    r('cleaning service', re.I),
    r('vibrator', re.I),
    r('male.+pills', re.I),
    r('seo .+', re.I),
    r('.+ lawyer', re.I),
    r('flat stomach', re.I),
    r('weight loss', re.I),
    r('angle grinder', re.I),
    r('janetcmr', re.I),
    r('steamfast sf-407', re.I),
    r('du ventre', re.I),
    r('iphone', re.I),
    r('antivirus', re.I),
    r('mortgage', re.I),
    r('windows.*key', re.I),
    r('office.*key', re.I),
    r('louis.*vuitton', re.I),
    r('land for sale', re.I),
    r('suspension training', re.I),
    r('artificial turf', re.I),
    r('make money', re.I),
    r('money online', re.I),
    r('beauty business', re.I),
    r('cheap.+ticket', re.I),
    r('hair loss', re.I),
]

spamlist_emails = [
    r('cancer', re.I),
]

spamlist_urls = [
    r('cancer', re.I),
    r('du-?ventre', re.I),
    r('xrumer.+service', re.I),
    r('cheap-', re.I),
]

spamlist_comments = [
    r('cash loan', re.I),
    r('tripploans.com', re.I),
    r('natural remed(y|ies)', re.I),
    r('acid reflux', re.I),
    r('unlock iphone', re.I),
    r('real estate', re.I),
]

