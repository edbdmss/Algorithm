select I.ID, N.FISH_NAME, I.LENGTH
from ( select ID, FISH_TYPE, LENGTH,
       max(LENGTH) OVER (partition by FISH_TYPE) as MAX_LENGTH, TIME
       from FISH_INFO 
      ) I
inner join FISH_NAME_INFO N 
on I.FISH_TYPE = N.FISH_TYPE
where I.LENGTH = I.MAX_LENGTH
order by I.ID;