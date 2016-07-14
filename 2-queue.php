<?php 

class queue{
	var  $data ;
	var  $head ;
	var  $tail ;
}
$q = new queue();
$q->head = 1;
$q->tail = 1;
$n = 10;
$tmp = array();
for ($i = 1; $i <= $n; $i++) { 
	$tmp[] = $i;
}
shuffle($tmp);
$q->data = $tmp;
// var_dump($q->data);

?>