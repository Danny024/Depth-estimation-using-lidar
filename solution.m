clear;clc;
% Parameters
n = 128; % number of pixels in each dimension
t_max = 300; % maximum time of flight
t = (1:t_max)'; % time vector
r = 5*ones(n); % target intensity/amplitude
b = ones(n); % background/dark photon level
g = @(x) exp(-x.^2/3^2); % Gaussian impulse response

% Depth map
load Depth_CameraMan.mat % load Cameraman image
t_ij = double(CameraMan)/255 * t_max; % scale to [0, t_max]


%Generates the data cube
s = zeros(n,n,t_max);
for i = 1:n
    for j = 1:n
        s(i,j,:) = r(i,j) * g(t - t_ij(i,j)) + b(i,j);
    end
end


% Generate noisy data cube
y = poissrnd(s);


% Matched filtering to estimate depth map
t_hat = zeros(n);
for i = 1:n
    for j = 1:n
        y_vec = reshape(y(i,j,:), [], 1);
        xcorr_g_y = xcorr(g(t), y_vec, 'biased');
        [~, max_idx] = max(xcorr_g_y);
        t_hat(i,j) = t(max_idx);
    end
end

% Display clean Camera image and the estimated depth maps
figure;
subplot(1,2,1);
imagesc(t_ij);
title('Clean Depth Map');
colorbar;
subplot(1,2,2);
imagesc(t_hat);
title('Estimated Depth Map');
colorbar;

% The depth map of the estimated image can be improved by using  a more pratical
% impulse response to model response of the LIDAR system. A deep learning/ 
% machine learning approach can be used to determine the depth map estimation.
