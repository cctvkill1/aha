<?php   
class queue  
{  
	var $data;  
	var $head;  
	var $tail;  
};  
class stack  
{  
	var $data;  
	var $top;  
};  

	//小哈队列
$q1 = new queue();
	//小哼队列
$q2 = new queue();
$s  = new stack();    
    //初始化队列  
$q1->head = 1;  
$q1->tail = 1;  
$q2->head = 1;  
$q2->tail = 1;  
    //初始化桌面栈  
$s->top = 0;  
    //初始化用来标记的数组，用来标记哪些牌已经放在桌上  
	// for($i=1; $i<=9; $i++)  
	// 	$book[$i]=0;  
        //依次向队列中插入6个数，即小哼和小哈手中的牌  
$poker = array();
// for ($j=0; $j < 4; $j++) {  
	// for ($i=1; $i <= 13; $i++) {
	// 	$poker[] = $i;
	// }
// }
	for ($i=1; $i <= 12; $i++) {
		$poker[] = rand()%12;
	}
$poker[] = 14;
$poker[] = 15;
$len = count($poker);
shuffle($poker); 
for($i=0; $i<$len/2; $i++){  
	$q1->data[$q1->tail] = $poker[$i]; 
	$q1->tail++;  
}  
for($i=$len/2; $i<$len; $i++){
	$q2->data[$q2->tail] = $poker[$i];  
	$q2->tail++;  
}  
    // var_dump($q1->head);
    // var_dump($q1->tail);
    // var_dump($q2->head);
    // var_dump($q2->tail);exit;
	//出牌环节
    while($q1->head<$q1->tail&&$q2->head<$q2->tail)  //当队列不为空时循环  
    {  
        $t=$q1->data[$q1->head];    //小哼出第一张牌  
        //判断小哼是否赢牌  
        if($book[$t]!=1)     //表示桌面上没有此牌  
        {  
            $q1->head++;   //打出的牌出队  
            $s->top++;     //打出的牌入栈  
            $s->data[$s->top]=$t;  
            $book[$t]=1;   //标记桌面上有此牌  
        }  
        else  
        {  
            //小哼赢得此牌  
            // $q1->head++;       //打出的牌入队  
            $q1->data[$q1->tail]=$t;  
            // $q1->tail++;  
            while($s->data[$s->top]!=$t)  //把桌上可以赢得的牌依次放入手中牌的末尾  
            {  
                $book[$s->data[$s->top]]=0;  //取消标记  
                $q1->data[$q1->tail]=$s->data[$s->top];    //依次放入末尾  
                $q1->tail++;  
                $s->top--;     //栈中少了一张牌，栈减1  
            }  
        }  
        //小哈出牌同小哼  
        $t=$q2->data[$q2->head];  
        if($book[$t]!=1)  
        {  
        	$q2->head++;  
        	$s->top++;  
        	$s->data[$s->top]=$t;  
        	$book[$t]=1;  
        }  
        else  
        {  
        	// $q2->head++;  
        	$q2->data[$q2->tail]=$t;  
        	// $q2->tail++;  
        	while($s->data[$s->top]!=$t)  
        	{  
        		$book[$s->data[$s->top]]=0;  
        		$q2->data[$q2->tail]=$s->data[$s->top];  
        		$q2->tail++;  
        		$s->top--;  
        	}   
        }  
    }

    if($q2->head==$q2->tail)  
    	echo "小哼win 共" . ($q1->tail-$q1->head).'张牌';  
    else  
    	echo "小哈win 共" . ($q2->tail-$q2->head).'张牌';  
    echo "<br>小哼当前手中的牌是：";  
    for($i=$q1->head; $i<=$q1->tail-1; $i++)  
    	echo $q1->data[$i]." ";  
    echo "<br>小哈当前手中的牌是："; 
    for($i=$q2->head; $i<=$q2->tail-1; $i++)  
    	echo $q2->data[$i]." ";  
    if($s->top>0){
    	echo "<br>桌上的牌是：";  
    	for($i=1; $i<=$s->top; $i++)  
    		echo $s->data[$i]." ";  
    }  
    else
    	echo "<br>桌上已经没有牌了！";  


    ?>