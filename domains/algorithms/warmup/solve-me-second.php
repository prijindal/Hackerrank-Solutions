<?php
function add($a){
    return $a[0] + $a[1];
}
$handle = fopen ("php://stdin","r");
$n=fgets($handle);

for($i=0;$i<$n;++$i){
	$A[]=split(' ',fgets($handle));
}

for($i=0;$i<$n;++$i){
	echo add($A[$i])."\n";
}

fclose($handle);
?>
