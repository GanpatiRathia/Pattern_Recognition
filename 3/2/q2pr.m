u_1 = [0; 0];
Sigma1 = [1 0; 0 1];
%finding deviation.
dev1 = sqrt(Sigma1(1,1));

% Getting points from -1 to 1
x1 = [0:50]*2/50 - 1;

% finding points from -dev to +dev from the mean value.
x1 = dev1*x1 + u_1(1);

%Substituting in circle equation.
y1 = sqrt(dev1^2 - (x1 - u_1(1)).^2) + u_1(2);

u_2 = [5;0];
Sigma2 = [4 0; 0 4];
%finding deviation.
dev2 = sqrt(Sigma2(1,1));
% Getting points from -1 to 1
x2 = [0:50]*2/50 - 1;
% finding points from -dev to +dev from the mean value.
x2 = dev2*x2 + u_2(1);
%Substituting in circle equation.
y2 = sqrt(dev2^2 - (x2 - u_2(1)).^2)+ u_2(2);


%Plotting the graph.
figure;
plot(x1,y1,'g-','LineWidth',3);
hold on;
plot(x1,-y1,'g-','LineWidth',3);
plot(x2,y2,'b-','LineWidth',3);
plot(x2,-y2,'b-','LineWidth',3);
axis equal;
xlabel('x_1'); 
ylabel('x_2');

