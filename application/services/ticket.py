from application.services.equipments import equipments_list
from application.services.auth import make_connection
from application.model import connection_db
import http.client
import json
import time


db_cursor = connection_db.cursor
db_cursor.execute("SELECT * from Equipment_Details")
records = db_cursor.fetchall()
millis = int(round(time.time() * 1000))

def make_ticket(id_equipamento, id_solicitante, tipo_servico, problema, observacoes, data_criacao, id_tipo_ordem_servico):
    conn, headers = make_connection()        
    chamadoteste = {'equipamento': id_equipamento, 'solicitante': id_solicitante, 'tipo_servico': tipo_servico, 'problema': problema, 'observacoes': observacoes, 'data_criacao': data_criacao, 'id_tipo_ordem_servico': id_tipo_ordem_servico}
    payload = json.dumps(chamadoteste)
    conn.request("POST", "/api/v1/chamado/novo/", payload, headers)
    res = conn.getresponse()
    data = res.read()    
    return chamadoteste

def send_ticket():
    for row in records:
        millis = int(round(time.time() * 1000))
        make_ticket(row[0],row[5], 3, 5, "Mesmo após socos e chutes, o equipamento curiosamente não liga. Não foi checado se estava ligado na tomada.", millis, 1)


       

