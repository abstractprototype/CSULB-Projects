/*
   Sam Chen
   Paul Nguon
   CECS 326
   10/19/20
   Project 2
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

// Global Variables
int num_students;
int office_capacity;
int occupancy;
int current_student_id;

pthread_mutex_t globalLock, StudentSpeaks; //Mutex threads to lock/unlock
pthread_cond_t StudentQuestions_cv, ProfessorAnswers_cv, Office_Occupancy_cv; // Conditions for the mutex's
 
void *Professor();
void *Student(void *id);
 
void AnswerStart(int sid);
void AnswerDone(int sid);
void EnterOffice(int id);
void LeaveOffice(int id);
void QuestionStart(int id);
void QuestionEnd(int id);

/*
   The Professor Method handles with the number of student's questions. 
   We use mutex_lock on StudentSpeaks to allow the student to ask a question, 
   and when they are done, we use mutex_unlock to let the next student question. 
*/
void *Professor(){
   int counter = 0;
   int totalQuestions = 0;
   for(int i = 0; i < num_students; i++){
      totalQuestions += (i % 4) + 1;
   }

   while(counter < totalQuestions){
      
       pthread_mutex_lock(&StudentSpeaks);
       pthread_cond_wait(&StudentQuestions_cv, &StudentSpeaks);
       AnswerStart(current_student_id);
       AnswerDone(current_student_id);
       pthread_mutex_unlock(&StudentSpeaks);
       counter++;
   
   }
   
}
 
/*
   In the Student method, we initiliaze the number of questions for each student.
   When the Student enters the office, we start the mutex_lock when they speak and handle it in the for loop.
   The usleep(0) resets the time to let another student question. 
*/
void *Student(void *id){
   int student_id = *((int *)id);
   int num_of_questions = (student_id % 4) + 1;
   
   EnterOffice(student_id);
 
   for(int i = 0; i < num_of_questions; i++){
       pthread_mutex_lock(&globalLock);
       pthread_mutex_lock(&StudentSpeaks);      
       current_student_id = student_id;
       QuestionStart(student_id);
       pthread_cond_wait(&ProfessorAnswers_cv, &StudentSpeaks);
       QuestionEnd(student_id);
       pthread_mutex_unlock(&StudentSpeaks);
       pthread_mutex_unlock(&globalLock);
       usleep(0);
   }
   
   LeaveOffice(student_id);
}
 
//Profressor Actions
// Professor starts to answer a question.
void AnswerStart(int student_id){
   printf("Professor starts to answer question for student %d.\n", student_id);
   
}
//Professor finishes answering a question.
void AnswerDone(int student_id){
   printf("Professor is done with answer for student %d.\n", student_id);
   pthread_cond_signal(&ProfessorAnswers_cv);
   
}
 
//Student Actions
//Students are able to enter the office, but we keep track of the occupancy and office capacity.
void EnterOffice(int id){
   pthread_mutex_lock(&globalLock);
   while(occupancy >= office_capacity){
       pthread_cond_wait(&Office_Occupancy_cv, &globalLock);
   }
   occupancy++; // How many students in the office (3 stuendts, 2 capacity)
   printf("Student %d enters the office.\n", id);
   pthread_mutex_unlock(&globalLock);
}
 
//Students are able to leave the office, and decrementing the occupancy for the next student to enter. 
void LeaveOffice(int id){
   pthread_mutex_lock(&globalLock);
   printf("Student %d leaves the office.\n", id);
   occupancy--;
   pthread_cond_signal(&Office_Occupancy_cv);
   pthread_mutex_unlock(&globalLock);
}
 
//Number of waits is proportional to number of signals (EX: n = n)
//Student starts asking a question. 
void QuestionStart(int id){
   printf("Student %d asks a question.\n", id);
   pthread_cond_signal(&StudentQuestions_cv);
}

//Student finishes with asking a question.
void QuestionEnd(int id){
   printf("Student %d is satisfied.\n", id);
  
}
 
int main(int argc, char *argv[]){
   // Checks to make sure you have two arguments
   if(argc <= 2){
       printf("Error: Invalid amount of students and office capacity.\n");
       return 0;
   }
 
   num_students = atoi(argv[1]);
   office_capacity = atoi(argv[2]);
   if(!num_students || !office_capacity){
       printf("Arguments are invalid.\n");
       return 0;
   }
   printf("Number of students:%d, Capacity:%d\n", num_students, office_capacity);
   occupancy = 0;
   //Initialize the mutex's and conditions
   pthread_mutex_init(&globalLock, NULL);
   pthread_mutex_init(&StudentSpeaks, NULL);
   pthread_cond_init(&ProfessorAnswers_cv, NULL);
   pthread_cond_init(&Office_Occupancy_cv, NULL);
   pthread_cond_init(&StudentQuestions_cv, NULL);

   //Create a professor thread and start the Professor method.
   pthread_t professor_thread;
   pthread_create(&professor_thread, NULL, Professor, NULL);
   usleep(1);
   
   //Create an array of student threads with student id's. 
   pthread_t student_threads[num_students];
   int student_ids[num_students];
 
   for(int i = 0; i < num_students; i++){
       student_ids[i] = i;
       pthread_create(&student_threads[i], NULL, Student, (void *)&student_ids[i]);
   }
 
   for(int i = 0; i < num_students; i++){
       pthread_join(student_threads[i], NULL);
   }

   pthread_join(professor_thread, NULL);
   printf("Professor finished answering questions.\n");
 
   return 0;
 
}

