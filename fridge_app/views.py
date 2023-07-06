from django.shortcuts import render

item_list = [
    {
        "id": 1,
        "name": "Apple",
        "category": "Fruits",
        "qty": 10,
        "fridge_id": 1,
        "expiry_date": "2023-03-09T22:00:00"
    },
    {
        "id": 2,
        "name": "Beef",
        "category": "Meat",
        "qty": 1,
        "fridge_id": 1,
        "expiry_date": "2023-03-10T22:00:00"
    },
    {
        "id": 3,
        "name": "Eggs",
        "category": "Diary",
        "qty": 12,
        "fridge_id": 1,
        "expiry_date": "2023-03-09T22:00:00"
    },
    {
        "id": 4,
        "name": "Milk",
        "category": "Diary",
        "qty": 2,
        "fridge_id": 2,
        "expiry_date": "2023-03-19T22:00:00"
    },
]

members = [
    {
        "name": "Kyaw Min Thu",
        "id": "gb6499",
    },
    {
        "name": "Nayan Pai",
        "id": "bp3398",
    },
    {
        "name": "Sarthak Adhikari",
        "id": "bv9292",
    },
    {
        "name": "Yichao Hao",
        "id": "ur5215",
    }
]


# Create your views here.
def home(request):
    context = {
        'item_list': item_list,
        'title': 'Home',
    }
    return render(request, 'fridge_app/home.html', context)


def about(request):
    context = {
        'members': members,
        'title': 'About',
    }
    return render(request, 'fridge_app/about.html', context)
