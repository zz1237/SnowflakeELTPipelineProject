select
    l.order_item_key
    , l.part_key
    , l.line_number
    , l.extended_price
    , o.order_key
    , o.customer_key
    , o.order_date
    , {{discounted_amount('l.extended_price','l.discount_percentage')}} as item_discount
from 
    {{ ref('stg_tpch_orders') }} as o 
join 
    {{ ref('stg_tpch_line_items') }} as l 
    on o.order_key=l.order_key
order by 
    o.order_date