from application.services.auth import make_connection
from application.model import connection_db
import itertools
import http.client
import json
def chosen_list():
    conn, headers = make_connection()
    conn.request("GET", "/api/v2/empresa/", None, headers)
    res = conn.getresponse()
    data = res.read()
    company_list = json.loads(data)   
    #indices_to_access = [3, 4 , 5 , 83 , 10, 18, 101, 107, 110, 114, 119, 120, 213, 212, 14, 125, 126, 128, 21,113]
    #accessed_mapping = map(company_list.__getitem__, indices_to_access)
    #list_to_access = list(accessed_mapping) 
    return company_list

def detail():
    company_list = chosen_list()    
    conn, headers = make_connection()    
    indices_to_access = [3, 4 , 5 , 83 , 10, 18, 101, 107, 110, 114, 119, 120, 213, 212, 14, 125, 126, 128, 21,113]
    accessed_mapping = map(company_list.__getitem__, indices_to_access)
    list_to_access = list(accessed_mapping)
    detail_list = []
    for company in list_to_access:
        comp_id = company["id"]        
        conn.request("GET", "/api/v2/company/{}/".format(comp_id), None, headers)
        res = conn.getresponse()
        data = res.read()
        detail_list.append(json.loads(data))           
            
    for empresa in enumerate(detail_list, start=1):
        pass
        connection_db.cursor.execute("INSERT OR REPLACE INTO Companies_Detailed (id, tipo, nome, nome_fantasia, superior, cnpj, observacoes, contato, email, telefone1, ramal1, telefone2, ramal2, fax, cep, rua, numero, complemento, bairro, cidade, estado) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (empresa[1]['id'], empresa[1]['tipo'], empresa[1]['nome'], empresa[1]['nome_fantasia'], empresa[1]['superior'], empresa[1]['cnpj'], empresa[1]['observacoes'], empresa[1]['contato'], empresa[1]['email'], empresa[1]['telefone1'], empresa[1]['ramal1'], empresa[1]['telefone2'], empresa[1]['ramal2'], empresa[1]['fax'], empresa[1]['cep'], empresa[1]['rua'], empresa[1]['numero'], empresa[1]['complemento'], empresa[1]['bairro'], empresa[1]['cidade'], empresa[1]['estado'],))
        connection_db.db.commit()
    return detail_list








         
