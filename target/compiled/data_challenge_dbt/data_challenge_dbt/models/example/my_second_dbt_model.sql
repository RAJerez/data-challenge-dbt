-- Use the `ref` function to select from other models

select *
from "data-challenge-dbt"."public"."my_first_dbt_model"
where id = 1