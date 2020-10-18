#include <stdio.h>

int main()
{
    char name[50];
    
    printf("Enter your name : ");//Get User name
    scanf("%s",name);//User inputs the name

    printf("Hi %s\nWelcome to Hacktoberfest 2020\n", name);

    return 0;
}
 