CREATE TABLE dim_users (
    id VARCHAR,
    name VARCHAR,
    email VARCHAR,
    phone VARCHAR,
    PRIMARY KEY (id)
);

CREATE TABLE fact_comments (
    id VARCHAR,
    comment_by VARCHAR,
    comment_to VARCHAR,
    content TEXT,
    create_at TIMESTAMP,
    update_at TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE fact_reactions (
    post_id VARCHAR,
    user_id VARCHAR,
    type VARCHAR,
    create_at TIMESTAMP,
    vendor VARCHAR
);

CREATE TABLE fact_views (
    post_id VARCHAR,
    user_id VARCHAR,
    durations INT
);

CREATE TABLE dim_posts (
    id VARCHAR,
    parent_post_id VARCHAR,
    user_id VARCHAR,
    content TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    type TEXT,  /* no type on the canvas */
    PRIMARY KEY (id)
);

CREATE TABLE dim_shares (
    post_id VARCHAR,
    shared_by VARCHAR,
    vendor VARCHAR,
    shared_at TIMESTAMP
);

ALTER TABLE fact_reactions
    ADD FOREIGN KEY (post_id) REFERENCES fact_views (post_id);

ALTER TABLE fact_reactions
    ADD FOREIGN KEY (post_id) REFERENCES fact_comments (comment_to);

ALTER TABLE fact_reactions
    ADD FOREIGN KEY (user_id) REFERENCES dim_users (id);

ALTER TABLE fact_comments
    ADD FOREIGN KEY (comment_to) REFERENCES dim_posts (id);

ALTER TABLE dim_shares
    ADD FOREIGN KEY (post_id) REFERENCES dim_posts (id);
