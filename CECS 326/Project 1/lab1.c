#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <pthread.h>
 
//Sam Chen 013502214
//Paul Nguon 015782505 
//Global variable
int sharedVariable = 0;
pthread_mutex_t lock;
pthread_barrier_t barrier;
 
void* SimpleThread(void* which){
   int *p;
   p = which;
   int num, val;
 
   for(num = 0; num < 20; num++){
       if(random() > RAND_MAX/2)
           usleep(500);

        #ifdef PTHREAD_SYNC 
        pthread_mutex_lock(&lock); //locks this critical section for one thread to access only
        #endif
	val = sharedVariable;
        printf("%d", *p);
        printf("***thread %d sees value %d\n", *p, val);
        sharedVariable = val + 1;
	#ifdef PTHREAD_SYNC
        pthread_mutex_unlock(&lock); //unlocks this critical section for the next thread to use
        #endif
   }
   
   pthread_barrier_wait(&barrier); //waits for the threads to join back together
   
   val = sharedVariable;
   printf("Thread %d sees final value %d\n", *p, val);
 
   pthread_exit(0);
}
 
int main(int argc, char *argv[]){

    int i;

   pthread_t threads[atoi(argv[1])]; //atoi changed char to int
 
   pthread_mutex_init(&lock, NULL); //initialize mutex lock
 
   pthread_barrier_init(&barrier, NULL, atoi(argv[1])); //initialize pthread barrier
 
  
   if(argc <= 1){ //Must have user supply an argument 
       printf("No argument supplied\n");
   }
   else {
       printf("More than one argument supplied\n");
       printf("argv[1]: %d\n", atoi(argv[1]));

       int valid = 1;
       for(i = 0; i < strlen(argv[1]); i++){
           if(argv[1][i] < '0' || argv[1][i] > '9'){
               valid = 0;
               break;
           }
       }
        if(valid == 0){ //Must have user input a number
            printf("\nPlease provide a positive integer as argument\n");
        }
        else{
            int num_args = atoi(argv[1]);
            int *threadIds = (int*) malloc(sizeof(int) * num_args);
        
            for(int i = 0; i < num_args; i++){
                threadIds[i] = i;
            }
        
            for(int i = 0; i < num_args; i++){
        
                pthread_attr_t attribute;
                pthread_attr_init(&attribute);
                pthread_create(&threads[i], &attribute, SimpleThread, &threadIds[i]);
            }
            //Wait until thread is done its work
            for(int i = 0; i < num_args; i ++){
                pthread_join(threads[i], NULL);
            }
        }
   }  
   pthread_mutex_destroy(&lock);
   pthread_barrier_destroy(&barrier);

   return 0;
}

