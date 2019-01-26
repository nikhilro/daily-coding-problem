#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

struct Node {
    int val;
    struct Node * xor;
};

void add(int element, struct Node * head) {
    struct Node * current = head;
    struct Node * previous = NULL;

    while(current->xor != previous) {
        struct Node * next = NULL;
        printf("%p %p %p \n", previous, current, next);
        next = (struct Node *)((intptr_t)current->xor ^ (intptr_t)previous);
        printf("%p %p %p \n", previous, current, next);
        previous = current;
        current = next;
    }

    struct Node * tail = NULL;
    tail = malloc(sizeof(struct Node));
    tail->val = element;
    tail->xor = current;

    if (!previous) {
        current->xor = tail;
    } else {
        current->xor = (struct Node *)((intptr_t)previous ^ (intptr_t)tail);
    }

    printf("%p %p %p \n\n", previous, current, tail);

    return;
}

struct Node * get(int index, struct Node * head) {
    struct Node * current = head;
    struct Node * previous = NULL;

    while(--index) {
        struct Node * next = NULL;
        next = (struct Node *)((intptr_t)current->xor ^ (intptr_t)previous);
        previous = current;
        current = next;
    } 
    return current;
}

void print(struct Node * head) {
    struct Node * current = head;
    struct Node * previous = NULL;

    while(current->xor != previous) {
        printf("%d ", current->val);
        struct Node * next = NULL;
        next = (struct Node *)((intptr_t)current->xor ^ (intptr_t)previous);
        previous = current;
        current = next;
    }
    printf("%d \n", current->val); 
    return;
}

int main() {
    struct Node * head =NULL;
    head = malloc(sizeof(struct Node));
    head->val = 1;
    head->xor = NULL;
    add(2, head);
    add(3, head);
    add(4, head);
    printf("%d \n", get(4, head)->val);
    print(head);
    return 0;
}
