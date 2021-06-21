# Clickhouse

http://docs.opengeospatial.org/per/20-039r2.html#_the_clickhouse_storage_choice

## dggs_catalog

not sure if needed, depends on metadata and layer management, potentially configure in a YAML file

```sql
CREATE TABLE dcube.dggs_catalog
(
    `table_name` String,
    `dggs_type` String,
    `extent` Array(Int32),
    `base_resolution` UInt16,
    `resolutions` Array(UInt16),
    `variables` Array(String),
    `description` String,
    `meta_url` String,
    `date_loaded` DateTime,
    `date_updated` DateTime
)
ENGINE = MergeTree
PARTITION BY dggs_type
ORDER BY table_name
SAMPLE BY date_updated
;

insert into dcube.dggs_catalog (table_name, dggs_type, base_resolution, resolutions, variables, description, date_loaded) values ( 'srtm_30m_estonia_h3' , 'H3' ,  9, [9, 8, 7, 6, 5, 4, 3, 2, 1] , ['elevation'],  '30m SRTM sampled at res 9 covering Estonia', toDateTime(now(), 'Europe/Tallinn') );

alter table dcube.dggs_catalog update extent = [24, 58, 27, 59] where table_name = 'srtm_30m_estonia_h3';

select * from dcube.dggs_catalog where arrayExists(x -> (x = 'elevation'), variables);
```

## data layer, elevation

```sql
CREATE TABLE dcube.srtm_30m_estonia_h3
(
    `cell_id` String,
    `elevation` Float,
    `resolution` UInt16,
    `parent_ids` Array(String)
)
ENGINE = MergeTree
PARTITION BY resolution
ORDER BY cell_id
SAMPLE BY cell_id
;
```
