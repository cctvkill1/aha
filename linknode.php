<?php
/**单向链表 -- 水浒传英雄排行版*/
class hero{
	public $name = '';
	public $no ='';
	public $cname = '';
	public $next = '';
	public function __construct($no = '',$name='',$cname=''){
		$this->no = $no;
		$this->name = $name;
		$this->cname = $cname;
	}
     //显示英雄链表
	public static function showHero($head){
		$cur = $head;
		while($cur->next != null){
			echo '英雄编号:'.$cur->next->no.'&nbsp;&nbsp;';
			echo '英雄姓名:'.$cur->next->name.'&nbsp;&nbsp;';
			echo '英雄昵称:'.$cur->next->cname.'&nbsp;&nbsp;';
			echo '<br />';
			$cur  = $cur->next;
		}
		echo '<hr />';
	}
     //英雄加到链表末端
	public static function addHero($head,$hero){
		$cur = $head;
		while($cur->next != null){
			$cur = $cur->next;
		}
		$cur->next  = $hero;
	}
     //英雄按排序加入
	public static function addHero2($head,$hero){
		$cur = $head;
		while($cur->next != null){
			if($cur->next->no  > $hero->no){
				break;
			}
			$cur = $cur->next;
		}
		$hero->next  = $cur->next;
		$cur->next  = $hero;
	}
     //修改英雄
	public static function editHero($head,$hero){
		$cur = $head;
		while($cur->next != null){
			if($cur->next == $hero){
				break;
			}
			$cur = $cur->next;
		}
		$cur->next->name  = $hero->name;
		$cur->next->cname  = $hero->cname;
	}
     //删除英雄
	public static function delHero($head,$hero){
		$cur = $head;
		while($cur->next != null){
			if($cur->next == $hero){
				break;
			}
			$cur = $cur->next;
		}
		$cur->next  = $hero->next;
		$hero->next  = null;
	}
}

$head = new hero();
$songjiang =new hero(1,'宋江','及时雨');
$lujunyi =new hero(2,'卢俊义','玉麒麟');

$head->next = $songjiang;
$songjiang->next = $lujunyi;

echo '默认<br>';
hero::showHero($head);
echo '加入到链表末端<br>';
$linchong = new hero(6,'林冲','豹子头');
hero::addHero($head,$linchong);
hero::showHero($head); 
echo '按排名加入链表<br>';
$wuyong = new hero(3,'吴用','智多星');
hero::addHero2($head,$wuyong);
hero::showHero($head); 
echo '修改英雄<br>';
$wuyong->name='吴用2';
hero::editHero($head,$wuyong);
hero::showHero($head); 
echo '删除英雄<br>';
hero::delHero($head,$wuyong);
hero::showHero($head);

?>