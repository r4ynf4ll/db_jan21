import gradio as gr
import pandas as pd
import sqlite3

def fetch():
    conn = sqlite3.connect('playoffs.db')
    cursor = conn.cursor()
    query = """
        SELECT *
        FROM teams
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    records_df = pd.DataFrame(records,columns=['id','city','name'])
    return records_df

iface = gr.Interface(fn = fetch,inputs=[],outputs=gr.Dataframe(headers=['id','city','name']))

iface.launch()