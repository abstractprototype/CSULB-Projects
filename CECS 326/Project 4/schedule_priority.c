/*
 * Priority scheduling
 */
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

#include "task.h"
#include "list.h"
#include "cpu.h"

/*
 * Your code and design here:
 */
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
    struct node* temp = head;
    while(temp != NULL){
        struct node* temp2 = head;
        if(temp->task->priority > temp2->task->priority){
            temp2 = temp;
        }
        else{
            temp = temp->next;
            run(temp2->task, temp2->task->burst);
            delete(&head, temp2->task);
        }
    }
}