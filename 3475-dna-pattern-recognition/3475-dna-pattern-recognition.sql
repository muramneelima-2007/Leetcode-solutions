# Write your MySQL query statement below
select sample_id,dna_sequence,species,
case
when dna_sequence like "ATG%" then 1
else 0 
end as has_start,

case
when dna_sequence LIKE "%TAA"
OR dna_sequence LIKE "%TAG"
OR dna_sequence LIKE "%TGA" then 1
else 0 
end as has_stop,

case
when dna_sequence like "%ATAT%" then 1
else 0 
end as has_atat,

case
when dna_sequence LIKE "%GGG%" then 1
else 0 
end as has_ggg

from Samples;