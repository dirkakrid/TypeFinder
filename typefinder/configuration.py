# -*- coding: utf-8 -*-

class Configuration(object):
    """docstring for Configuration"""
    # Date formats for date matching:
    # https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
    search_date_formats = ['%d %m %Y', '%d-%m-%Y', '%d/%m/%Y', '%d.%m.%Y', '%d/%m-%Y', '%d.%m-%Y', '%Y-%m-%d']
    search_date_formats = search_date_formats + ['%d %m %y', '%d-%m-%y', '%d/%m/%y', '%d.%m.%y', '%d/%m-%y', '%d.%m-%y', '%y-%m-%d']
    standard_date_format = '%d-%m-%Y'
    # https://www.iana.org/domains/root/db
    dns_root_zones = [u'abogado', u'ac', u'academy', u'accountants', u'active', u'actor', u'ad', u'ae', u'aero', u'af', u'ag', u'agency', u'ai', u'airforce', u'al', u'allfinanz', u'alsace', u'am', u'an', u'android', u'ao', u'aq', u'aquarelle', u'ar', u'archi', u'army', u'arpa', u'as', u'asia', u'associates', u'at', u'attorney', u'au', u'auction', u'audio', u'autos', u'aw', u'ax', u'axa', u'az', u'ba', u'band', u'bar', u'bargains', u'bayern', u'bb', u'bd', u'be', u'beer', u'berlin', u'best', u'bf', u'bg', u'bh', u'bi', u'bid', u'bike', u'bio', u'biz', u'bj', u'bl', u'black', u'blackfriday', u'bloomberg', u'blue', u'bm', u'bmw', u'bn', u'bnpparibas', u'bo', u'boo', u'boutique', u'bq', u'br', u'brussels', u'bs', u'bt', u'budapest', u'build', u'builders', u'business', u'buzz', u'bv', u'bw', u'by', u'bz', u'bzh', u'ca', u'cab', u'cal', u'camera', u'camp', u'cancerresearch', u'capetown', u'capital', u'caravan', u'cards', u'care', u'career', u'careers', u'casa', u'cash', u'cat', u'catering', u'cc', u'cd', u'center', u'ceo', u'cern', u'cf', u'cg', u'ch', u'channel', u'cheap', u'christmas', u'chrome', u'church', u'ci', u'citic', u'city', u'ck', u'cl', u'claims', u'cleaning', u'click', u'clinic', u'clothing', u'club', u'cm', u'cn', u'co', u'coach', u'codes', u'coffee', u'college', u'cologne', u'com', u'community', u'company', u'computer', u'condos', u'construction', u'consulting', u'contractors', u'cooking', u'cool', u'coop', u'country', u'cr', u'credit', u'creditcard', u'cricket', u'crs', u'cruises', u'cu', u'cuisinella', u'cv', u'cw', u'cx', u'cy', u'cymru', u'cz', u'dad', u'dance', u'dating', u'day', u'de', u'deals', u'degree', u'delivery', u'democrat', u'dental', u'dentist', u'desi', u'diamonds', u'diet', u'digital', u'direct', u'directory', u'discount', u'dj', u'dk', u'dm', u'dnp', u'do', u'domains', u'durban', u'dvag', u'dz', u'eat', u'ec', u'edu', u'education', u'ee', u'eg', u'eh', u'email', u'emerck', u'energy', u'engineer', u'engineering', u'enterprises', u'equipment', u'er', u'es', u'esq', u'estate', u'et', u'eu', u'eus', u'events', u'everbank', u'exchange', u'expert', u'exposed', u'fail', u'farm', u'feedback', u'fi', u'finance', u'financial', u'firmdale', u'fish', u'fishing', u'fitness', u'fj', u'fk', u'flights', u'florist', u'flsmidth', u'fly', u'fm', u'fo', u'foo', u'forsale', u'foundation', u'fr', u'frl', u'frogans', u'fund', u'furniture', u'futbol', u'ga', u'gal', u'gallery', u'gb', u'gbiz', u'gd', u'ge', u'gent', u'gf', u'gg', u'gh', u'gi', u'gift', u'gifts', u'gives', u'gl', u'glass', u'gle', u'global', u'globo', u'gm', u'gmail', u'gmo', u'gmx', u'gn', u'google', u'gop', u'gov', u'gp', u'gq', u'gr', u'graphics', u'gratis', u'green', u'gripe', u'gs', u'gt', u'gu', u'guide', u'guitars', u'guru', u'gw', u'gy', u'hamburg', u'haus', u'healthcare', u'help', u'here', u'hiphop', u'hiv', u'hk', u'hm', u'hn', u'holdings', u'holiday', u'homes', u'horse', u'host', u'hosting', u'house', u'how', u'hr', u'ht', u'hu', u'ibm', u'id', u'ie', u'il', u'im', u'immo', u'immobilien', u'in', u'industries', u'info', u'ing', u'ink', u'institute', u'insure', u'int', u'international', u'investments', u'io', u'iq', u'ir', u'irish', u'is', u'it', u'je', u'jetzt', u'jm', u'jo', u'jobs', u'joburg', u'jp', u'juegos', u'kaufen', u'ke', u'kg', u'kh', u'ki', u'kim', u'kitchen', u'kiwi', u'km', u'kn', u'koeln', u'kp', u'kr', u'krd', u'kred', u'kw', u'ky', u'kz', u'la', u'lacaixa', u'land', u'latrobe', u'lawyer', u'lb', u'lc', u'lds', u'lease', u'legal', u'lgbt', u'li', u'life', u'lighting', u'limited', u'limo', u'link', u'lk', u'loans', u'london', u'lotto', u'lr', u'ls', u'lt', u'ltda', u'lu', u'luxe', u'luxury', u'lv', u'ly', u'ma', u'madrid', u'maison', u'management', u'mango', u'market', u'marketing', u'mc', u'md', u'me', u'media', u'meet', u'melbourne', u'meme', u'memorial', u'menu', u'mf', u'mg', u'mh', u'miami', u'mil', u'mini', u'mk', u'ml', u'mm', u'mn', u'mo', u'mobi', u'moda', u'moe', u'monash', u'money', u'mormon', u'mortgage', u'moscow', u'motorcycles', u'mov', u'mp', u'mq', u'mr', u'ms', u'mt', u'mu', u'museum', u'mv', u'mw', u'mx', u'my', u'mz', u'na', u'nagoya', u'name', u'navy', u'nc', u'ne', u'net', u'network', u'neustar', u'new', u'nexus', u'nf', u'ng', u'ngo', u'nhk', u'ni', u'ninja', u'nl', u'no', u'np', u'nr', u'nra', u'nrw', u'nu', u'nyc', u'nz', u'okinawa', u'om', u'ong', u'onl', u'ooo', u'org', u'organic', u'otsuka', u'ovh', u'pa', u'paris', u'partners', u'parts', u'party', u'pe', u'pf', u'pg', u'ph', u'pharmacy', u'photo', u'photography', u'photos', u'physio', u'pics', u'pictures', u'pink', u'pizza', u'pk', u'pl', u'place', u'plumbing', u'pm', u'pn', u'pohl', u'poker', u'post', u'pr', u'praxi', u'press', u'pro', u'prod', u'productions', u'prof', u'properties', u'property', u'ps', u'pt', u'pub', u'pw', u'py', u'qa', u'qpon', u'quebec', u're', u'realtor', u'recipes', u'red', u'rehab', u'reise', u'reisen', u'reit', u'ren', u'rentals', u'repair', u'report', u'republican', u'rest', u'restaurant', u'reviews', u'rich', u'rio', u'rip', u'ro', u'rocks', u'rodeo', u'rs', u'rsvp', u'ru', u'ruhr', u'rw', u'ryukyu', u'sa', u'saarland', u'sarl', u'sb', u'sc', u'sca', u'scb', u'schmidt', u'schule', u'science', u'scot', u'sd', u'se', u'services', u'sexy', u'sg', u'sh', u'shiksha', u'shoes', u'si', u'singles', u'sj', u'sk', u'sl', u'sm', u'sn', u'so', u'social', u'software', u'sohu', u'solar', u'solutions', u'soy', u'space', u'spiegel', u'sr', u'ss', u'st', u'su', u'supplies', u'supply', u'support', u'surf', u'surgery', u'suzuki', u'sv', u'sx', u'sy', u'sydney', u'systems', u'sz', u'taipei', u'tatar', u'tattoo', u'tax', u'tc', u'td', u'technology', u'tel', u'tf', u'tg', u'th', u'tienda', u'tips', u'tirol', u'tj', u'tk', u'tl', u'tm', u'tn', u'to', u'today', u'tokyo', u'tools', u'top', u'town', u'toys', u'tp', u'tr', u'trade', u'training', u'travel', u'tt', u'tui', u'tv', u'tw', u'tz', u'ua', u'ug', u'uk', u'um', u'university', u'uno', u'uol', u'us', u'uy', u'uz', u'va', u'vacations', u'vc', u've', u'vegas', u'ventures', u'versicherung', u'vet', u'vg', u'vi', u'viajes', u'villas', u'vision', u'vlaanderen', u'vn', u'vodka', u'vote', u'voting', u'voto', u'voyage', u'vu', u'wales', u'wang', u'watch', u'webcam', u'website', u'wed', u'wedding', u'wf', u'whoswho', u'wien', u'wiki', u'williamhill', u'wme', u'work', u'works', u'world', u'ws', u'wtc', u'wtf', u'vermögensberater', u'vermögensberatung', u'xxx', u'xyz', u'yachts', u'yandex', u'ye', u'yoga', u'yokohama', u'youtube', u'yt', u'za', u'zip', u'zm', u'zone', u'zw']
    # Hosts file for hostname matching
    rfc1123_hostname_label = r'^(?!-)[a-z0-9-]{,63}(?<!-)$'
    rfc1123_hostname = r'^((?!-)[a-z0-9-]+\.)*(?!-)[a-z0-9-]+$'
    hostname_re = [r'^[a-z]\S+\d+$', r'^(?:\S*(?:(?:srv)|(?:app)|(?:sql))\S+)|(?:\S+(?:(?:srv)|(?:app)|(?:sql))\S*)$']
    known_hosts = []
    host_file = 'hosts'
    # Country Codes
    # https://www.iso.org/obp/ui/#search
    country = dict()
    country['ad'] = 'Andorra'
    country['ae'] = 'United Arab Emirates (the)'
    country['af'] = 'Afghanistan'
    country['ag'] = 'Antigua and Barbuda'
    country['ai'] = 'Anguilla'
    country['al'] = 'Albania'
    country['am'] = 'Armenia'
    country['ao'] = 'Angola'
    country['aq'] = 'Antarctica'
    country['ar'] = 'Argentina'
    country['as'] = 'American Samoa'
    country['at'] = 'Austria'
    country['au'] = 'Australia'
    country['aw'] = 'Aruba'
    country['ax'] = 'Åland Islands'
    country['az'] = 'Azerbaijan'
    country['ba'] = 'Bosnia and Herzegovina'
    country['bb'] = 'Barbados'
    country['bd'] = 'Bangladesh'
    country['be'] = 'Belgium'
    country['bf'] = 'Burkina Faso'
    country['bg'] = 'Bulgaria'
    country['bh'] = 'Bahrain'
    country['bi'] = 'Burundi'
    country['bj'] = 'Benin'
    country['bl'] = 'Saint Barthélemy'
    country['bm'] = 'Bermuda'
    country['bn'] = 'Brunei Darussalam'
    country['bo'] = 'Bolivia, Plurinational State of'
    country['bq'] = 'Bonaire, Sint Eustatius and Saba'
    country['br'] = 'Brazil'
    country['bs'] = 'Bahamas (the)'
    country['bt'] = 'Bhutan'
    country['bv'] = 'Bouvet Island'
    country['bw'] = 'Botswana'
    country['by'] = 'Belarus'
    country['bz'] = 'Belize'
    country['ca'] = 'Canada'
    country['cc'] = 'Cocos (Keeling) Islands (the)'
    country['cd'] = 'Congo (the Democratic Republic of the)'
    country['cf'] = 'Central African Republic (the)'
    country['cg'] = 'Congo'
    country['ch'] = 'Switzerland'
    country['ci'] = 'Côte d\'Ivoire'
    country['ck'] = 'Cook Islands (the)'
    country['cl'] = 'Chile'
    country['cm'] = 'Cameroon'
    country['cn'] = 'China'
    country['co'] = 'Colombia'
    country['cr'] = 'Costa Rica'
    country['cu'] = 'Cuba'
    country['cv'] = 'Cabo Verde'
    country['cw'] = 'Curaçao'
    country['cx'] = 'Christmas Island'
    country['cy'] = 'Cyprus'
    country['cz'] = 'Czech Republic (the)'
    country['de'] = 'Germany'
    country['dj'] = 'Djibouti'
    country['dk'] = 'Denmark'
    country['dm'] = 'Dominica'
    country['do'] = 'Dominican Republic (the)'
    country['dz'] = 'Algeria'
    country['ec'] = 'Ecuador'
    country['ee'] = 'Estonia'
    country['eg'] = 'Egypt'
    country['eh'] = 'Western Sahara*'
    country['er'] = 'Eritrea'
    country['es'] = 'Spain'
    country['et'] = 'Ethiopia'
    country['fi'] = 'Finland'
    country['fj'] = 'Fiji'
    country['fk'] = 'Falkland Islands (the) [Malvinas]'
    country['fm'] = 'Micronesia (the Federated States of)'
    country['fo'] = 'Faroe Islands (the)'
    country['fr'] = 'France'
    country['ga'] = 'Gabon'
    country['gb'] = 'United Kingdom (the)'
    country['gd'] = 'Grenada'
    country['ge'] = 'Georgia'
    country['gf'] = 'French Guiana'
    country['gg'] = 'Guernsey'
    country['gh'] = 'Ghana'
    country['gi'] = 'Gibraltar'
    country['gl'] = 'Greenland'
    country['gm'] = 'Gambia (The)'
    country['gn'] = 'Guinea'
    country['gp'] = 'Guadeloupe'
    country['gq'] = 'Equatorial Guinea'
    country['gr'] = 'Greece'
    country['gs'] = 'South Georgia and the South Sandwich Islands'
    country['gt'] = 'Guatemala'
    country['gu'] = 'Guam'
    country['gw'] = 'Guinea-Bissau'
    country['gy'] = 'Guyana'
    country['hk'] = 'Hong Kong'
    country['hm'] = 'Heard Island and McDonald Islands'
    country['hn'] = 'Honduras'
    country['hr'] = 'Croatia'
    country['ht'] = 'Haiti'
    country['hu'] = 'Hungary'
    country['id'] = 'Indonesia'
    country['ie'] = 'Ireland'
    country['il'] = 'Israel'
    country['im'] = 'Isle of Man'
    country['in'] = 'India'
    country['io'] = 'British Indian Ocean Territory (the)'
    country['iq'] = 'Iraq'
    country['ir'] = 'Iran (the Islamic Republic of)'
    country['is'] = 'Iceland'
    country['it'] = 'Italy'
    country['je'] = 'Jersey'
    country['jm'] = 'Jamaica'
    country['jo'] = 'Jordan'
    country['jp'] = 'Japan'
    country['ke'] = 'Kenya'
    country['kg'] = 'Kyrgyzstan'
    country['kh'] = 'Cambodia'
    country['ki'] = 'Kiribati'
    country['km'] = 'Comoros'
    country['kn'] = 'Saint Kitts and Nevis'
    country['kp'] = 'Korea (the Democratic People\'s Republic of)'
    country['kr'] = 'Korea (the Republic of)'
    country['kw'] = 'Kuwait'
    country['ky'] = 'Cayman Islands (the)'
    country['kz'] = 'Kazakhstan'
    country['la'] = 'Lao People\'s Democratic Republic (the)'
    country['lb'] = 'Lebanon'
    country['lc'] = 'Saint Lucia'
    country['li'] = 'Liechtenstein'
    country['lk'] = 'Sri Lanka'
    country['lr'] = 'Liberia'
    country['ls'] = 'Lesotho'
    country['lt'] = 'Lithuania'
    country['lu'] = 'Luxembourg'
    country['lv'] = 'Latvia'
    country['ly'] = 'Libya'
    country['ma'] = 'Morocco'
    country['mc'] = 'Monaco'
    country['md'] = 'Moldova (the Republic of)'
    country['me'] = 'Montenegro'
    country['mf'] = 'Saint Martin (French part)'
    country['mg'] = 'Madagascar'
    country['mh'] = 'Marshall Islands (the)'
    country['mk'] = 'Macedonia (the former Yugoslav Republic of)'
    country['ml'] = 'Mali'
    country['mm'] = 'Myanmar'
    country['mn'] = 'Mongolia'
    country['mo'] = 'Macao'
    country['mp'] = 'Northern Mariana Islands (the)'
    country['mq'] = 'Martinique'
    country['mr'] = 'Mauritania'
    country['ms'] = 'Montserrat'
    country['mt'] = 'Malta'
    country['mu'] = 'Mauritius'
    country['mv'] = 'Maldives'
    country['mw'] = 'Malawi'
    country['mx'] = 'Mexico'
    country['my'] = 'Malaysia'
    country['mz'] = 'Mozambique'
    country['na'] = 'Namibia'
    country['nc'] = 'New Caledonia'
    country['ne'] = 'Niger (the)'
    country['nf'] = 'Norfolk Island'
    country['ng'] = 'Nigeria'
    country['ni'] = 'Nicaragua'
    country['nl'] = 'Netherlands (the)'
    country['no'] = 'Norway'
    country['np'] = 'Nepal'
    country['nr'] = 'Nauru'
    country['nu'] = 'Niue'
    country['nz'] = 'New Zealand'
    country['om'] = 'Oman'
    country['pa'] = 'Panama'
    country['pe'] = 'Peru'
    country['pf'] = 'French Polynesia'
    country['pg'] = 'Papua New Guinea'
    country['ph'] = 'Philippines (the)'
    country['pk'] = 'Pakistan'
    country['pl'] = 'Poland'
    country['pm'] = 'Saint Pierre and Miquelon'
    country['pn'] = 'Pitcairn'
    country['pr'] = 'Puerto Rico'
    country['ps'] = 'Palestine, State of'
    country['pt'] = 'Portugal'
    country['pw'] = 'Palau'
    country['py'] = 'Paraguay'
    country['qa'] = 'Qatar'
    country['re'] = 'Réunion'
    country['ro'] = 'Romania'
    country['rs'] = 'Serbia'
    country['ru'] = 'Russian Federation (the)'
    country['rw'] = 'Rwanda'
    country['sa'] = 'Saudi Arabia'
    country['sb'] = 'Solomon Islands (the)'
    country['sc'] = 'Seychelles'
    country['sd'] = 'Sudan (the)'
    country['se'] = 'Sweden'
    country['sg'] = 'Singapore'
    country['sh'] = 'Saint Helena, Ascension and Tristan da Cunha'
    country['si'] = 'Slovenia'
    country['sj'] = 'Svalbard and Jan Mayen'
    country['sk'] = 'Slovakia'
    country['sl'] = 'Sierra Leone'
    country['sm'] = 'San Marino'
    country['sn'] = 'Senegal'
    country['so'] = 'Somalia'
    country['sr'] = 'Suriname'
    country['ss'] = 'South Sudan'
    country['st'] = 'Sao Tome and Principe'
    country['sv'] = 'El Salvador'
    country['sx'] = 'Sint Maarten (Dutch part)'
    country['sy'] = 'Syrian Arab Republic (the)'
    country['sz'] = 'Swaziland'
    country['tc'] = 'Turks and Caicos Islands (the)'
    country['td'] = 'Chad'
    country['tf'] = 'French Southern Territories (the)'
    country['tg'] = 'Togo'
    country['th'] = 'Thailand'
    country['tj'] = 'Tajikistan'
    country['tk'] = 'Tokelau'
    country['tl'] = 'Timor-Leste'
    country['tm'] = 'Turkmenistan'
    country['tn'] = 'Tunisia'
    country['to'] = 'Tonga'
    country['tr'] = 'Turkey'
    country['tt'] = 'Trinidad and Tobago'
    country['tv'] = 'Tuvalu'
    country['tw'] = 'Taiwan (Province of China)'
    country['tz'] = 'Tanzania, United Republic of'
    country['ua'] = 'Ukraine'
    country['ug'] = 'Uganda'
    country['um'] = 'United States Minor Outlying Islands (the)'
    country['us'] = 'United States (the)'
    country['uy'] = 'Uruguay'
    country['uz'] = 'Uzbekistan'
    country['va'] = 'Holy See (the) [Vatican City State]'
    country['vc'] = 'Saint Vincent and the Grenadines'
    country['ve'] = 'Venezuela, Bolivarian Republic of'
    country['vg'] = 'Virgin Islands (British)'
    country['vi'] = 'Virgin Islands (U.S.)'
    country['vn'] = 'Viet Nam'
    country['vu'] = 'Vanuatu'
    country['wf'] = 'Wallis and Futuna'
    country['ws'] = 'Samoa'
    country['ye'] = 'Yemen'
    country['yt'] = 'Mayotte'
    country['za'] = 'South Africa'
    country['zm'] = 'Zambia'
    country['zw'] = 'Zimbabwe'