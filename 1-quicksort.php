<?php
$pagestartime = microtime(); 
//快速排序
//数组中找个基数，将基数定位，然后基数左右两边的递归此方法，知道两边都排序
//时间复杂度最差的时候和冒泡排序一样 都是O(N²) 平均是O(NlogN) 差不多是6点几(N为10)
function quicksort($left , $right){
	if($left>=$right)//书上这里是 left>right 不正确 应该是>= 因为等于的时候已经左右两边都都一个索引上了 就可退出了 不然递归次数就是数组长度
		return;
	$GLOBALS['n1']++;
	$temp = $GLOBALS['a'][$left];
	$i = $left;
	$j = $right;
	while ($i!=$j) {
		//先从右往左找
		while($GLOBALS['a'][$j]>=$temp && $i<$j)
			$j--;
		//再从左往右
		while($GLOBALS['a'][$i]<=$temp && $i<$j)
			$i++;
		if($i<$j){
			$t  			  = $GLOBALS['a'][$i];
			$GLOBALS['a'][$i] = $GLOBALS['a'][$j];
			$GLOBALS['a'][$j] = $t;
		}
	}
	$GLOBALS['a'][$left] = $GLOBALS['a'][$i];
	$GLOBALS['a'][$i] = $temp;
	quicksort($left,$i-1);
	quicksort($i+1,$right);
}
//快速排序 php 简便写法
function quick_sort($arr) {
    //先判断是否需要继续进行
	$length = count($arr);
	if($length <= 1) {
		return $arr;
	}
	$GLOBALS['n2']++;
    //如果没有返回，说明数组内的元素个数 多余1个，需要排序
    //选择一个标尺
    //选择第一个元素
	$base_num = $arr[0];
    //遍历 除了标尺外的所有元素，按照大小关系放入两个数组内
    //初始化两个数组
    $left_array = array();//小于标尺的
    $right_array = array();//大于标尺的
    for($i=1; $i<$length; $i++) {
    	if($base_num > $arr[$i]) {
            //放入左边数组
    		$left_array[] = $arr[$i];
    	} else {
            //放入右边
    		$right_array[] = $arr[$i];
    	}
    }
    //再分别对 左边 和 右边的数组进行相同的排序处理方式
    //递归调用这个函数,并记录结果
    $left_array = quick_sort($left_array);
    $right_array = quick_sort($right_array);
    //合并左边 标尺 右边
    return array_merge($left_array, array($base_num), $right_array);
}

$n = 10;
$tmp = array();
for ($i = 1; $i <= $n; $i++) { 
	$tmp[] = $i;
}
// shuffle($tmp);
// 	// print_r($tmp);
// 	// echo "<br>";
// 	$GLOBALS['a']  = $tmp;
// 	quicksort(0,$n-1);
// 	// print_r($GLOBALS['a']);
// 	// echo $GLOBALS['n1'].'<br>';
// 	$result =  quick_sort($tmp);
// 	// print_r($result);
// 	// echo $GLOBALS['n2'].'<br>';

//简单测试执行递归次数（基本一致）
$max = 10000;
for ($i=0; $i < $max; $i++) { 

	shuffle($tmp);
	$GLOBALS['a']  = $tmp;
	quicksort(0,$n-1);//10000次250ms左右 //这种最佳 $n=100的时候快一秒

	// $result =  quick_sort($tmp);//10000次320ms左右

}
echo $GLOBALS['n1']/$max.'<br>';
echo $GLOBALS['n2']/$max;


$pageendtime = microtime(); 
$starttime   = explode(" ",$pagestartime); 
$endtime     = explode(" ",$pageendtime); 
$totaltime   = $endtime[0]-$starttime[0]+$endtime[1]-$starttime[1]; 
$timecost 	 = sprintf("%s",$totaltime*1000);  
echo "<br>运行时间: $timecost 毫秒<br>"; 
?>