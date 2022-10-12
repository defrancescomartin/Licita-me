#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
* Check_Rut - Function that checks if a RUT code given is valid through DV.
* @rut: rut code given
* Return: 0 if valid, -1 otherwise
**/
int Check_Rut(char rut[])
{
char ver[12] = "43298765432";
int dv, dc, total = 0, x = 0;
int val_a = 0, val_b = 0;

	if (strlen(rut) != 12)
	{
		printf("RUT code should be 12 digits.\n");
		return (-1);
	}
	dc = rut[11] - '0';

	while (x <= 10)
	{
		val_a = rut[x] - '0';
		val_b = ver[x] - '0';
		total += (val_a * val_b);
		x++;
	}
	dv = 11 - (total % 11);
	if (dv == 11)
	{
		dv = 0;
	}
	else if (dv == 10)
	{
		dv = 1;
	}
	if (dv == dc)
	{
		return (0);
	}
	else
	{
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
char rut[12] = "211003420017";
int a;

	a = Check_Rut(rut);

	if (a == 0)
	{
		printf("Valid RUT\n");
		return (0);
	}
	else if (a == -1)
	{
		printf("Invalid RUT\n");
		return (-1);
	}
}
