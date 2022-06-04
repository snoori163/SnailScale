from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response



import scraping

from pyramid.response import Response, FileResponse



id = 0
value_cal = 0
value_fat = 0
value_protein = 0
value_fiber = 0
value_carb = 0
value_chol = 0

cal1 = 0
fat1 = 0
protein1 = 0
fiber1 = 0
carb1 = 0
chol1 = 0
cal2 = 0
fat2 = 0
protein2 = 0
fiber2 = 0
carb2 = 0
chol2 = 0
cal3 = 0
fat3 = 0
protein3 = 0
fiber3 = 0
carb3 = 0
chol3 = 0

item_1 = " "
item_2 = " "
item_3 = " "


def get_home(req):
  return FileResponse("index.html")

#when user clicks start button and items has to appear on confirm section
def get_item(req):
    global item_1
    global item_2
    global item_3
    item_1, item_2, item_3 = scraping.get_class()
    
    return {"item1" : item_1,
            "item2" : item_2,
            "item3" : item_3}
    

def get_operation(req):
    idx = int(req.matchdict['operation_id'])
    global value_cal
    global value_fat
    global value_protein
    global value_fiber
    global value_carb
    global value_chol
    
    #make global
    
    global cal1
    global fat1
    global protein1
    global fiber1
    global carb1
    global chol1
    global cal2
    global fat2
    global protein2
    global fiber2
    global carb2
    global chol2
    global cal3
    global fat3
    global protein3
    global fiber3
    global carb3
    global chol3
    global id
    print(id)
    if idx == 1:
        cal1, fat1, protein1, fiber1, carb1, chol1, cal2, fat2, protein2, fiber2, carb2, chol2, cal3, fat3, protein3, fiber3, carb3, chol3 = scraping.get_value()
        
    #call start/add
        if id == 1:
            value_cal = value_cal + cal1
            value_fat = value_fat + fat1
            value_protein = value_protein + protein1
            value_fiber = value_fiber + fiber1
            value_carb = value_carb + carb1
            value_chol = value_chol + chol1
            
        if id == 2:
            value_cal = value_cal + cal2
            value_fat = value_fat + fat2
            value_protein = value_protein + protein2
            value_fiber = value_fiber + fiber2
            value_carb = value_carb + carb2
            value_chol = value_chol + chol2
            
        if id == 3:
            value_cal = value_cal + cal3
            value_fat = value_fat + fat3
            value_protein = value_protein + protein3
            value_fiber = value_fiber + fiber3
            value_carb = value_carb + carb3
            value_chol = value_chol + chol3
        
    if idx == 2:
        #call remove
        if id == 1:
            value_cal = value_cal - cal1
            value_fat = value_fat - fat1
            value_protein = value_protein - protein1
            value_fiber = value_fiber - fiber1
            value_carb = value_carb - carb1
            value_chol = value_chol - chol1
        if id == 2:
            value_cal = value_cal - cal2
            value_fat = value_fat - fat2
            value_protein = value_protein - protein2
            value_fiber = value_fiber - fiber2
            value_carb = value_carb - carb2
            value_chol = value_chol - chol2
        if id == 3:
            value_cal = value_cal - cal3
            value_fat = value_fat - fat3
            value_protein = value_protein - protein3
            value_fiber = value_fiber - fiber3
            value_carb = value_carb - carb3
            value_chol = value_chol - chol3


    if idx == 3:
        #call clear
        value_cal = 0
        value_fat = 0
        value_protein = 0
        value_fiber = 0
        value_carb = 0
        value_chol = 0
        
        cal1 = 0
        fat1 = 0
        protein1 = 0
        fiber1 = 0
        carb1 = 0
        chol1 = 0
        cal2 = 0
        fat2 = 0
        protein2 = 0
        fiber2 = 0
        carb2 = 0
        chol2 = 0
        cal3 = 0
        fat3 = 0
        protein3 = 0
        fiber3 = 0
        carb3 = 0
        chol3 = 0

        
    
        

        
def get_facts(req):
    idx = int(req.matchdict['confirm_id'])
    global id
    id = idx
    cal1, fat1, protein1, fiber1, carb1, chol1, cal2, fat2, protein2, fiber2, carb2, chol2, cal3, fat3, protein3, fiber3, carb3, chol3 = scraping.get_value()

    if idx == 1:
        return { "cal" : cal1,
                 "fat" : fat1,
                 "pro" : protein1,
                 "fib" : fiber1,
                 "car" : carb1,
                 "chol": chol1
                 }
                 
    if idx == 2:
        return { "cal" : cal2,
                 "fat" : fat2,
                 "pro" : protein2,
                 "fib" : fiber2,
                 "car" : carb2,
                 "chol": chol2}

    if idx == 3:
        return { "cal" : cal3,
                 "fat" : fat3,
                 "pro" : protein3,
                 "fib" : fiber3,
                 "car" : carb3,
                 "chol": chol3}

def get_sum(req):

    print(value_cal, value_fat, value_protein, value_fiber, value_carb, value_chol)
  
    return { "cal" : value_cal,
             "fat" : value_fat,
             "pro" : value_protein,
             "fib" : value_fiber,
             "car" : value_carb,
             "chol": value_chol}
                 

  

''' Route Configurations '''

if __name__ == '__main__':

    with Configurator() as config:

        # route for home page

        config.add_route('home', '/')
        config.add_view(get_home, route_name='home')
  
        
#        config.add_route('get_operation', '/operation/{operation_id}')
#        config.add_view(get_operation, route_name='get_operation', renderer='json')
        
        config.add_route('get_item','/start/')
        config.add_view(get_item, route_name='get_item', renderer='json')

        config.add_route('facts', '/confirm/{confirm_id}')
        config.add_view(get_facts, route_name='facts', renderer='json')

 
        config.add_route('get_operation', '/operation/{operation_id}')
        config.add_view(get_operation, route_name='get_operation', renderer='json')

  #route for returning nutrition
#        config.add_route('facts', '/confirm/{confirm_id}')
#        config.add_view(get_facts, route_name='facts', renderer='json')
        
        config.add_route('total', '/total/')
        config.add_view(get_sum, route_name='total', renderer='json')


        config.add_static_view(name='/', path='./public', cache_max_age=3600)

        

        app = config.make_wsgi_app()


        

server = make_server('0.0.0.0', 6544, app)

print('Web server started on: http://0.0.0.0:6544')

server.serve_forever()
