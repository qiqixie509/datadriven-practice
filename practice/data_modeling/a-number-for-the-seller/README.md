# A Number for the Seller

*They want a total. Give them the right schema first.*

[Data Modeling · Easy · on DataDriven](https://datadriven.io/problems/a_number_for_the_seller)

## How it went

| | |
|---|---|
| Solved | 2026-10-05 |
| Accepted | on the 2nd submission |
| Hints | none |
| Concepts | Attributes, Dimension Tables, Fact Tables, Foreign Keys, Grain Definition, Metric Additivity, One-to-Many, Pre-Aggregation, Primary Keys, Star Schema, Surrogate Keys |

## The design

```mermaid
erDiagram
    dim_seller {
        VARCHAR id PK
        VARCHAR name
        VARCHAR gender
        VARCHAR email
        VARCHAR phone
    }
    dim_products {
        VARCHAR name
        VARCHAR id PK
        DECIMAL price
    }
    fact_sale {
        INT quantity
        VARCHAR product_id FK
        VARCHAR id PK
        DECIMAL total_amount
        TIMESTAMP created_at
        DATE sale_date
    }
    new_table {
    }
    fact_list {
        VARCHAR product_id FK
        VARCHAR seller_id FK
        BOOLEAN active
        TIMESTAMP update_at
        DATE went_live_date
    }
    dim_seller only one optionally to zero or more fact_list : "seller_id = id"
    fact_list only one optionally to zero or more fact_sale : "product_id"
    dim_products only one optionally to zero or more fact_sale : "product_id = id"
```

The accepted design is in [`schema.sql`](./schema.sql) as DDL and in [`schema.json`](./schema.json) as JSON.
