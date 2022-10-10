#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int Check_Rut(char rut[])
{
char ver[12] = "43298765432";
int dv, dc, total, x = 0;

        if (strlen(rut) != 11)
        {
                return (-1);
        }
        dc = rut[10];

        while (x <= 10)
        {
                total += (rut[x] * ver[x]);
		printf("total %d is: %d\n", x, total);
                x++;
        }
	printf("total is %d\n", total);
        dv = 11 - (total % 11);
        if (dv == 11)
        {
                dv = 0;
        }
        else if(dv == 10)
        {
                dv = 1;
        }
        if(dv == dc)
        {
                return (0);
        }
        else
        {
		printf("dv = %d\n", dv);
		printf("dc = %d\n", dc);
                return (-1);
        }
}
/**
 * main - check the code
 *
 * Return: Always 0.
 **/
int main(void)
{
char rut[12] = "21100320017";
int a;

	a = Check_Rut(rut);

	if (a == 0)
	{
		printf("Sexo\n");
		return (0);
	}
	else if (a == -1);
	{
		printf("No Sexo\n");
		return (1);
	}
}
