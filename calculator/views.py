from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home(request):
    context = {
        'recipe_names': DATA.keys()
    }
    return render(request, 'home_page/home.html', context)


def all_recipes(request, recipe_name):
    res_ing_amount = {}
    ing_amount = DATA[recipe_name]
    servings = int(request.GET.get('servings'))
    for ing, amount in ing_amount.items():
        new_amount = round(amount * servings, 2)
        res_ing_amount[ing] = new_amount
    context = {
        'recipe_name': recipe_name,
        'recipe': res_ing_amount
    }
    return render(request, 'calculator/index.html', context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


# ДРУГОЕ РЕШЕНИЕ
# def omlet(request):
#     servings = int(request.GET.get('servings'))
#     context = {
#         'recipe': {
#             'яйца, шт': 2 * servings,
#             'молоко, л': round(0.1 * servings, 2),
#             'соль, ч.л.': round(0.5 * servings, 2),
#         }
#     }
#     return render(request, 'calculator/index.html', context)
#
# def pasta(request):
#     servings = int(request.GET.get('servings'))
#     context = {
#         'recipe': {
#             'макароны, г': round(0.3 * servings, 2),
#             'сыр, г': round(0.05 * servings, 3),
#         }
#     }
#     return render(request, 'calculator/index.html', context)
#
# def buter(request):
#     servings = int(request.GET.get('servings'))
#     context = {
#         'recipe': {
#             'хлеб, ломтик': 1 * servings,
#             'колбаса, ломтик': 1 * servings,
#             'сыр, ломтик': 1 * servings,
#             'помидор, ломтик': 1 * servings,
#         }
#     }
#     return render(request, 'calculator/index.html', context)




