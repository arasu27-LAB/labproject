importjava.util.Scanner;

interfaceShape
{
voidinput(); void area();
}
class CircleimplementsShape
{
intr=0;
doublepi=3.14,ar=0; @Override
publicvoidinput()
{
r=5;
}
@Override
publicvoidarea()
{
ar = pi * r * r; System.out.println("Areaofcircle:"+ar);
}
}
classRectangleextendsCircle
{
intl=0,b=0; double ar;
publicvoidinput()
{
super.input(); l =6;
b=4;
 
}
publicvoidarea()
{
super.area();
ar=l*b;
System.out.println("Areaofrectangle:"+ar);
}
}
publicclassDemo
{
publicstaticvoidmain(String[]args)
{
Rectangleobj=newRectangle(); obj.input();
obj.area();
}
}
