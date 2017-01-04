
/*
Consider  and  to be two points on a 2D plane where  are the respective minimum and maximum values of Northern Latitude (LAT_N) and  are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.
*/
SELECT ROUND(SQRT(POWER(MIN(LONG_W) - MIN(LAT_N), 2) +  POWER(MAX(LONG_W) - MAX(LAT_N), 2)) , 4)
FROM STATION;
