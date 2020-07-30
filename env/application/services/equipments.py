from application.services.auth import make_connection
from application.services.company import detail
from application.model import connection_db

import http.client
import json

db_cursor = connection_db.cursor
ticket_teste = {}
tickets_by_equip = []
ticket_counts = 0


def equipments_list():
    conn, headers = make_connection()
    detail_list = detail()
    results_tratados = []

    #company_id = 0
    for company in detail_list:
        if company["tipo"] != 5:
            company_id = company["id"]
            conn.request(
                "GET", "/api/v2/equipamentos_paginados/?empresa_id={}".format(company_id), None, headers)
            res = conn.getresponse()
            data = json.loads(res.read())
            resultados = data['results']
            for equipment in resultados:
                equipment.pop("procedimentos")
                equipment.pop("identificacao")
                equipment.pop("qr_code")
                equipment.pop("tipo_contrato")
                equipment.pop("contratante")
                results_tratados.append(equipment)
    # for equip in enumerate(results_tratados, start=1):

    for equip in enumerate(results_tratados, start=1):
        ticket_counts = (get_equip_tickets(
            equip[1]['id'], equip[1]['tipo']['descricao']))
        # db_cursor.execute("INSERT INTO Equipment_Details (id, fabricante, modelo, patrimonio, numero_serie, id_proprietario, nome_proprietario, apelido_proprietario, id_tipo, descricao_tipo, quantidade_tickets) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        #                  (equip[1]['id'], equip[1]['fabricante'], equip[1]['modelo'],  equip[1]['patrimonio'], equip[1]['numero_serie'], equip[1]['proprietario']['id'], equip[1]['proprietario']['nome'], equip[1]['proprietario']['apelido'], equip[1]['tipo']['id'], equip[1]['tipo']['descricao'],ticket_counts,))
        # connection_db.db.commit()

    for ticks in enumerate(tickets_by_equip, start=1):
        db_cursor.execute("INSERT INTO Equipment_Tickets (id_ticket, numero_ticket, prop_ticket, equipamento_ticket) values (?, ?, ?, ?)",
                          (ticks[1]['id'], ticks[1]['numero'], ticks[1]['solicitante'], ticks[1]['equip_nome'],))
        connection_db.db.commit()

    connection_db.db.close()

    return None


def get_equip_tickets(equip_id, equip_nome):
    conn, headers = make_connection()
    conn.request(
        "GET", "/api/v2/chamado/?equipamento_id={}".format(equip_id), None, headers)
    res = conn.getresponse()
    data = json.loads(res.read())
    teste = data['results']
    for tickets in enumerate(teste, start=1):
        tickets_by_equip.append({
            'id': tickets[1]['id'],
            'numero': tickets[1]['numero'],
            'solicitante': tickets[1]['get_solicitante'],
            'equip_nome': equip_nome
        })
        ticket_counts = len(teste)
    
    return ticket_counts
