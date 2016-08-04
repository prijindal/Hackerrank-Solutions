/*

Consider  and  to be two points on a 2D plane.

 happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
 happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
 happens to equal the minimum value in Western Longitude (LONG_W in STATION).
 happens to equal the maximum value in Western Longitude (LONG_W in STATION).
Query the Manhattan Distance between points  and  and round it to a scale of  decimal places.*/
SELECT ROUND(ABS(MIN(LONG_W) - MIN(LAT_N)) +  ABS(MAX(LONG_W) - MAX(LAT_N)) , 4)
FROM STATION;
