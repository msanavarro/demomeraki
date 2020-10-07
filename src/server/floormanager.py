'''
Created on 7 oct. 2020

@author: msanavarro
'''
def visits_table_helper(locationdata):
    db = get_db()
    #  ESTE CICLO REVISA Y REGISTRA LAS LLEGADAS
    if (locationdata["data"]["apFloors"][0] == "Planta Baja"):
        db.execute(
                'INSERT INTO slice (datetime, floor0)'
                    ' VALUES (CURRENT_TIMESTAMP, ?)',
                    (len(locationdata['data']['observations']),)
                )
        db.commit()
    else if (locationdata["data"]["apFloors"][0] == "Piso 1"):
        db.execute(
                'INSERT INTO slice (datetime, floor1)'
                    ' VALUES (CURRENT_TIMESTAMP, ?)',
                    (len(locationdata['data']['observations']),)
                )
        db.commit()
    else if (locationdata["data"]["apFloors"][0] == "Piso 2"):
        db.execute(
                'INSERT INTO slice (datetime, floor2)'
                    ' VALUES (CURRENT_TIMESTAMP, ?)',
                    (len(locationdata['data']['observations']),)
                )
        db.commit()
    else if (locationdata["data"]["apFloors"][0] == "Piso 3"):
        db.execute(
                'INSERT INTO slice (datetime, floor3)'
                    ' VALUES (CURRENT_TIMESTAMP, ?)',
                    (len(locationdata['data']['observations']),)
                )
        db.commit()
    else:
        print("No esta registrado este piso")
    
    return