from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import csv

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),   
}

dag = DAG(
    'ejemplo_airflow_datos_api',
    default_args=default_args,
    description='DAG que descarga, procesa y guarda datos de una api en un CSV',
    schedule_interval=timedelta(days=1),
)

def descargar_datos():
    url = "https://api.ejemplo-com/datos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error al descargar los datos")
    
def procesar_datos(ti):
    datos = ti.xcom_pull (task_ids='descargar_datos')
    datos_procesados = [{'id': item ['id'], 'nombre': item['nombre'], 'valor': item['valor']} for item in datos]
    return datos_procesados

def guardar_en_csv(ti):
    datos_procesados = ti.xcom_pull (task_ids='procesar_datos')
    with open('/path/a/tu/archivo.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'nombre', 'valor'])
        writer.writeheader()
        writer.writerows(datos_procesados)

tarea_descargar = PythonOperator(
    task_id='procesar_datos',
    python_callable=procesar_datos,
    provide_context=True,
    dag=dag,
)

tarea_procesar = PythonOperator(
    task_id='procesar_datos',
    python_callable=procesar_datos,
    provide_context=True,
    dag=dag,
)

tarea_guardar = PythonOperator(
    task_id='guardar_en_csv',
    python_callable=guardar_en_csv,
    provide_context=True,
    dag=dag,
)

tarea_descargar >> tarea_procesar >> tarea_guardar