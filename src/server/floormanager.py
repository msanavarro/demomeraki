'''
Created on 7 oct. 2020

@author: msanavarro
'''
def visits_table_helper(locationdata):
    db = get_db()
    #  ESTE CICLO REVISA Y REGISTRA LAS LLEGADAS
    if (locationdata["data"]["apFloors"][0] == "Planta Baja"):
        db.execute(
                'INSERT INTO visits (macaddr, name, timesseen, averagestay)'
                    ' VALUES (?, ?, ?, ?)',
                    (value["clientMac"],"Cambiar nombre", 1, 0)
                )
            db.commit()
    for value in locationdata["data"]["observations"] :
        macaddr = (value["clientMac"],)
        exists = db.execute("SELECT EXISTS(SELECT 1 FROM visits WHERE macaddr=?)", macaddr)
        if(exists.fetchone()[0]==0):
            db.execute(
                'INSERT INTO visits (macaddr, name, timesseen, averagestay)'
                    ' VALUES (?, ?, ?, ?)',
                    (value["clientMac"],"Cambiar nombre", 1, 0)
                )
            db.commit()
        else:
            # PENDIENTE CAMBIAR CONSULTAS POR UNA SOLA LECTURA QUE TOME TODO Y LO META EN UN DICCIONARIO
            lastarrivaltime = list(db.execute("SELECT lastarrivaltime FROM visits WHERE macaddr=?", macaddr).fetchone())[0]
            lastexittime = list(db.execute("SELECT lastexittime FROM visits WHERE macaddr=?", macaddr).fetchone())[0]
            timesseen = list(db.execute("SELECT timesSEEN FROM visits WHERE macaddr=?", macaddr).fetchone())[0]
            if(lastarrivaltime >= lastexittime):
                print('{} está en el edificio'.format(macaddr[0]))
            else:
                db.execute(
                    'UPDATE visits SET lastarrivaltime = CURRENT_TIMESTAMP WHERE macaddr = ?', 
                    (value["clientMac"],)
                    )
                db.commit()
                print('{} acaba de entrar al edificio'.format(macaddr))
    #  ESTE CICLO REVISA Y REGISTRA LAS SALIDAS
    cursor = db.cursor()
    cursor.execute(
        'SELECT * FROM visits'
    )
    rows = cursor.fetchall()
    dbdata = []
    for row in rows:
        macaddr = (row['macaddr'],)
        if (any(d['clientMac'] == row['macaddr'] for d in locationdata['data']['observations'])):
            print('{} sigue en el edificio'.format(row['macaddr']))
        else:
            lastarrivaltime = list(db.execute("SELECT lastarrivaltime FROM visits WHERE macaddr=?", macaddr).fetchone())[0]
            lastexittime = datetime.datetime.now() #list(db.execute("SELECT CURRENT_TIMESTAMP", macaddr).fetchone())[0]
            timesseen = list(db.execute("SELECT timesseen FROM visits WHERE macaddr=?", macaddr).fetchone())[0]
            averagestay = list(db.execute("SELECT averagestay FROM visits WHERE macaddr=?", macaddr).fetchone())[0]
            print(lastarrivaltime, lastexittime)
            newavgstay = (timesseen*averagestay +(lastexittime - lastarrivaltime).total_seconds())/(timesseen+1)
            db.execute(
                    'UPDATE visits SET lastexittime = CURRENT_TIMESTAMP, timesseen = ?, averagestay = ? WHERE macaddr = ?', 
                    (timesseen + 1, newavgstay, row['macaddr'])
                    )
            db.commit()
            print('{} salió del edificio'.format(row['macaddr']))
    return