from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	'my_list': [
    	{"restaurant_name": "China Town" , "food_type": "chinese"},
    	{"restaurant_name": "elevation burger" , "food_type": "burgers"},
    	{"restaurant_name": "papa jones" , "food_type": "pizzas"},
    	],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object": {
    		"restaurant_name": "China Town" ,
    		 "food_type": "chinese",
    	}

    }
    return render(request, 'detail.html', context)
