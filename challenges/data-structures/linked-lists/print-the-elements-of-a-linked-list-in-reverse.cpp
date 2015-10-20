#include <iostream>
using namespace std;

class Stack {
    int Arr[100];
    int size;
    public:
    Stack() {
        size = 0;
    }
    void push(int data) {
        Arr[size] = data;
        size++;
    }
    int pop() {
        int data = Arr[size-1];
        size--;
        return data;
    }
    bool isEmpty() {
        return size == 0;
    }
};

void ReversePrint(Node *head)
{
    Stack S;
    Node *temp;
    temp = head;
    while(temp!=NULL) {
        S.push(temp->data);
        temp = temp->next;
    }
    while(!S.isEmpty()) {
        cout<<S.pop()<<'\n';
    }
}

int main() {
    Stack S;
    S.push(5);
    cout<<S.pop();
}
