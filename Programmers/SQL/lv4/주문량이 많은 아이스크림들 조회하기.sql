SELECT J.FLAVOR
from 
    (select SHIPMENT_ID, FLAVOR, sum(TOTAL_ORDER) as F_TOTAL_ORDER
     from FIRST_HALF 
     group by FLAVOR
     ) F
inner join 
    (select SHIPMENT_ID, FLAVOR, sum(TOTAL_ORDER) as J_TOTAL_ORDER
     from JULY 
     group by FLAVOR
    ) J
on F.FLAVOR = J.FLAVOR
order by F_TOTAL_ORDER + J_TOTAL_ORDER desc limit 3;