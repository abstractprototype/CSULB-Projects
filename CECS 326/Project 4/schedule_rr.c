/**
 * Round-robin scheduling
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
    while(head != NULL){
        struct node* temp = head;

        while(temp != NULL){
            if(temp->task->burst > QUANTUM){
                run(temp->task, QUANTUM);
                temp->task->burst = temp->task->burst - QUANTUM;
            }
            else{
                run(temp->task, temp->task->burst);
                printf("Task [%s] finished.\n", temp->task->name);
                struct node* ptr = temp;
                // Passes in entire list, and deletes previous task.
                delete(&head, ptr->task);
            }
            temp = temp->next;
        }
    }
    
}