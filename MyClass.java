classMyClass<TextendsComparable<T>>
{
T[]vals;
MyClass(T[]o)
{
vals=o;
}
publicTmin()
{
Tv=vals[0]; for(inti=1;i<vals.length;i++)if(vals[i].compareTo(v)<0) v=vals[i];returnv;
}
publicTmax()
{
Tv=vals[0]; for(inti=1;i<vals.length;i++)if(vals[i].compareTo(v) >0) v=vals[i];returnv;
}
}
classgendemo
{
publicstaticvoidmain(Stringargs[])
 
{
inti; Integerinums[]={10,2,5,4,6,1};Characterchs[]={'v','p','s','a','n','h'}; 
Doubled[]={20.2,45.4,71.6,88.3,54.6,10.4};
MyClass<Integer> iob = new MyClass<Integer>(inums);
MyClass<Character>cob=newMyClass<Character>(chs);
MyClass<Doubl e>dob = new MyClass<Double>(d);
System.out.println("Max value in inums: " + iob.max());
System.out.println("Min value in inums: " + iob.min());
System.out.println("Maxvalue inchs:"+cob.max())
System.out.println("Min value in chs: " + cob.min()); 
System.out.println("Maxvalueinchs:"+dob.max()); 
System.out.println("Minvalueinchs:"+dob.min());
}
}
