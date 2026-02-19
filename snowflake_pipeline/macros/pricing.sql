{%{% macro discounted_amount(price, discount, scale=2) %}
    (-1 * {{price}} * {{discount}})::decimal(16, {{scale}})
{% endmacro %}%}