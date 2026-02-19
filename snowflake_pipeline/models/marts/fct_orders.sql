select
    o.*
    , s.gross_item_sales_amount
    , s.item_discount_amount
from 
    {{ ref('stg_tpch_orders') }} as o 
join 
    {{ ref('int_order_items_summary') }} as s 
    on o.order_key=s.order_key
order by order_date