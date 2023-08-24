# Lee los IDs del archivo
with open('data_ids.csv', 'r') as file:
    ids = [line.strip() for line in file]

# Divide los IDs en lotes de 100
batched_ids = [ids[i:i+100] for i in range(0, len(ids), 100)]

# Genera las sentencias SQL por lote de IDs
batched_sql = []
for batch in batched_ids:
    id_list = ', '.join(batch)
    sql = f"UPDATE inventario SET estado = False WHERE ID IN ({id_list});"
    batched_sql.append(sql)

# Crea y escribe el archivo SQL con las sentencias en lotes
with open('update_batched.sql', 'w') as file:
    file.write('\n'.join(batched_sql))

print("Archivo SQL en lotes generados exitosamente.")
