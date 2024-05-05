# Консольное приложение `Личный финансовый кошелек`.

#### Этот инструмент позволяет отслеживать и управлять вашими финансовыми транзакциями. С его помощью вы можете добавлять новые записи, обновлять существующие, получать текущий баланс, а также просматривать записи по различным критериям.

## Использование

- Запустите приложение с помощью Python, указав нужные аргументы.

```bash
python main.py [arguments]
```

- Вывод описания команд в консоли.

```bash
python main.py -h
```

### Описание Команд

#### Команда `add` - добавляет новую запись.

- Синтаксис:

```bash
python main.py add <amount> <category> <date> <description>
```

| Параметр | Описание | Тип |
| -------- | -------- | --- |
| amount | Сумма транзакции. | Float |
| category | Категория транзакции (`income` или `expense`).  | String |
| date | Дата транзакции (дата должна быть в формате `YYYY-MM-DD` или `YYYY-M-D`).  | String |
| description | Описание транзакции.  | String |

- Пример:

```bash
python main.py add 6000 "income" "2024-05-05" "Пополнение счета"
```

```bash
python main.py add 1000004.99 "income" "2024-05-05" "Подарок"
```

```bash
python main.py add 3124.99 "expense" "2024-05-05" "Покупки в продуктовом магазине"
```

#### Команда `update` - обновляет данные в записи.

- Синтаксис:

```bash
python main.py update <index> [--amount <new_amount>] [--category <new_category>] [--date <new_date>] [--description <new_description>]
```

| Параметр | Описание | Тип |
| -------- | -------- | --- |
| index | Индекс записи, которую необходимо обновить. | Integer |
| --amount | (Опционально) Обновлённая сумма транзакции. | Float |
| --category | (Опционально) Обновлённая категория транзакции. | String |
| --date | (Опционально) Обновлённая дата транзакции. | String |
| --description | (Опционально) Обновлённое описание транзакции. | String |

- Пример:

```bash
python main.py update 2 --amount 4700.99 --description "Покупки в продуктовом магазине и зоомагазине"
```

#### Команда `get_balance` - возвращает информацию о балансе, доходах и расходах.

- Синтаксис:

```bash
python main.py get_balance
```

- Вывод:

```bash
Balance: 1001304.0
Income: 1006004.99
Expense: 4700.99
```

#### Команда `get` - выводит все существующие записи и их индексы.

- Синтаксис:

```bash
python main.py get
```

- Вывод:

```bash
[0]
Amount: 6000.0.
Category: income.
Date: 2024-05-05.
Description: Пополнение счета.

[1]
Amount: 4700.99.
Category: expense.
Date: 2024-05-05.
Description: Покупки в продуктовом магазине и зоомагазине.
```

#### Команда `get_by_key` -  позволяет получать записи и их индексы по ключевым значениям, таким как `amount`, `category`, или `date`.

- Синтаксис:

```bash
    python main.py get_by_key <by> <value>
```

| Параметр | Описание | Тип |
| -------- | -------- | --- |
| by | Ключ, по которому производится поиск (`amount`, `category`, или `date`) | String |
| value | Значение, используемое для поиска | Float или String |

- Пример:

```bash
python main.py get_by_key "category" "income"
```

- Вывод:

```bash
[0]
Amount: 6000.0.
Category: income.
Date: 2024-05-05.
Description: Пополнение счета.

[1]
Amount: 1000004.99.
Category: income.
Date: 2024-05-05.
Description: Подарок.
```

### Тесты.

- Для запуска всех тестов используйте эту команду.

```bash
python -m unittest discover -s tests -v
```
