
% Normal distribution rotated and scaled.
x = normrnd(0,1,1,300);
y = normrnd(0,1,1,300);

x = x * 20;

theta = 15;
R = [cosd(theta) -sind(theta); sind(theta) cosd(theta)];

normplot = R * [x ; y];

% Uniform distribution
x = unifrnd(0,1,1,300);
y = unifrnd(0,1,1,300);

% display plots
subplot(1,2,1);
scatter(normplot(1,:), normplot(2,:));
axis equal;
lsline;

subplot(1,2,2);
scatter(x, y);
lsline;

% save figure
print('2dplots.pdf', '-dpdf')
