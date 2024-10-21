start=0;
End=2*pi;
fs=100;
r2 = 20
r3 = 60
t =linspace(start,End,(End-start)*fs);
O = t
x4 = r2*cos(O) + sqrt( r3^2  - r2^2*sin(O).^2 );
plot(O,x4,'r');

