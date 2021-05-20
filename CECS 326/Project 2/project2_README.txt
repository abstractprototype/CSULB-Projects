Project 2 README

----

The 2nd part of the project, we will utilize pthreads still from the last part of the project but now designing a real
scenario/application with multithreaded synchronization. 

Make sure you have a virtual machine installed such as Virtual Box that has Linux or Ubuntu.

The file will be called lab2.c, and you can use the terminal in Ubuntu to navigate to that file by using the cd command. 


Once you're navigated into the project folder, make an executable for lab2.c with the command "gcc -pthread -o lab2exe lab2.c"

This will allow you to use the next command "./lab2exe 3 2" followed along with the two paramters. First parameter will be the number of students 
and the second parameter will be the capacity amount. 

To create a makefile that will automatically input the gcc command "gcc -pthread -o lab2exe lab2.c", we install the makefile command using
"sudo apt-get install build essential" into your terminal (Make sure you are still in your project directory before running this command)

To use the makefile now: Type "make lab2"

Finally, test it using the inputs "3 2" after ./lab2exe to run the application.


 