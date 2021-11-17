def count(*t):
    ce=0;
    oe=0;
    for i in t:
        if i%2==0:
            ce=ce+1;
            print(ce)
        else:
            oe=oe+1;
            print(oe)
count(2,3,4,5,6,7,8)