# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %md
# MAGIC # SESION 2: Tarea de Spark · Caso de negocio con `samples.tpch` 

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. El dataset: `samples.tpch`
# MAGIC
# MAGIC | Tabla | Qué es | Columnas que usaremos |
# MAGIC |---|---|---|
# MAGIC | `orders` | Un pedido por fila | `o_custkey`, `o_orderstatus`, `o_totalprice`, `o_orderdate` |
# MAGIC | `customer` | Un cliente por fila | `c_custkey`, `c_nationkey`, `c_mktsegment` |
# MAGIC | `nation` | Países (25) | `n_nationkey`, `n_name` |
# MAGIC
# MAGIC Se conectan así: `orders.o_custkey` → `customer.c_custkey` y `customer.c_nationkey` → `nation.n_nationkey`.
# MAGIC

# COMMAND ----------

from pyspark.sql import functions as F

orders   = spark.table("samples.tpch.orders")
customer = spark.table("samples.tpch.customer")
nation   = spark.table("samples.tpch.nation")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Preguntas de negocio

# COMMAND ----------

# MAGIC %md
# MAGIC ### Pregunta 1 · Pedidos por estado 
# MAGIC
# MAGIC ¿Cuántos pedidos hay en cada estado (`o_orderstatus`) y cuál es el monto total de cada uno?
# MAGIC
# MAGIC *Pista:* `groupBy` sobre `orders` con dos agregaciones: `count` y `sum` de `o_totalprice`.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### Pregunta 2 · Evolución anual 
# MAGIC ¿Cuántos pedidos y qué monto total hay por año (`o_orderdate`)? Ordena del año más antiguo al más reciente.
# MAGIC
# MAGIC *Pista:* Crea la columna `año` con `F.year(...)` y agrupa por ella.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### Pregunta 3 · Pedidos grandes ya finalizados 
# MAGIC
# MAGIC ¿Cuántos pedidos finalizados (`o_orderstatus` = `'F'`) tienen un monto (`o_totalprice`) mayor a 100,000?
# MAGIC
# MAGIC *Pista:* Usa `filter` con las dos condiciones unidas con `&` (cada una entre paréntesis) y luego `agg(F.count("*"))`.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### Pregunta 4 · Clientes por segmento
# MAGIC
# MAGIC ¿Cuántos clientes hay en cada segmento de mercado (`c_mktsegment`)? Ordénalos de mayor a menor.
# MAGIC
# MAGIC *Pista:* `groupBy` sobre `customer` y `count`.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### Pregunta 5 · Clientes por país
# MAGIC
# MAGIC ¿En qué 5 países (`n_name`) hay más clientes? Muestra el país y el número de clientes, de mayor a menor.
# MAGIC
# MAGIC *Pista:* Une `customer` con `nation` (`c_nationkey` = `n_nationkey`), agrupa por `n_name` y cuenta.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### Pregunta 6 · Ticket promedio por segmento
# MAGIC
# MAGIC ¿Cuál es el ticket promedio (monto promedio por pedido, `o_totalprice`) de cada segmento de mercado? Ordénalo de mayor a menor.
# MAGIC
# MAGIC *Pista:* Une `orders` con `customer` (`o_custkey` = `c_custkey`), agrupa por `c_mktsegment` y usa `F.avg`.

# COMMAND ----------

