str1=fileread('doc1.txt');
c1=strsplit(str1, {' ',',','.','\n'});
str2=fileread('doc2.txt');
c2=strsplit(str2, {' ',',','.','\n'});
dic=union(c1,c2);

finalList=dic(2:size(dic,2));
finalList
vectorOne=zeros(size(finalList,2),1);
vectorTwo=zeros(size(finalList,2),1);

for i=1:size(c1,2)
    pos=find(strcmp(finalList,c1(i)));
    vectorOne(pos,:)=vectorOne(pos,:)+1;
end

for i=1:size(c2,2)
    pos=find(strcmp(finalList,c2(i)));
    vectorTwo(pos,:)=vectorTwo(pos,:)+1;
end

%find cosine distance
similarity=(sum(vectorOne.*vectorTwo))/(sqrt(sum(vectorOne.^2))*sqrt(sum(vectorTwo.^2)))
distance=1-similarity

