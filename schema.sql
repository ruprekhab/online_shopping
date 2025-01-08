-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/3zgMBG
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "customer" (
    "customer_id" Numeric   NOT NULL,
    "gender" Varchar(1)   NOT NULL,
    "customer_location" Varchar(15)   NOT NULL,
    "customer_tenure" Numeric   NOT NULL,
    CONSTRAINT "pk_customer" PRIMARY KEY (
        "customer_id"
     )
);

CREATE TABLE "product" (
    "product_id" Varchar(20)   NOT NULL,
    "product_description" varchar(100)   NOT NULL,
    "product_category" varchar(30)   NOT NULL,
    "avg_price" numeric   NOT NULL,
    CONSTRAINT "pk_product" PRIMARY KEY (
        "product_id"
     )
);

CREATE TABLE "transaction" (
    "id" Numeric   NOT NULL,
    "transaction_id" Numeric   NOT NULL,
    "customer_id" Numeric   NOT NULL,
    "transaction_date" DATE   NOT NULL,
    "product_id" Varchar(20)   NOT NULL,
    "quantity" Numeric   NOT NULL,
    "delivery_charges" Numeric   NOT NULL,
    "coupon_status" varchar(10)   NOT NULL,
    "coupon_code" varchar(10)   NOT NULL,
    "discount_pct" Numeric   NOT NULL,
    "gst" Numeric   NOT NULL,
    "month" Numeric   NOT NULL,
    CONSTRAINT "pk_transaction" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "transaction" ADD CONSTRAINT "fk_transaction_customer_id" FOREIGN KEY("customer_id")
REFERENCES "customer" ("customer_id");

ALTER TABLE "transaction" ADD CONSTRAINT "fk_transaction_product_id" FOREIGN KEY("product_id")
REFERENCES "product" ("product_id");

