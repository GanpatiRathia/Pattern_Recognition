P=[70,90,80];
Q=[40,6,6];
R=[10,20,30];
S=[32,43,55];
T=[70,60,40];

X=[25,20,40];

a = ['P','Q','R','S','T','X']';
b = num2str(a);
c =cellstr(b);

D=zeros(5,1);
D(1)=sqrt(sum((X-P).^2));
D(2)=sqrt(sum((X-Q).^2));
D(3)=sqrt(sum((X-R).^2));
D(4)=sqrt(sum((X-S).^2));
D(5)=sqrt(sum((X-T).^2));
[value,index]=min(D);

if index==1
    fprintf("P is the closest\n");
elseif index==2
    fprintf("Q is the closest ");
elseif index==3
    fprintf("R is the closest ");
elseif index==2
    fprintf("S is the closest ");
else
    fprintf("T is the closest ");
end
fprintf("with distance %f\n",value);
x=[70,40,10,32,70,25];
y=[90,6,20,43,6,20];
z=[80,6,30,55,40,40];

point_id=[P,Q,R,S,T,X];
scatter3(x,y,z,'b*')
hold on
scatter3(x(6),y(6),z(6),'g*') %given vector
scatter3(x(index),y(index),z(index),'r*') %min distance vector
hold off
text(x,y,z,c,'Fontsize',12)
