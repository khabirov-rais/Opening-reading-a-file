def read_recipes(filename):
    cook_book = {}

    with open('recipes.txt', 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    for i in range(0, len(lines), 4):
        recipe_name = lines[i]
        num_ingredients = int(lines[i + 1])
        ingredients = [
            {
                'ingredient_name': ingredient.split(' | ')[0],
                'quantity': int(ingredient.split(' | ')[1]),
                'measure': ingredient.split(' | ')[2]
            }
            for ingredient in lines[i + 2: i + 2 + num_ingredients]
        ]
        cook_book[recipe_name] = ingredients

    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
 
    for dish in dishes:
        shop_list = {
            shop_list,
            {ingredient['ingredient_name']: {
                'measure': ingredient['measure'],
                'quantity': ingredient['quantity'] * person_count
            } for ingredient in cook_book.get(dish, [])}
        }

    return shop_list


def main():
    filename = 'recipes.txt'
    cook_book = read_recipes(filename)

    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2

    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print(shop_list)

if __name__ == '__main__':
    main()
