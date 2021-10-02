 #include <stdio.h>

int main()
{
   char name[25];
    printf("Welcome to Hacktoberfest 2021\n");
    printf("Enter your name : \n");   //Get User name
    scanf("%[^\n]s",&name);  //User inputs the name
	printf("\nYour name is = %s",name);
    getch();
    return 0;
}
