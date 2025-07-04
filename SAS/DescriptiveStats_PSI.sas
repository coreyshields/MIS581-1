proc sql;
select 
        count(rate) as n,
        mean(rate) as mean_rate,
        min(rate) as min_rate,
        max(rate) as max_rate
    from work.cms_psi
    where rate >= 0 and measure_id = 'PSI_90'
    order by mean_rate;