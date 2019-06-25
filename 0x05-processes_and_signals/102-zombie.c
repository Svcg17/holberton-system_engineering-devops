#include <unistd.h>
#include <stdio.h>
int infinite_while(void);

/**
 * main - main function
 * Return: 0
 */
int main(void)
{
	int i = 0;
	pid_t ret = 0;

	for (i = 0; i < 5; i++)
	{
		ret = fork();
		if (ret < 0)
			return (0);
		if (ret == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}
	infinite_while();
	return (0);
}
/**
 * infinite_while - loops infinitely
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
