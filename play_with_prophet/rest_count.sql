drop table if exists all_dates;
create temp table all_dates as (
  select
    l.date as the_date
  from public.list_of_all_dates_ever l
  where l.date between '2009-01-01' and '2016-12-31'
);

drop table if exists sandbox.live_rest_count;
create table sandbox.live_rest_count  as (
  select
    ad.the_date,
    count(distinct rsh.cust_id) as live_cust_count
  from all_dates ad
  join public.restaurant_status_history rsh
    on rsh.begin_status_date <= ad.the_date
    and coalesce(rsh.end_status_date, current_date) >= ad.the_date
    and rsh.live_status_ind=1
  group by 1
);
