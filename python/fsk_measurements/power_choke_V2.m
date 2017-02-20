data = importfile_power_choke('1_layer_power_choke_test.csv', 29, 115);

plot(data(:,1), data(:,2));

data = importfile_power_choke('1_layer_power_choke_test.csv', 130, 179);
figure('color','white');
plot(data(:,1), data(:,2));

%% Onelayer
close all; clear all; clc;

data = importfile_onelayer('1LAYER.csv', 17, 217);
plot(data(:,1), data(:,2),'color','RED');
hold on;
data = importfile_onelayer('1LSTRAY.csv', 17, 217);
plot(data(:,1), data(:,2),'color','GREEN');
hold on;
data = importfile_onelayer('MULTILAY.csv', 17, 217);
plot(data(:,1),data(:,2),'color','BLUE');
legend('oneLayer','Lstray','multiLayer');



figure()
data = importfile_onelayer('1LAYER.csv', 221, 421);
plot(data(:,1), data(:,2),'color','RED');
hold on;
data = importfile_onelayer('1LSTRAY.csv', 221, 421);
plot(data(:,1), data(:,2),'color','GREEN');
hold on;
data = importfile_onelayer('MULTILAY.csv', 221, 421);
plot(data(:,1),data(:,2),'color','BLUE');

legend('oneLayer','Lstray','multiLayer');
% data = importfile_power_choke('1_layer_power_choke_test.csv', 130, 179);
% figure('color','white');
% plot(data(:,1), data(:,2));

