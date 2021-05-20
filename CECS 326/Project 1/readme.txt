Project 1 README

This program will introduce threads subsystem of Linux. It will create multiple threads and able to synchronize data with Pthread mutex.

To get started: First install and set up Virtual Box then use Ubuntu as the operating system for this project. 

Using the terminal in Ubuntu, navigate to the folder with the proper lab1.c file. You can do this by using the cd command.

Now make an executable for lab1.c with the command "gcc -pthread lab1.c -o lab1exe".

This will allow you to use the next command "./lab1exe" to run the file. 

To create a make file that will automatically input the gcc command, this will help manage your debugging more efficiently. This creates an executable for you to run your code on the terminal. 

To install the makefile command use "sudo apt-get install build-essential"

To use the make file: Type "make lab1" for part 1 without synchronization. Type "make lab1_sync" for part 2 with synchronization

Finally, test a single output "1, 2, 3, 4, 5" after ./lab1exe to display multiple threads running in parallel.

