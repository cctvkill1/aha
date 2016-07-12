<?php 
//判断字符串是否是回文 主要取字符长度的中间值 然后左右边比较
function ishuiwen($str){
	$len=strlen($str);
	$l=true;
	$k=intval($len/2)+1;
	for($j=0;$j<$k;$j++){
		if (substr($str,$j,1)!=substr($str,$len-$j-1,1)){
			$l=false;
			break;
		}
	}
	if ($l==1)
		return true;	
	else
		return false;
	
}
$str='abcba';
var_dump(ishuiwen($str));
$str='abcb';
var_dump(ishuiwen($str));



?>