#include<stdio.h>

int main(){
    int x = 11,y = 22,*px,*py;
    px = &x;
    py = &y;
    printf("preincrement  : %d\n",(*px)++);
    printf("postincrement : %d",++*(px));
    return 0;

}