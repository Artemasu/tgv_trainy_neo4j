import pandas as pd
from neo4j import GraphDatabase
from nettoyage import preparer_donnees 

URI = "bolt://13.218.194.110"
AUTH = ("neo4j", "centerline-apparatuses-deck")

def configurer_base(session):
    print("Configuration des index")
    session.run("CREATE CONSTRAINT gare_iata IF NOT EXISTS FOR (g:Gare) REQUIRE g.code_iata IS UNIQUE")

def importer_donnees_opti(session, df_nodes, df_rels):
    # Les Gares
    query_nodes = "UNWIND $batch AS l MERGE (g:Gare {code_iata: l.iata}) SET g.ville = l.ville"
    session.run(query_nodes, batch=df_nodes.to_dict('records'))

    # Les Trajets
    query_rels = """
    UNWIND $batch AS l
    MATCH (dep:Gare {code_iata: l['Origine IATA']})
    MATCH (arr:Gare {code_iata: l['Destination IATA']})
    CREATE (dep)-[:TRAJET {
        `n°`: l.TRAIN_NO,
        `heure départ`: l.Heure_depart,
        `heure arrivée`: l.Heure_arrivee,
        dates: l.DATE
    }]->(arr)
    """
    dict_rels = df_rels.to_dict('records')
    chunk_size = 5000
    for i in range(0, len(dict_rels), chunk_size):
        batch = dict_rels[i:i + chunk_size]
        session.run(query_rels, batch=batch)
        print(f"Importation : {min(i + chunk_size, len(dict_rels))} / {len(dict_rels)}", end='\r')
    print("\nImportation terminée.")

def main():
    driver = GraphDatabase.driver(URI, auth=AUTH)
    with driver.session() as session:
        nb_gares = session.run("MATCH (g:Gare) RETURN count(g) AS nb").single()["nb"]

        if nb_gares == 0:
            df_nodes, df_rels = preparer_donnees('tgvmax.csv')
            configurer_base(session)
            importer_donnees_opti(session, df_nodes, df_rels)
        else:
            print(f"Base déjà alimentée ({nb_gares} gares).")

    driver.close()

if __name__ == "__main__":
    main()