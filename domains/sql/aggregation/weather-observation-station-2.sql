/*
Query the sum of LAT_N, followed by the sum of LONG_W, from STATION. The two results should be separated by a space and rounded to  decimal places.
*/
SELECT ROUND(SUM(LAT_N),2),ROUND(SUM(LONG_W),2)
FROM STATION;
