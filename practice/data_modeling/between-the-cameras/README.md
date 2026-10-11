# Between the Cameras

*Every plate that goes in should come out. Watch the ones that don't.*

[Data Modeling · Easy · on DataDriven](https://datadriven.io/problems/between_the_cameras)

## How it went

| | |
|---|---|
| Solved | 2026-10-05 |
| Accepted | on the first submission |
| Hints | none |
| Concepts | Attributes, Constraints, Data Types, Entities, Foreign Keys, Grain Definition, One-to-Many, Pre-Aggregation, Primary Keys |

## The design

```mermaid
erDiagram
    dim_plate {
        VARCHAR id PK
        VARCHAR plate_number
    }
    dim_section {
        VARCHAR id PK
        VARCHAR name
    }
    fact_commuter {
        VARCHAR event_id PK
        VARCHAR plate_id FK
        VARCHAR section_id FK
        VARCHAR event_type
        TIMESTAMP event_time
    }
    dim_plate only one optionally to zero or more fact_commuter : "plate_id = id"
    dim_section only one optionally to zero or more fact_commuter : "section_id = id"
```

The accepted design is in [`schema.sql`](./schema.sql) as DDL and in [`schema.json`](./schema.json) as JSON.
