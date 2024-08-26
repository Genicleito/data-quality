# Data Quality
Repositório com scripts PySpark para verificação e validação de dados a partir de regras definidas em um JSON

## Arquivo com as definições de regras de validação das tabelas [dags/config.json](dags/config.json)

### Estrutura raiz do arquivo JSON com as configurações
```python
{
    "tables": [
        { # 'Table 1'
            "name": "TABLE_NAME",
            "alias": "TABLE_ALIAS", # Optional
            "filters": [...], # List of filters
            "validations": [...] # List of validation rules
        },
        ...
    ]
}
```

### Estrutura detalhada com exemplo da chave `filters`

Existem duas formas de definir regras de filtros para os dados. Por meio da definição de uma query personalizada **OU** por meio da definição de parâmetros com os nomes das colunas, operador e valor a ser filtrado. 

1. Abaixo segue um exemplo de filtro utilizando query, desse modo quaisquer outras chaves indicando nome da coluna ou operador serão ignoradas (a menos que estejam em outro contexto de condição e não no mesmo escopo `{...}`):

```python
{
    ...
    "filters": [
        {
            "query": "COLUMN_NAME_A = 'active'",
        },
        ...
    ],
    ...
}
```

2. Abaixo segue um exemplo utilizando operadores para definir as regras de filtro que deverão ser aplicadas. Ambas as formas podem ser combinadas para múltiplas validações:
```python
{
    ...
    "filters": [
        {
            "column": "COLUMN_NAME_A",
            "operator": "=",
            "value": "active"
        },
        {
            "column": "COLUMN_NAME_B",
            "operator": ">",
            "value": "2024-01-01"
        },
        {
            "query": "COLUMN_NAME_C = 'OK'",
        }
    ],
    ...
}
```

> OBS: Se a chave `query` for inserida no contexto de uma regra de filtro, as demais chaves `column`, `operator` e `value` serão ignoradas

### Estrutura detalhada com exemplo da chave `validations`

### Estrutura detalhada da chave `joins`

### Estrutura detalhada da chave `aggregations`

### Estrutura detalhada da chave `aggregations_with_joins`
