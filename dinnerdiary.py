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


dish_ingredients = {
    'asparagus risotto': ['rice', 'vegetables'],
    'baguette sandwich': ['bread', 'cold cuts'],
    'baked chicken': ['chicken', 'potatoes'],
    'baked milanese': ['chicken'],
    'baked rice': ['rice'],
    'baloney sandwich': ['bread', 'cold cuts'],
    'bean soup': ['beans'],
    'bean, pork and kale soup': ['beans', 'pork', 'vegetables'],
    'beans': ['beans'],
    'beans with sausage': ['beans', 'sausages'],
    'beef steak with funghi': ['beef', 'mushrooms'],
    'beef steak with worcestershire sauce': ['beef'],
    'beef stew': ['beef', 'potatoes', 'vegetables'],
    'beef teriyaki': ['beef'],
    'beef wellington': [],  # do not show in searches
    'beef with manioc': ['beef', 'manioc'],
    'beef with wine sauce': ['beef'],
    'beet salad': ['vegetables'],
    'bifum': ['noodles'],
    'breaded beef steak': ['beef'],
    'breaded beef strips': ['beef'],
    'burgers': ['ground meat'],
    'cabbage rolls': ['ground meat', 'cabbage'],
    'carne de panela': ['beef', 'potatoes', 'carrots'],
    'cauliflower au gratin': ['vegetables'],
    'champignon risotto': ['rice', 'mushrooms'],
    'chao fan': ['rice', 'vegetables'],
    'chicken burger': ['ground meat', 'chicken'],
    'chicken chao fan': ['rice', 'chicken', 'vegetables'],
    'chicken crepes': ['chicken'],
    'chicken fillets': ['chicken'],
    'chicken nuggets': ['chicken', 'fried'],
    'chicken pot pie': ['chicken', 'cream', 'vegetables'],
    'chicken stroganoff': ['chicken', 'cream'],
    'chicken thighs with onion': ['chicken'],
    'chicken vegetable soup': ['chicken', 'vegetables'],
    'chicken with cabbage': ['chicken', 'cabbage'],
    'chicken with miso': ['chicken', 'miso'],
    'chicken with sliced potatoes': ['chicken', 'potatoes'],
    'chickpea and tomato salad': ['chickpeas', 'tomatoes'],
    'chickpea pie': ['chickpeas'],
    'chinese-style pork': ['pork', 'vegetables'],
    'cod w/ tomato sauce': ['fish', 'tomato sauce'],
    'coleslaw': ['cabbage', 'carrots'],
    'coq au vin': ['chicken', 'bacon', 'mushrooms'],
    'dadinho de tapioca': ['fried', 'tapioca'],
    'deep-dish pizza': ['bread', 'cheese'],
    'eggplant lasagna': ['vegetables', 'cream', 'tomato sauce'],
    'empanada': ['bread', 'ground meat'],
    'esfiha': ['bread', 'ground meat'],
    'fried chicken': ['chicken', 'fried'],
    'fried fish': ['fish', 'fried'],
    'fried kale': ['vegetables'],
    'fried manioc': ['manioc'],
    'funghi risotto': ['rice', 'mushrooms'],
    'garlic bacon pasta': ['bacon', 'pasta'],
    'gizzards with onion': ['gizzards'],
    'green beans salad': ['vegetables'],
    'grilled beef steak': ['beef'],
    'ground beef with mixed veggies': ['ground meat', 'vegetables'],
    'gyoza': ['ground meat', 'dumplings'],
    'ham and cheese sandwich': ['cold cuts', 'bread'],
    'heart of palm salad': ['vegetables'],
    'hijiki gohan': ['rice', 'mushrooms'],
    'hot dog and fries': ['bread', 'sausages'],
    'hummus': ['chickpeas'],
    'hummus sandwich': ['bread', 'chickpeas'],
    'inari sushi': ['rice'],
    'jeyuk bokkeum': ['pork', 'hot sauce'],
    'kare rice': ['rice', 'ground meat', 'spices'],
    'kare udon': ['noodles', 'ground meat', 'spices'],
    'kibbeh': ['ground meat', 'grains'],
    'kung pao chicken': ['chicken', 'vegetables'],
    'lamen': ['noodles'],
    'lasagna': ['pasta', 'cream', 'ground meat', 'tomato sauce'],
    'lettuce wrap with chicken': ['lettuce', 'chicken'],
    'ma-po tofu': ['tofu', 'ground meat', 'hot sauce'],
    'mac and cheese': ['pasta', 'cheese', 'cream'],
    'meatloaf': ['ground meat'],
    'mifen': ['noodles'],
    'miso shiru': ['miso', 'vegetables'],
    'miso udon': ['miso', 'noodles'],
    'mu-shu pork': ['pork', 'mushrooms', 'eggs'],
    'mussels pasta': ['seafood', 'pasta'],
    'napa cabbage and beans': ['vegetables'],
    'nitsuke': ['soup', 'yams', 'vegetables', 'beef'],
    'noodle soup': ['soup', 'noodles', 'vegetables'],
    'omelet': ['eggs'],
    'onigiri': ['rice'],
    'pad thai': ['noodles'],
    'panqueca de carne': ['ground meat', 'tomato sauce', 'crepes'],
    'pasta bolognese': ['pasta', 'ground meat', 'tomato sauce'],
    'pasta bolognese with soy protein': ['pasta', 'tomato sauce', 'soy protein'],
    'pasta carbonara': ['pasta', 'eggs', 'bacon'],
    'pasta with creamy bacon': ['pasta', 'cream', 'bacon'],
    'pasta with mussels': ['pasta', 'seafood', 'tomato sauce'],
    'pasta with sausage': ['pasta', 'tomato sauce', 'sausages'],
    'pasta with zucchini': ['pasta', 'tomato sauce', 'vegetables'],
    'pizza de buu': ['bread', 'cheese', 'tomato sauce'],
    'pizza de key': ['bread', 'cheese', 'tomato sauce'],
    'pork loin with bell peppers': ['pork', 'vegetables'],
    'pork miso udon': ['pork', 'noodles', 'miso'],
    'pork steak': ['pork'],
    'pork with broccoli': ['pork', 'vegetables'],
    'pork with miso': ['pork', 'miso'],
    'porridge with garlic miso': ['rice', 'miso'],
    'portobello risotto': ['rice', 'mushrooms'],
    'potato salad': ['potatoes', 'carrots', 'eggs'],
    'ratatouille': ['vegetables'],
    'rice pilaf': ['rice', 'vegetables'],
    'roast chicken': ['chicken', 'potatoes', 'carrots'],
    'roast pork ribs': ['pork'],
    'sausage soup': ['sausages', 'soup'],
    'shimeji risotto': ['rice', 'mushrooms'],
    'shredded chicken risotto': ['chicken', 'rice'],
    'soy bolognese pasta': ['soy protein', 'tomato sauce', 'pasta'],
    'spaghetti with meatballs': ['pasta', 'ground meat', 'tomato sauce'],
    'spaghetti with pesto': ['pasta', 'pesto'],
    'stuffed potatoes': ['potatoes', 'cheese'],
    'stuffed zucchini': ['vegetables', 'ground meat'],
    'sushi': ['rice', 'eggs', 'kani'],
    'tempura': ['fried', 'vegetables'],
    'tempura udon': ['fried', 'vegetables', 'noodles'],
    'teok with shimeji': ['mushrooms', 'rice cakes'],
    'tom kha chicken': ['chicken', 'soup'],
    'tom yum soup': ['shrimps', 'soup', 'hot sauce'],
    'tomato honey chicken': ['tomatoes', 'chicken', 'carrots'],
    'tomato honey pork': ['tomatoes', 'pork', 'carrots'],
    'tomato risotto': ['rice', 'tomatoes'],
    'tonkatsu': ['pork', 'fried'],
    'tuna mayo pasta': ['tuna', 'pasta'],
    'tuna steak': ['tuna'],
    'udon': ['noodles'],
    'vegetable curry': ['vegetables', 'spices'],
    'vegetable soup': ['vegetables', 'soup'],
    'velvet beef': ['beef', 'vegetables'],
    'vietnamese shrimp rolls': ['shrimps', 'carrots'],
    'vodka pasta': ['pasta', 'cream'],
    'yakisoba': ['noodles', 'beef', 'vegetables', 'cabbage', 'carrots'],
}

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
    '2021-07-11': 'chicken nuggets',
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
    '2021-08-02': 'chicken nuggets',
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
    '2022-02-01': 'burgers',
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
    '2022-02-25': 'burgers',
    '2022-02-26': 'beans',
    '2022-02-26b': 'hummus',
    '2022-02-27': 'kare udon',
    '2022-02-28': 'mu-shu pork',
    '2022-02-28b': 'dadinho de tapioca',
    '2022-02-28c': 'heart of palm salad',
    '2022-03-01': 'grilled beef steak',
    '2022-03-03': 'portobello risotto',
    '2022-03-04': 'soy bolognese pasta',
    '2022-03-05': 'esfiha',
    '2022-03-06': 'carne de panela',
    '2022-03-07': 'meatloaf',
    '2022-03-08': 'tomato honey chicken',
    '2022-03-09': 'cod w/ tomato sauce',
    '2022-03-10': 'chicken with cabbage',
    '2022-03-11': 'chao fan',
    '2022-03-12': 'panqueca de carne',
    '2022-03-13': 'roast chicken',
    '2022-03-14': 'gizzards with onion',
    '2022-03-15': 'miso udon',
    '2022-03-17': 'sushi',
    '2022-03-19': 'portobello risotto',
    '2022-03-19b': 'ma-po tofu',
    '2022-03-20': 'roast chicken',
    '2022-03-21': 'vegetable soup',
    '2022-03-22': 'beef teriyaki',
    '2022-03-22b': 'ground beef with mixed veggies',
    '2022-03-23': 'mu-shu pork',
    '2022-03-24': 'kare udon',
    '2022-03-25': 'potato salad',
    '2022-03-27': 'mussels pasta',
    '2022-03-27b': '',
    '2022-03-28': '',
    '2022-03-29': '',
    '2022-03-30': '',
    '2022-03-31': '',
})


def histogram(start_date='2000-01-01'):
    c = Counter(d[1] for d in dinners.items() if d[0] >= start_date)
    return sorted([f"{'%02d' % item[1]} {item[0]}" for item in reversed(c.most_common()) if item[0] != ''])


def when_made(search_term):
    last_made = ""
    for date, dish in dinners.items():
        if search_term in dish:
            last_made = date
    return f"{last_made}: {search_term}"


def pretty_print():
    print('\n'.join(f"{date}: {dish}" for date, dish in dinners.items() if dish != ''))


def print_histogram(start_date='2000-01-01'):
    print('\n'.join(histogram(start_date)))


def check_ingredients_dict():
    """Check that all dishes in 'dinners' are in dish_ingredients"""
    if len(set(dinners.values())) == len(dish_ingredients):
        print("Ingredients check: OK")
    else:
        missing = set(dinners.values()) - dish_ingredients.keys()
        print(sorted(missing), "are missing ingredients in the dish_ingredients dict")


def main_ingredients():
    """Collect distinct ingredients from lists in dish_ingredients"""
    for ingr in sorted(set(ingr for dish_list in dish_ingredients.values() for ingr in dish_list)):
        print(ingr)


def with_ingredient(ingr):
    """Return all dishes with ingredient ingr"""
    matches = set(d for d in dish_ingredients if ingr in dish_ingredients[d])
    match_when = sorted([when_made(d) for d in matches], reverse=True)
    for m in match_when:
        print(m)


# call when sending whole file
check_ingredients_dict()

print("""Usage:

print_histogram('2000-01-01') shows how many times a dish was made since the given date. Without a date, all entries are counted.
main_ingredients() prints broad categories of ingredients used.
with_ingredient(ingr) prints dishes containing ingr and the last time it was made.
check_ingredients_dict() checks if the two data dictionaries agree.
""")
