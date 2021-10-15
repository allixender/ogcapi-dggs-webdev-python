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


# Sqlite3

Sqlite is by no means a production-usable database for even a midsized DGGS dataset. But it used here to outline general concepts.

```sql
CREATE TABLE "dggs_catalog" (
	"table_name"	TEXT NOT NULL,
	"dggs_type"	TEXT NOT NULL,
	"extent"	TEXT,
	"base_resolution"	INTEGER NOT NULL,
	"resolutions"	TEXT,
	"variables"	TEXT,
	"description"	TEXT,
	"meta_url"	TEXT,
	"date_loaded"	NUMERIC,
	"date_updated"	NUMERIC,
	PRIMARY KEY("table_name")
);

INSERT INTO dggs_catalog  (table_name, dggs_type, base_resolution, resolutions, variables, description, date_loaded) values ( 'srtm_30m_estonia_h3' , 'H3' ,  9, '9:8:7:6:5:4:3:2' , 'elevation',  '30m SRTM sampled at res 9 covering Estonia', CAST ( strftime('%s','now') AS INT) );

UPDATE dggs_catalog set extent = '24,58,27,59' where table_name = 'srtm_30m_estonia_h3';

```

Then the corresponding data table referenced in the catalog:

```sql
CREATE TABLE "srtm_30m_estonia_h3" (
	"cell_id"	TEXT,
	"elevation"	REAL NOT NULL,
	"resolution"	INTEGER NOT NULL,
	"parent_ids"	TEXT,
	PRIMARY KEY("cell_id")
);
```

And fill in a single cell with parents:

```sql
INSERT INTO srtm_30m_estonia_h3 ( 'cell_id','elevation','resolution','parent_ids') VALUES ( '891136a71c7ffff', 38.7, 9, '881136a71dfffff:871136a71ffffff:861136a77ffffff:851136a7fffffff:841136bffffffff:831136fffffffff:821137fffffffff');
INSERT INTO srtm_30m_estonia_h3 ( 'cell_id','elevation','resolution','parent_ids') VALUES ( '881136a71dfffff', 38.7, 8, '871136a71ffffff:861136a77ffffff:851136a7fffffff:841136bffffffff:831136fffffffff:821137fffffffff');
INSERT INTO srtm_30m_estonia_h3 ( 'cell_id','elevation','resolution','parent_ids') VALUES ( '871136a71ffffff', 38.7, 7, '861136a77ffffff:851136a7fffffff:841136bffffffff:831136fffffffff:821137fffffffff');
INSERT INTO srtm_30m_estonia_h3 ( 'cell_id','elevation','resolution','parent_ids') VALUES ( '861136a77ffffff', 38.7, 6, '851136a7fffffff:841136bffffffff:831136fffffffff:821137fffffffff');
INSERT INTO srtm_30m_estonia_h3 ( 'cell_id','elevation','resolution','parent_ids') VALUES ( '851136a7fffffff', 38.7, 5, '841136bffffffff:831136fffffffff:821137fffffffff');
INSERT INTO srtm_30m_estonia_h3 ( 'cell_id','elevation','resolution','parent_ids') VALUES ( '841136bffffffff', 38.7, 4, '831136fffffffff:821137fffffffff');
INSERT INTO srtm_30m_estonia_h3 ( 'cell_id','elevation','resolution','parent_ids') VALUES ( '831136fffffffff', 38.7, 3, '821137fffffffff');
INSERT INTO srtm_30m_estonia_h3 ( 'cell_id','elevation','resolution','parent_ids') VALUES ( '821137fffffffff', 38.7, 2, '');

```
