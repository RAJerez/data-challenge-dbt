
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

-- TODO: Models doesn't need to be named as my_first_* ... instead of that, put a more descriptive name 

{{ config(materialized='table') }}

with source_data as (

    select 1 as id
    union all
    select null as id

)

select *
from source_data


-- TODO: With DBT I'd try to present a real case or another example in order to show your capabilities with the tool, this example is pretty basic

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
