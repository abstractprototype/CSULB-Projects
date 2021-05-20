/**
 * FCFS scheduling
 */
 
#include <stdlib.h>
#include <stdio.h>

#include "task.h"
#include "list.h"
#include "cpu.h"

//Your code and design here
int tempid = 1;
struct node* head;

void add(char *name, int priority, int burst){
    struct task* temp = NULL;
    temp = malloc(sizeof(Task));
    temp->name = name;
    temp->priority = priority;
    temp->burst = burst;
    temp->tid = tempid;
    tempid++;
    insert(&head, temp);
}

void schedule(){
    struct task* temp;
    // Iterates through list
    // Reads item and deletes and iterates again.
    while(head != NULL){
        temp = head->task;
        run(temp, temp->burst);
        delete(&head, temp);
    }
}
