
z1 = 0;
a = 0;
b = 2;
h = 0.2;
N = (b - a) / h;
alpha = 0;
beta = -4;
z2 = (beta - alpha) / (b -a);
p = @(x) 2 ;
q = @(x) -1 ;
r = @(x) x * exp(x) - x;
M = 1000;
TOL = 0.0001;

f1 = @(x, u1, u2) u2;
f2 = @(x, u1, u2) p(x)*u2 + q(x)*u1 + r(x);

u10 = alpha;
u20 = z1;
[~, v1, v2] = RK4(a, b, N, u10,u20, f1, f2);

u10 = alpha;
u20 = z2;
[t, w1, w2] = RK4(a, b, N, u10,u20, f1, f2);

k = 0;
TK = (beta - alpha) / (b -a);

while k <= M
    z3 = z2 - ([w1(N + 1) - beta] * (z2 - z1)) / (w1(N+1) - v1(N+1));
    if (abs(z3 - z1) < TOL)
        break
    end
    k = k + 1;

    z1 = z2;
    z2 = z3;
    u10 = alpha;
    u20 = z1;
    [~, v1, v2] = RK4(a, b, N, u10,u20, f1, f2);
    u10 = alpha;
    u20 = z2;
    [~, w1, w2] = RK4(a, b, N, u10,u20, f1, f2);
end

u10 = alpha;
u20 = z3;
[t, w1, w2] = RK4(a, b, N, u10,u20, f1, f2);

y = @(x) ((1/6) * x^3 * exp(x)) - (5/3) * x * exp(x) + 2 * exp(x) - x - 2;
errors = zeros(11, 1);
ys = zeros(11, 1);

for i = 1:N
    ys(i) = y(t(i));
    errors(i) = abs(y(t(i)) - w1(i));
end

errors
plot(t, errors)

function [t, w1, w2] = RK4(a, b, N, u10, u20, f1, f2)
    h = (b-a)/N;
    
    %% Initial Values
    t = zeros(N+1,1);
    w1 = zeros(N+1,1);  % w1 approximates u1
    w2 = zeros(N+1,1);  % w2 approximates u2
    
    t(1) = a;
    w1(1) = u10;
    w2(1) = u20;
    
    %% Do RK4 Method
    
    for n = 1:N
        t(n+1) = a + n*h;
        
        k(1,1) = h * f1( t(n), w1(n), w2(n) );
        k(1,2) = h * f2( t(n), w1(n), w2(n) );
    
        k(2,1) = h * f1( t(n) + h/2, w1(n) + (1/2)*k(1,1), w2(n) + (1/2)*k(1,2) );
        k(2,2) = h * f2( t(n) + h/2, w1(n) + (1/2)*k(1,1), w2(n) + (1/2)*k(1,2) );
        
        k(3,1) = h * f1( t(n) + h/2, w1(n) + (1/2)*k(2,1), w2(n) + (1/2)*k(2,2) );
        k(3,2) = h * f2( t(n) + h/2, w1(n) + (1/2)*k(2,1), w2(n) + (1/2)*k(2,2) );
    
        k(4,1) = h * f1( t(n+1), w1(n) + k(3,1), w2(n) + k(3,2) );
        k(4,2) = h * f2( t(n+1), w1(n) + k(3,1), w2(n) + k(3,2) );
    
        w1(n+1) = w1(n) + (1/6)*( k(1,1) + 2*k(2,1) + 2*k(3,1) + k(4,1) );
        w2(n+1) = w2(n) + (1/6)*( k(1,2) + 2*k(2,2) + 2*k(3,2) + k(4,2) );
    end
end


