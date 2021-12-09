#include <stdio.h>

typedef struct student{
  char name[40];
  int roll;
  int age;
  float marks;
}student;

int main(void)
{
  student stu;
  printf("\nPlease Enter Name:");
  scanf("%s",stu.name);

  printf("\nPlease Enter roll:");
  scanf("%i",&stu.roll);

  printf("\nPlease Enter age:");
  scanf("%i",&stu.age);

  printf("\nPlease Enter marks:");
  scanf("%f",&stu.marks);

  printf("\n%s %i %i %.f",stu.name, stu.roll, stu.age, stu.marks );

}
