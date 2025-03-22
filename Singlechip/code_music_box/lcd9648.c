#include "lcd9648.h"
#include "font.h"
#include "public.h"	

/*******************************************************************************
* 函 数 名       : lcd9648_spi_write_byte
* 函数功能		 : LCD9648 SPI传输数据
* 输    入       : dat：数据
* 输    出    	 : 无
*******************************************************************************/
void lcd9648_spi_write_byte(u8 dat)
{
	u8 i=0;

   	for(i=0;i<8;i++)//循环8次将一个字节传输			
   	{  
      	if((dat&0x80)!=0) 
			SDA = 1;
        else 
			SDA = 0;
      	dat<<= 1;//先写高位再写低位
	  	SCL = 0;
      	SCL = 1;//时钟上升沿写入数据			
   	}
}

/*******************************************************************************
* 函 数 名       : lcd9648_write_cmd
* 函数功能		 : LCD9648写命令
* 输    入       : cmd：命令
* 输    出    	 : 无
*******************************************************************************/
void lcd9648_write_cmd(u8 cmd)
{
	CS0 = 0;//使能
	RS  = 0;//选择命令
	lcd9648_spi_write_byte(cmd);//发送命令
	CS0 = 1;//失能	
}

/*******************************************************************************
* 函 数 名       : lcd9648_write_dat
* 函数功能		 : LCD9648写数据
* 输    入       : dat：数据
* 输    出    	 : 无
*******************************************************************************/
void lcd9648_write_dat(u8 dat)
{
	CS0 = 0;//使能
	RS  = 1;//选择数据
	lcd9648_spi_write_byte(dat);//发送数据
	CS0 = 1;//失能	
}

/*******************************************************************************
* 函 数 名       : lcd9648_init
* 函数功能		 : LCD9648初始化
* 输    入       : 无
* 输    出    	 : 无
*******************************************************************************/
void lcd9648_init(void)
{
	RST=1;  
	delay_ms(10);
	RST=0;
	delay_ms(10);
	RST=1;
	delay_ms(10);//复位

	lcd9648_write_cmd(0xe2);		  //软件复位
	lcd9648_write_cmd(0xc8);		  //0xC8普通方向选择选择反向，0xC0为正常方向
	lcd9648_write_cmd(0xa0);		  //0xA0段方向选择正常方向（0xA1为反方向
	lcd9648_write_cmd(0x2f);
	lcd9648_write_cmd(0x26);
	lcd9648_write_cmd(0x81);		  //背景光对比度
	lcd9648_write_cmd(0x10);
	lcd9648_write_cmd(0xaf);		  //开启显示
	lcd9648_write_cmd(0x40);		  //设置滚动一行命令
}

/*******************************************************************************
* 函 数 名       : lcd9648_clear
* 函数功能		 : LCD9648清屏
* 输    入       : 无
* 输    出    	 : 无
*******************************************************************************/
void lcd9648_clear(void)
{
	u8 i,j;

	for(i=0;i<9;i++)//一共9页
	{
		lcd9648_write_cmd(0x40);//设置滚动一行命令
		lcd9648_write_cmd(0xb0+i);//页地址
		lcd9648_write_cmd(0x10);//列高字节地址
		lcd9648_write_cmd(0x00);//列低字节地址
		
		for(j = 0; j < LCD_WIDTH; j++)//每一行的像素点
		{
			lcd9648_write_dat(0x00);//不显示	
		}	
	}
}

//在指定位置显示一个16*8字符
//x,y:起始坐标 x:0-96 y:0-2 
//num:要显示的字符:" "--->"~"
void lcd_show_char(u8 x,u8 y,u8 num)
{
	unsigned char i, x1, x2;

	if(x>96||y>2)return;//超出范围了

	y *= 2;
	y += 0xB0;	   			//求取Y坐标的值
	x1 = (x >> 4) & 0x0F;   //由于X坐标要两句命令，分高低4位，所以这里先取出高4位
	x2 = x & 0x0F;          //去低四位

	lcd9648_write_cmd(y);	//页地址 y坐标
	lcd9648_write_cmd(0x10+x1);	//列高字节地址 x坐标
	lcd9648_write_cmd(0x00+x2);	//列低字节地址

	num=num-' ';//得到偏移后的值（ASCII字库是从空格开始取模，所以-' '就是对应字符的字库）

	for(i = 0;i < 8;i++) 
	{
		lcd9648_write_dat(ascii_1608[num][i*2]);
	}
	
	lcd9648_write_cmd(y+1);	//页地址 y坐标
	lcd9648_write_cmd(0x10+x1);	//列高字节地址 x坐标
	lcd9648_write_cmd(0x00+x2);	//列低字节地址
	
	for(i = 0;i < 8;i++) 
	{
		lcd9648_write_dat(ascii_1608[num][i*2+1]);
	}

}

//显示字符串
//x,y:起点坐标 x:0-96 y:0-2 
//*p:字符串起始地址		  
void lcd_show_string(u8 x,u8 y,u8 Num,u8 *p)
{
	u8 i = 0;
	while(i < Num)
	{
		lcd_show_char(x,y,*p);
		x+=8;
		p++;
		i++;
		if(*p == '\0' || i >= 12)
			return;
	}
}

//m^n函数
//返回值:m^n次方.
u32 lcd_pow(u8 m,u8 n)
{
	u32 result=1;	 
	while(n--)result*=m;    
	return result;
}	

//显示数字,
//x,y:起点坐标
//num:数值(0~999999999);	 
//len:长度(即要显示的位数)
//mode:0-高位空字符填充  1-高位补0 
void lcd_show_num(u8 x,u8 y,u32 num,u8 len,u8 mode)
{
	u8 t,temp;
	u8 enshow=0;						   
	for(t=0;t<len;t++)
	{
		temp=(num/lcd_pow(10,len-t-1))%10;
		if(enshow==0&&t<(len-1))
		{
			if(temp==0)
			{
				if(mode == 1)
					lcd_show_char(x+(16/2)*t,y,'0');
				else
					lcd_show_char(x+(16/2)*t,y,' ');
 				continue;
			}else enshow=1; 
		 	 
		}
	 	lcd_show_char(x+(16/2)*t,y,temp+'0'); 
	}
}

//显示16*16汉字
//x,y:起点坐标 x:0-96 y:0-2
//*cn:字符串起始地址		  
void lcd_show_16HZ(u8 x, u8 y, u8 *cn)
{
	u8 j, x1, x2, wordNum;
	
	if(x>96||y>5)return;//超出范围了

	y *= 2;
	y += 0xB0;	   			//求取Y坐标的值

	while ( *cn != '\0')	 //在C语言中字符串结束以‘\0’结尾
	{
		x1 = (x >> 4) & 0x0F;   //由于X坐标要两句命令，分高低4位，所以这里先取出高4位
		x2 = x & 0x0F;          //去低四位

		lcd9648_write_cmd(y);	//页地址 y坐标
		lcd9648_write_cmd(0x10+x1);	//列高字节地址 x坐标
		lcd9648_write_cmd(0x00+x2);	//列低字节地址

		for (wordNum=0; wordNum<30; wordNum++)
		{
			//--查询要写的字在字库中的位置--//
			if ((CnChar16x16[wordNum].Index[0] == *cn)&&(CnChar16x16[wordNum].Index[1] == *(cn+1)))
			{
				for (j=0; j<32; j++) //写一个字
				{
					if (j == 16)	 //由于16X16用到两个Y坐标，当大于等于16时，切换坐标
					{
						lcd9648_write_cmd(y+1);	//页地址 y坐标
						lcd9648_write_cmd(0x10+x1);	//列高字节地址 x坐标
						lcd9648_write_cmd(0x00+x2);	//列低字节地址
					}
					lcd9648_write_dat(CnChar16x16[wordNum].Msk[j]);
				}
				x += 16;
			}
		}
		cn += 2;	//下一个字
	}
}

