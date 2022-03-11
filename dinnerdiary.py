from datetime import datetime, timedelta
from collections import Counter, OrderedDict


# to set up entries:
def print_entries(yr, mo, day):
    """
    print_entries(2021, 11, 1)
    """
    dstart = datetime(yr, mo, day)
    for i in range(60):
        print(f"    '{dstart.strftime('%Y-%m-%d')}': '',")
        dstart += timedelta(days=1)


dinners = OrderedDict({
    '2021-05-01': 'pizza de key',
    '2021-05-02': 'kare udon',
    '2021-05-03': 'hijiki gohan',
    '2021-05-04': 'chicken with miso',
    '2021-05-05': 'yakisoba',
    '2021-05-06': 'spaghetti with meatballs',
    '2021-05-07': 'pad thai',
    '2021-05-08': 'baked milanese',
    '2021-05-08b': 'coleslaw',
    '2021-05-09': 'gyoza',
    '2021-05-10': 'potato salad',
    '2021-05-11': 'mac and cheese',
    '2021-05-12': 'pork loin with bell peppers',
    '2021-05-13': 'stuffed zucchini',
    '2021-05-14': 'noodle soup',
    '2021-05-15': 'bean, pork and kale soup',
    '2021-05-16': 'roast chicken',
    '2021-05-17': 'beef steak with worcestershire sauce',
    '2021-05-18': 'hijiki gohan',
    '2021-05-19': 'spaghetti with pesto',
    '2021-05-20': 'chinese-style pork',
    '2021-05-21': 'pork steak',
    '2021-05-22': 'pizza de buu',
    '2021-05-23': 'coq au vin',
    '2021-05-24': 'ratatouille',
    '2021-05-26': 'beef with wine sauce',
    '2021-05-27': 'bean soup',
    '2021-05-28': 'funghi risotto',
    '2021-05-29': 'asparagus risotto',
    '2021-05-29b': 'tuna steak',
    '2021-05-30': 'roast chicken',
    '2021-06-01': 'pork steak',
    '2021-06-02': 'onigiri',
    '2021-06-03': 'ma-po tofu',
    '2021-06-04': 'nitsuke',
    '2021-06-05': 'deep-dish pizza',
    '2021-06-06': 'inari sushi',
    '2021-06-07': 'ratatouille',
    '2021-06-08': 'breaded beef steak',
    '2021-06-09': 'stuffed potatoes',
    '2021-06-09b': 'pasta bolognese',
    '2021-06-10': 'fried chicken',
    '2021-06-11': 'vodka pasta',
    '2021-06-12': 'fried chicken',
    '2021-06-12': 'ratatouille',
    '2021-06-13': 'roast chicken',
    '2021-06-14': 'yakisoba',
    '2021-06-15': 'chicken biryani',
    '2021-06-15': 'chicken with cabbage',
    '2021-06-17': 'pork with miso',
    '2021-06-18': 'funghi risotto',
    '2021-06-19': 'baguette sandwich',
    '2021-06-20': 'noodle soup',
    '2021-06-21': 'beef stew',
    '2021-06-22': 'pasta bolognese',
    '2021-06-23': 'beef teriyaki',
    '2021-06-24': 'ma-po tofu',
    '2021-06-25': 'potato salad',
    '2021-06-26': 'beef with manioc',
    '2021-06-27': 'pizza de buu',
    '2021-06-28': 'tempura udon',
    '2021-06-29': 'roast chicken',
    '2021-06-30': 'chao fan',
    '2021-07-01': 'lamen',
    '2021-07-02': 'gyoza',
    '2021-07-03': 'teok with shimeji',
    '2021-07-04': 'tomato risotto',
    '2021-07-04b': 'beef steak with funghi',
    '2021-07-05': 'ma-po tofu',
    '2021-07-06': 'roast chicken',
    '2021-07-07': 'chao fan',
    '2021-07-07b': 'chicken nuggets',
    '2021-07-08': 'cabbage rolls',
    '2021-07-09': 'ham and cheese sandwich',
    '2021-07-10': 'vietnamese shrimp rolls',
    '2021-07-11': 'nuggets',
    '2021-07-12': 'potato salad',
    '2021-07-13': 'noodle soup',
    '2021-07-14': 'ma-po tofu',
    '2021-07-15': 'tonkatsu',
    '2021-07-16': 'tomato honey chicken',
    '2021-07-16b': 'chicken with sliced potatoes',
    '2021-07-18': 'mifen',
    '2021-07-20': 'bean soup',
    '2021-07-21': 'nitsuke',
    '2021-07-23': 'mifen',
    '2021-07-25': 'chao fan',
    '2021-07-26': 'pasta bolognese',
    '2021-07-27': 'tom kha chicken',
    '2021-07-28': 'ma-po tofu',
    '2021-07-29': 'pork with miso',
    '2021-07-30': 'garlic bacon pasta',
    '2021-07-31': 'beef stew',
    '2021-08-01': 'noodle soup',
    '2021-08-02': 'nuggets',
    '2021-08-02b': 'fried manioc',
    '2021-08-03': 'omelet',
    '2021-08-04': 'potato salad',
    '2021-08-05': 'baloney sandwich',
    '2021-08-06': 'chickpea pie',
    '2021-08-08': 'roast chicken',
    '2021-08-09': 'hummus sandwich',
    '2021-08-10': 'pasta bolognese',
    '2021-08-11': 'ground beef with mixed veggies',
    '2021-08-12': 'pad thai',
    '2021-08-13': 'ma-po tofu',
    '2021-08-14': 'tempura',
    '2021-08-15': 'pork with broccoli',
    '2021-08-16': 'fried chicken',
    '2021-08-17': 'shimeji risotto',
    '2021-08-18': 'coq au vin',
    '2021-08-19': 'pasta with mussels',
    '2021-08-21': 'udon',
    '2021-08-22': 'potato salad',
    '2021-08-23': 'tomato honey pork',
    '2021-08-24': 'pasta with creamy bacon',
    '2021-08-25': 'roast chicken',
    '2021-08-26': 'beans with sausage',
    '2021-08-27': 'sausage soup',
    '2021-08-28': 'tomato risotto',
    '2021-08-29': 'cauliflower au gratin',
    '2021-08-30': 'lettuce wrap with chicken',
    '2021-08-31': 'lettuce wrap with chicken',
    '2021-09-02': 'ma-po tofu',
    '2021-09-05': 'eggplant lasagna',
    '2021-09-07': 'chicken vegetable soup',
    '2021-09-08': 'shredded chicken risotto',
    '2021-09-09': 'chicken crepes',
    '2021-09-13': 'napa cabbage and beans',
    '2021-09-15': 'mifen',
    '2021-09-17': 'pasta bolognese with soy protein',
    '2021-09-18': 'rice pilaf',
    '2021-09-21': 'roast chicken',
    '2021-09-26': 'beef wellington',
    '2021-09-27': 'lasagna',
    '2021-09-30': 'coq au vin',
    '2021-10-01': 'fried fish',
    '2021-10-01b': 'pad thai',
    '2021-10-02': 'chao fan',
    '2021-10-03': 'vegetable soup',
    '2021-10-04': 'kare udon',
    '2021-10-05': 'portobello risotto',
    '2021-10-06': 'chickpea and tomato salad',
    '2021-10-07': 'hot dog and fries',
    '2021-10-08': 'roast pork ribs',
    '2021-10-09': 'omelet',
    '2021-10-13': 'pasta with zucchini',
    '2021-10-14': 'chicken vegetable soup',
    '2021-10-15': 'chicken with cabbage',
    '2021-10-16': 'potato salad',
    '2021-10-16b': 'breaded beef strips',
    '2021-11-05': 'potato salad',
    '2021-11-05b': 'chicken fillets',
    '2021-11-06': 'pasta bolognese',
    '2021-11-06b': 'green beans salad',
    '2021-11-08': 'kare udon',
    '2021-11-09': 'mu-shu pork',
    '2021-11-10': 'coq au vin',
    '2021-11-11': 'velvet beef',
    '2021-11-12': 'gyoza',
    '2021-11-13': 'empanada',
    '2021-11-15': 'baked chicken',
    '2021-11-16': 'asparagus risotto',
    '2021-11-17': 'ratatouille',
    '2021-11-18': 'chicken stroganoff',
    '2021-11-21': 'rice pilaf',
    '2021-11-22': 'mac and cheese',
    '2021-11-23': 'fried chicken',
    '2021-11-24': 'vegetable curry',
    '2021-11-26': 'ma-po tofu',
    '2021-11-27': 'tom yum soup',
    '2021-11-28': 'chicken pot pie',
    '2021-11-29': 'baked rice',
    '2021-11-30': 'tomato honey chicken',
    '2021-12-01': 'portobello risotto',
    '2021-12-02': 'mu-shu pork',
    '2021-12-03': 'kibbeh',
    '2021-12-06': 'pasta with sausage',
    '2021-12-07': 'roast chicken',
    '2021-12-08': 'fried chicken',
    '2021-12-08b': 'potato salad',
    '2022-01-23': 'roast chicken',
    '2022-01-24': 'portobello risotto',
    '2022-01-25': 'jeyuk bokkeum',
    '2022-01-27': 'chicken fillets',
    '2022-01-27b': 'fried kale',
    '2022-01-28': 'chicken chao fan',
    '2022-01-29': 'potato salad',
    '2022-01-30': 'roast chicken',
    '2022-01-31': 'pasta carbonara',
    '2022-02-01': 'hamburgers',
    '2022-02-02': 'chicken stroganoff',
    '2022-02-03': 'jeyuk bokkeum',
    '2022-02-05': 'pork miso udon',
    '2022-02-06': 'chicken burger',
    '2022-02-08': 'carne de panela',
    '2022-02-09': 'kare rice',
    '2022-02-10': 'champignon risotto',
    '2022-02-11': 'pasta bolognese',
    '2022-02-12': 'porridge with garlic miso',
    '2022-02-14': 'mac and cheese',
    '2022-02-15': 'chicken thighs with onion',
    '2022-02-17': 'tonkatsu',
    '2022-02-17b': 'miso shiru',
    '2022-02-18': 'potato salad',
    '2022-02-19': 'beet salad',
    '2022-02-20': 'tuna mayo pasta',
    '2022-02-20b': 'coq au vin',
    '2022-02-21': 'nitsuke',
    '2022-02-22': 'bifum',
    '2022-02-23': 'kung pao chicken',
    '2022-02-24': 'chao fan',
    '2022-02-25': 'hamburgers',
    '2022-02-26': 'beans',
    '2022-02-26b': 'hummus',
    '2022-02-27': 'kare udon',
    '2022-02-28': 'mu-shu pork',
    '2022-02-28b': 'dadinho de tapioca',
    '2022-03-01': 'grilled beef steak',
    # '2022-03-02': '',
    # '2022-03-03': '',
    # '2022-03-04': '',
    # '2022-03-05': '',
    # '2022-03-06': '',
    '2022-03-07': 'meatloaf',
    '2022-03-08': 'tomato honey chicken',
    '2022-03-09': 'cod w/ tomato sauce',
    '2022-03-10': 'chicken with cabbage',
})


def histogram(start_date='2000-01-01'):
    c = Counter(d[1] for d in dinners.items() if d[0] >= start_date)
    return sorted([f"{'%02d' % item[1]} {item[0]}" for item in reversed(c.most_common()) if item[0] != ''])


def when_made(search_term):
    print('\n'.join(f"{date}: {dish}" for date, dish in dinners.items() if search_term in dish))


def pretty_print():
    print('\n'.join(f"{date}: {dish}" for date, dish in dinners.items() if dish != ''))


def print_histogram(start_date='2000-01-01'):
    print('\n'.join(histogram(start_date)))
