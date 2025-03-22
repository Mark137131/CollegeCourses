#include "reg52.h"
#include "public.h"
#include "MatrixKey.h"

/*******************************************************************************
* 函 数 名      : MatrixKey
* 函数功能		   : 矩阵键盘读取按键键码
* 输    入       : 无
* 输    出    	 : KeyNumber：按键对应的值
*******************************************************************************/

u8 MatrixKey()
{  
    unsigned char KeyNumber=0;
		u8 i=0;
		u8 j=0;
	  
	  k1=k2=k3=k4=1; o1=o2=o3=o4=1;
	  k1=0;
	  if(o4==0){delay_ms(20);while(o4==0);delay_ms(20);KeyNumber=4;}
	  if(o3==0){delay_ms(20);while(o3==0);delay_ms(20);KeyNumber=3;}
	  if(o2==0){delay_ms(20);while(o2==0);delay_ms(20);KeyNumber=2;}
	  if(o1==0){delay_ms(20);while(o1==0);delay_ms(20);KeyNumber=1;}
		
	  k1=k2=k3=k4=1;o1=o2=o3=o4=1;
	  k2=0;
	  if(o4==0){delay_ms(20);while(o4==0);delay_ms(20);KeyNumber=8;}
	  if(o3==0){delay_ms(20);while(o3==0);delay_ms(20);KeyNumber=7;}
	  if(o2==0){delay_ms(20);while(o2==0);delay_ms(20);KeyNumber=6;}
	  if(o1==0){delay_ms(20);while(o1==0);delay_ms(20);KeyNumber=5;}
		
	  k1=k2=k3=k4=1;o1=o2=o3=o4=1;
	  k3=0;
	  if(o4==0){delay_ms(20);while(o4==0);delay_ms(20);KeyNumber=12;}
	  if(o3==0){delay_ms(20);while(o3==0);delay_ms(20);KeyNumber=11;}
	  if(o2==0){delay_ms(20);while(o2==0);delay_ms(20);KeyNumber=10;}
	  if(o1==0){delay_ms(20);while(o1==0);delay_ms(20);KeyNumber=9;}
		
	  k1=k2=k3=k4=1;o1=o2=o3=o4=1;
	  k4=0;
	  if(o4==0){delay_ms(20);while(o4==0);delay_ms(20);KeyNumber=16;}
	  if(o3==0){delay_ms(20);while(o3==0);delay_ms(20);KeyNumber=15;}
	  if(o2==0){delay_ms(20);while(o2==0);delay_ms(20);KeyNumber=14;}
	  if(o1==0){delay_ms(20);while(o1==0);delay_ms(20);KeyNumber=13;}
		
		return KeyNumber;
}

