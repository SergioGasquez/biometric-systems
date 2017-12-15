fileID = fopen('imagespath.txt','r');

tline = fgetl(fileID);
while ischar(tline)
    eyes.x(1)=100;
    eyes.y(1)=110;
    eyes.x(2)=145;
    eyes.y(2)=110;
    size=[100 100];
    X=imread(tline);
    Y = register_face_based_on_eyes(X,eyes,size);
    imwrite(uint8(Y),tline);
    tline = fgetl(fileID);
end

