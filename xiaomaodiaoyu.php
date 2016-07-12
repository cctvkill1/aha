<?php   
 // set_time_limit(1800) ;
class queue  
{  
	var $data;  
	// var $head;  
	// var $tail;  
};  
class stack  
{  
	var $data;  
	// var $top;  
};  

	//小哈队列
$q1 = new queue();
	//小哼队列
$q2 = new queue();	//array_push 尾部加入 array_shift 删除第一个
$s  = new stack();  //array_push 尾部加入 array_pop 删除最后一个
$poker = array();
for ($j=0; $j < 4; $j++) {  
	for ($i=1; $i <= 13; $i++) {
		$poker[] = $i;
	}
} 
// $poker[] = 14;
// $poker[] = 15;
$len = count($poker);
shuffle($poker); 
for($i=0; $i<$len/2; $i++){  
	$q1->data[] = $poker[$i];  
}  
for($i=$len/2; $i<$len; $i++){
	$q2->data[] = $poker[$i];  
}   
// var_dump($q1->data);
// var_dump($q2->data);

	//出牌环节
    while(count($q1->data)!=0&&count($q2->data)!=0)  //当队列不为空时循环  
    {   
        $t=array_shift($q1->data);//小哼出第一张牌  
        //判断小哼是否赢牌  
        if($book[$t]!=1)     //表示桌面上没有此牌  
        {   
        	$s->data[] = $t;
            $book[$t]=1;   //标记桌面上有此牌  
        }  
        else  
        {  
            //小哼赢得此牌
        	$q1->data[] = $t;
        	$len = count($s->data)-1;
            while($s->data[$len]!=$t&&$len>0)  //把桌上可以赢得的牌依次放入手中牌的末尾  
            {  
                $book[$s->data[$len]] = 0;  //取消标记   
                $q1->data[] = $s->data[$len];
                array_pop($s->data);
                $len--;     //栈中少了一张牌，栈减1  
            }  
        }  
        if(count($q1->data)==0) break;
        //小哈出牌同小哼   
        $t=array_shift($q2->data);//小哈出第一张牌  
        if($book[$t]!=1)  
        {   
        	$s->data[] = $t;
            $book[$t]=1;   //标记桌面上有此牌  
        }  
        else  
        {  
        	 //小哈赢得此牌
        	$q2->data[] = $t;
        	$len = count($s->data)-1;
            while($s->data[$len]!=$t&&$len>0)  //把桌上可以赢得的牌依次放入手中牌的末尾  
            {  
                $book[$s->data[$len]] = 0;  //取消标记   
                $q2->data[] = $s->data[$len];
                array_pop($s->data);
                $len--;     //栈中少了一张牌，栈减1  
            }  
        }  
        if(count($q2->data)==0) break;
        // print_r($s->data);
    }

    if(count($q2->data)==0)
    	echo "<br>小哼win 共" . count($q1->data).'张牌';  
    else  
    	echo "<br>小哈win 共" . count($q2->data).'张牌';  
    echo "<br>小哼当前手中的牌是：";  
    for($i=0; $i<count($q1->data); $i++)  
    	echo $q1->data[$i]." ";  
    echo "<br>小哈当前手中的牌是："; 
    for($i=0; $i<count($q2->data); $i++)  
    	echo $q2->data[$i]." ";  
    if(count($s->data)>0){
    	echo "<br>桌上的牌是(".count($s->data)."张)：";  
    	for($i=0; $i<count($s->data); $i++)  
    		echo $s->data[$i]." ";  
    }  
    else
    	echo "<br>桌上已经没有牌了！";  

    // var_dump($s);


    ?>