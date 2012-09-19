% compute the pade diagonal terms
A(1:9,1:9) = 0.0;
A(2:9,1) = [0.11680327031603929       0.54811809877664308       0.32415586486790715       0.70189121153216261        1.1787485995196625       0.32147689077808972       0.28932920170028076       8.14408123304494191E-002];
A = A + diag([-3.5619639498212341 -1.24670000000000011E-004   -2.82920000000000036E-004 -4.25240000000000015E-004 -1.33041999999999991E-003  -2.92466999999999987E-003  -6.66487999999999976E-003 -1.63478100000000008E-002  -3.55460000000000012E-002]);
A(1,2:9) = [1.24670000000000011E-004   2.82920000000000036E-004 4.25240000000000015E-004 1.33041999999999991E-003  2.92466999999999987E-003  6.66487999999999976E-003 1.63478100000000008E-002  3.55460000000000012E-002];

tic
[f,e] = log2(norm(A,'inf'));
s = max(0,e+1);
A = A/2^s;

X = A;
c = 1/2;
E = eye(size(A)) + c*A;
D = eye(size(A)) - c*A;
q = 6; p=1;
for k = 2:q
    c = c*(q-k+1)/(k*(2*q-k+1));
    X = A*X;
    cX = c*X;
    E = E + cX;
    if p, D = D + cX;
    else D = D - cX; end
    p = ~p;
end

E = D\E;

for k = 1:s, E = E*E; end
toc