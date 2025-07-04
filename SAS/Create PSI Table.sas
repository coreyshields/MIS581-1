proc sql outobs=100;
create table work.cms_psi  (
facility_id num
,facility_name char(50)
,address char(50)
,city char(10)
,state char(10)
,zip num
,county char(10)
,measure_id char(10)
,measure_name char(75)
,rate num 
,footnote char(10)
,start_date num 
,end_date num 
);

insert into work.cms_psi
select * from cms_psi_90;