clear all;
%% Train Matrix
filename = 'trainPaths.txt';
fid = fopen(filename);
Z=[];
tline = fgetl(fid);
while ischar(tline)
    X=imread(tline);
    Y=double(X(:));
    Z=[Z Y];
    tline = fgetl(fid);
end
%% Test Matrix
filename = 'testPaths.txt';
fid = fopen(filename);
Ztest=[];
tline = fgetl(fid);
while ischar(tline)
    X=imread(tline);
    Y=double(X(:));
    Ztest=[Ztest Y];
    tline = fgetl(fid);
end
%% We get the model
Z=double(Z);
model= perform_pca_PhD(Z,200)
ftrain = linear_subspace_projection_PhD(Z, model);
ftest = linear_subspace_projection_PhD(Ztest, model);

%% We concatenate train matrix
H=[];
a=1;
for i=1:2200
   A=ftrain(:,a);
   a=a+1;
   B=ftrain(:,a);
   a=a+1;
   H=[H;A' B'];
end
%% We concatenate test matrix
Htest=[];
a=1;
for i=1:1000
   A=ftest(:,a);
   a=a+1;
   B=ftest(:,a);
   a=a+1;
   Htest=[Htest;A' B'];
end
%% We get the SVM model
labels=[ones(1,1100) zeros(1,1100)];
CVSVMModel = fitcsvm(H,labels);
%% We get the prediction scores
[label,score] = predict(CVSVMModel,Htest)

%% We represent ROC
scoreN=score(1:end,2)
labelN=[ones(1,500) zeros(1,500)];


eerX=linspace(0,1,100);
eerY=linspace(0,0,100);


[Xa,Ya]=perfcurve(labelN,scoreN','1');
plot(Xa,Ya)
title('ROC')
xlabel('False Positive Rate')
ylabel('True Positive Rate')
hold on
plot(eerX,eerX,'--')


