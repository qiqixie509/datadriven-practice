# Content Engagement Data Model

*Post published. Now measure everything that happens next.*

[Data Modeling · Hard · on DataDriven](https://datadriven.io/problems/content_engagement_data_model)

## How it went

| | |
|---|---|
| Solved | 2026-10-06 |
| Accepted | on the first submission |
| Hints | none |
| Concepts | Denormalization, Dimension Tables, Fact Tables, Foreign Keys, Grain Definition, Metric Additivity, One-to-Many, Pre-Aggregation, Primary Keys, Star Schema |

## The design

```mermaid
erDiagram
    dim_users {
        VARCHAR id PK
        VARCHAR name
        VARCHAR email
        VARCHAR phone
    }
    fact_comments {
        VARCHAR id PK
        VARCHAR comment_by
        VARCHAR comment_to FK
        TEXT content
        TIMESTAMP create_at
        TIMESTAMP update_at
    }
    fact_reactions {
        VARCHAR post_id FK
        VARCHAR user_id FK
        VARCHAR type
        TIMESTAMP create_at
        VARCHAR vendor
    }
    fact_views {
        VARCHAR post_id FK
        VARCHAR user_id
        INT durations
    }
    dim_posts {
        VARCHAR id PK
        VARCHAR parent_post_id
        VARCHAR user_id FK
        TEXT content
        TIMESTAMP created_at
        TIMESTAMP updated_at
        unspecified type
    }
    dim_shares {
        VARCHAR post_id FK
        VARCHAR shared_by
        VARCHAR vendor
        TIMESTAMP shared_at
    }
    fact_views only one optionally to zero or more fact_reactions : "post_id"
    fact_comments only one optionally to zero or more fact_reactions : "post_id = comment_to"
    dim_users only one optionally to zero or more fact_reactions : "user_id = id"
    dim_posts only one optionally to zero or more fact_comments : "comment_to = id"
    dim_posts only one optionally to zero or more dim_shares : "post_id = id"
```

The accepted design is in [`schema.sql`](./schema.sql) as DDL and in [`schema.json`](./schema.json) as JSON.
