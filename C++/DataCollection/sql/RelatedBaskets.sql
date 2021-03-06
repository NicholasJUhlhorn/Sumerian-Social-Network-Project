/*Grabs basketID*/
select tabid from basketnames group by tabid;

/*Grabs basket years*/
select tabid, year from bestyears where tabid in (select tabid from basketnames group by tabid) group by year;

/*Joins Basket Name, Year, and tabID*/
select basketnames.name, basketnames.tabid, A.year from 
basketnames join 
(select tabid, year from bestyears where tabid in (select tabid from basketnames group by tabid) ) as A
on basketnames.tabid = A.tabid;

/*Joins rawname and years*/
select rawnames.tabid, rawnames.name, bestyears.year from rawnames join bestyears on rawnames.tabid = bestyears.tabid;

/*Compare basket names and years with raw names and years*/
select Raw.tabid as RawID, Raw.name as RawName, Raw.Year as RawYear, Basket.tabid as BasketID, Basket.name as BasketName, Basket.Year as BasketYear from 
(select rawnames.tabid, rawnames.name, bestyears.year from rawnames join bestyears on rawnames.tabid = bestyears.tabid) as Raw,
(select basketnames.name, basketnames.tabid, A.year from basketnames join 
(select tabid, year from bestyears where tabid in (select tabid from basketnames group by tabid) ) as A
on basketnames.tabid = A.tabid) as Basket
where Raw.name = Basket.name and Raw.Year = Basket.year and Basket.name not like '...' group by Basket.tabid;

