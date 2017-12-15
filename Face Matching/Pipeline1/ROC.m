clear all
close all

fileID = fopen('results.txt','r');
formatSpec = '%d %f';
A = fscanf(fileID,formatSpec);
a=1;
b=1;
for i=1:2000
    if (mod(i,2)==0)
        Scores(a)=A(i);
        a=a+1;
    else
        Labels(b)=A(i);
        b=b+1;
    end
end

eerX=linspace(0,1,100);
eerY=linspace(1,0,100);


[X,Y]=perfcurve(Labels,Scores,'1');
figure (1)
plot(X,Y)
title('ROC')
xlabel('False Positive Rate')
ylabel('True Positive Rate')
hold on
plot(eerX,eerY,'--')